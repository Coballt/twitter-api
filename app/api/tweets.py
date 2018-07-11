# app/api/tweets.py
from flask import Blueprint, jsonify, request
from app.db import tweet_repository
from app.models import Tweet
import json

api = Blueprint('tweets', __name__)

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
    return '', 204

@api.route('/tweets/<int:id>', methods=['DELETE'])
def delete_tweet(id):
    res = tweet_repository.delete(id)
    if res is False:
        return jsonify({'error' : 'Tweet not found'}), 404
    return '', 204
