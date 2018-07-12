# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods
import json
from flask import Blueprint, jsonify, request
from app import db
from app.models import Tweet
from app.utils import validate_token
from app.schemas import tweets_schema, tweet_schema
from datetime import datetime

api = Blueprint('tweets', __name__)

@api.route('/tweets', methods=['GET'])
def get_all_tweet():
    list_twt = db.session.query(Tweet).all()
    return tweets_schema.jsonify(list_twt), 200

@api.route('/tweets/<int:id>', methods=['GET'])
def get_tweet(id):
    tweet = db.session.query(Tweet).get(id)
    if tweet is not None :
        return tweet_schema.jsonify(tweet)
    return jsonify({"error": "Tweet not found"}), 404

@api.route('/tweets', methods=['POST'])
def post_tweet():
    if 'Authorization' not in request.headers:
        return jsonify({"error" : "Not authorized"}), 403
    user = validate_token(request.headers['Authorization'])
    if user is None:
        return jsonify({"error" : "Not authorized"}), 403
    try:
        payload = json.loads(request.data)
    except ValueError :
        return jsonify({"error" : "Bad payload received"}), 422
    if 'text' not in payload:
        return jsonify({"error" : "Bad payload received"}), 422
    tweet = Tweet(text=payload['text'], created_at=datetime.now(), user_id=user.id)
    db.session.add(tweet)
    db.session.flush()
    db.session.commit()
    return tweet_schema.jsonify(tweet), 201

@api.route('/tweets/<int:id>', methods=['DELETE'])
def delete_tweet(id):
    if 'Authorization' not in request.headers:
        return jsonify({"error" : "Not authorized"}), 403
    user = validate_token(request.headers['Authorization'])
    if user is None:
        return jsonify({"error" : "Not authorized"}), 403
    tweet = db.session.query(Tweet).get(id)
    if user.id != tweet.user_id:
        return jsonify({"error" : "Not authorized (not your tweet)"}), 403
    if tweet is not None :
        db.session.delete(tweet)
        db.session.flush()
        db.session.commit()
        return '', 204
    return jsonify({"error": "Tweet not found"}), 404

@api.route('/tweets/<int:id>', methods=['PATCH'])
def change_tweet(id):
    if 'Authorization' not in request.headers:
        return jsonify({"error" : "Not authorized"}), 403
    user = validate_token(request.headers['Authorization'])
    if user is None:
        return jsonify({"error" : "Not authorized"}), 403
    try:
        payload = json.loads(request.data)
    except ValueError :
        return jsonify({"error" : "Bad payload received"}), 422
    if 'text' not in payload:
        return jsonify({"error" : "Bad payload received"}), 422
    tweet = db.session.query(Tweet).get(id)
    if user.id != tweet.user_id:
        return jsonify({"error" : "Not authorized (not your tweet)"}), 403
    if tweet is not None :
        tweet.text = payload['text']
        db.session.commit()
        return '', 204
    return jsonify({"error": "Tweet not found"}), 404
