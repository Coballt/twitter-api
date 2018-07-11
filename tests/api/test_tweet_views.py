from flask_testing import TestCase
from app import create_app
from app.models import Tweet
from app.db import tweet_repository
import json

class TestTweetViews(TestCase):
    def create_app(self):
        app = create_app()
        app.config['TESTING'] = True
        return app

    def setUp(self):
        tweet_repository.tweets.clear()
        tweet_repository.max_id = 1 # Make sure each test starts with an empty database

    def test_tweet_show(self):
        first_tweet = Tweet("First tweet")
        tweet_repository.add(first_tweet)
        response = self.client.get("/api/v1/tweets/1")
        response_tweet = response.json
        self.assertEqual(response_tweet["id"], 1)
        self.assertEqual(response_tweet["text"], "First tweet")
        self.assertIsNotNone(response_tweet["created_at"])

    def test_post_tweet_works(self):
        payload = {'text' : "Another awesome tweet"}
        response = self.client.post("/api/v1/tweets", data=json.dumps(payload))
        response_tweet = response.json
        self.assertEqual(response.status_code, 204)
        self.assertEqual(response_tweet, None)
        self.assertEqual(tweet_repository.max_id, 2)
        self.assertEqual(len(tweet_repository.tweets), 1)

    def test_post_tweet_bad_payload(self):
        payload = {'none' : "Another awesome tweet"}
        response = self.client.post("/api/v1/tweets", data=json.dumps(payload))
        response_tweet = response.json
        self.assertEqual(response.status_code, 422)
        self.assertEqual(response_tweet['error'], "Bad payload received")
        self.assertEqual(tweet_repository.max_id, 1)
        self.assertEqual(len(tweet_repository.tweets), 0)

    def test_delete_tweet_works(self):
        first_tweet = Tweet("First tweet")
        tweet_repository.add(first_tweet)
        response = self.client.delete("/api/v1/tweets/1")
        response_tweet = response.json
        self.assertEqual(response.status_code, 204)
        self.assertEqual(response_tweet, None)
        self.assertEqual(tweet_repository.max_id, 2)
        self.assertEqual(len(tweet_repository.tweets), 0)

    def test_delete_tweet_not_found(self):
        response = self.client.delete("/api/v1/tweets/1")
        response_tweet = response.json
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response_tweet['error'], 'Tweet not found')
