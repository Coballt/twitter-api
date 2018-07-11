from unittest import TestCase
from app.repositories import TweetRepository
from app.models import Tweet

class TestRepository(TestCase):
    tweet = Tweet("Awesome tweet")
    def test_instance_variables(self):
        repo = TweetRepository()
        self.assertEqual(repo.tweets, [])

    def test_add_tweet(self):
        repo = TweetRepository()
        repo.add(self.tweet)
        self.assertEqual(repo.tweets, [self.tweet])
        self.assertEqual(repo.max_id, 2)
        self.assertEqual(self.tweet.id, 1)

    def test_get_tweet(self):
        repo = TweetRepository()
        repo.add(self.tweet)
        tweet = repo.get(1)
        self.assertEqual(tweet, self.tweet)

    def test_get_tweet_not_found(self):
        repo = TweetRepository()
        tweet = repo.get(1)
        self.assertEqual(tweet, None)
