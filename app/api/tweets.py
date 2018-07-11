# app/api/tweets.py
from flask import Blueprint, jsonify, request
from app.db import tweet_repository
from app.models import Tweet
import json

api = Blueprint('tweets', __name__)

@api.route('/tweets', methods=['GET'])
def get_all_tweet():
    list_twt = []
    for tweet in tweet_repository.get_all():
        response = {
            'id': tweet.id,
            'text': tweet.text,
            'created_at': tweet.created_at
        }
        list_twt.append(response)
    return jsonify(list_twt), 200

@api.route('/tweets/<int:id>', methods=['GET'])
def get_tweet(id):
    tweet = tweet_repository.get(id)
    if tweet is not None:
        response = {
            'id': tweet.id,
            'text': tweet.text,
            'created_at': tweet.created_at
        }
        return jsonify(response), 200
    return jsonify({"error": "Tweet not found"}), 404

@api.route('/tweets', methods=['POST'])
def post_tweet():
    try:
        payload = json.loads(request.data)
    except ValueError :
        return jsonify({"error" : "Bad payload received"}), 422
    if 'text' not in payload:
        return jsonify({"error" : "Bad payload received"}), 422
    tweet = Tweet(payload['text'])
    tweet_repository.add(tweet)
    response = {
            'id': tweet.id,
            'text': tweet.text,
            'created_at': tweet.created_at
        }
    return jsonify(response), 201

@api.route('/tweets/<int:id>', methods=['DELETE'])
def delete_tweet(id):
    res = tweet_repository.delete(id)
    if res is False:
        return jsonify({'error' : 'Tweet not found'}), 404
    return '', 204

@api.route('/tweets/<int:id>', methods=['PATCH'])
def change_tweet(id):
    try:
        payload = json.loads(request.data)
    except ValueError :
        return jsonify({"error" : "Bad payload received"}), 422
    if 'text' not in payload:
        return jsonify({"error" : "Bad payload received"}), 422
    tweet = tweet_repository.get(id)
    if tweet is not None:
        tweet.change_text(payload['text'])
        return '', 204
    return jsonify({'error' : 'Tweet not found'}), 404
