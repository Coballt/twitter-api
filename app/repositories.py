# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods
class TweetRepository:
    def __init__(self):
        self.tweets = []
        self.max_id = 1

    def add(self, tweet):
        self.tweets.append(tweet)
        tweet.id = self.max_id
        self.max_id += 1

    def get(self, id):
        for tweet in self.tweets:
            if tweet.id == id:
                return tweet
        return None

    def get_all(self):
        return self.tweets

    def delete(self, id):
        for tweet in self.tweets:
            if tweet.id == id:
                del self.tweets[self.tweets.index(tweet)]
                return True
        return False
