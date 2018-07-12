# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods
import json
from flask import Blueprint, jsonify, request
from app import db
from app.models import User
from app.schemas import user_schema, users_schema
from datetime import datetime

api = Blueprint('user', __name__)

@api.route('/users', methods=['GET'])
def get_all_users():
    list_users = db.session.query(User).all()
    return users_schema.jsonify(list_users), 200

@api.route('/tweets/<int:id>', methods=['GET'])
def get_tweet(id):
    tweet = db.session.query(Tweet).get(id)
    if tweet is not None :
        return tweet_schema.jsonify(tweet)
    return jsonify({"error": "Tweet not found"}), 404

@api.route('/tweets', methods=['POST'])
def post_tweet():
    try:
        payload = json.loads(request.data)
    except ValueError :
        return jsonify({"error" : "Bad payload received"}), 422
    if 'text' not in payload:
        return jsonify({"error" : "Bad payload received"}), 422
    tweet = Tweet(text=payload['text'], created_at=datetime.now())
    db.session.add(tweet)
    db.session.flush()
    db.session.commit()
    return tweet_schema.jsonify(tweet), 201

@api.route('/tweets/<int:id>', methods=['DELETE'])
def delete_tweet(id):
    tweet = db.session.query(Tweet).get(id)
    if tweet is not None :
        db.session.delete(tweet)
        db.session.flush()
        db.session.commit()
        return '', 204
    return jsonify({"error": "Tweet not found"}), 404

@api.route('/tweets/<int:id>', methods=['PATCH'])
def change_tweet(id):
    try:
        payload = json.loads(request.data)
    except ValueError :
        return jsonify({"error" : "Bad payload received"}), 422
    if 'text' not in payload:
        return jsonify({"error" : "Bad payload received"}), 422
    tweet = db.session.query(Tweet).get(id)
    if tweet is not None :
        tweet.text = payload['text']
        db.session.commit()
        return '', 204
    return jsonify({"error": "Tweet not found"}), 404
