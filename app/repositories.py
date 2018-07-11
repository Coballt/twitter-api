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
