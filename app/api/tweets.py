# app/api/tweets.py
from flask import Blueprint, jsonify
from app.db import tweet_repository

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
