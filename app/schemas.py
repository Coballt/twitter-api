from app import ma
from .models import Tweet, User

class TweetSchema(ma.Schema):
    class Meta:
        model = Tweet
        fields = ('id', 'text', 'created_at') # These are the fields we want in the JSON!

tweet_schema = TweetSchema()
tweets_schema = TweetSchema(many=True)

class UserSchema(ma.Schema):
    class Meta:
        model = User
        fields = ('id', 'name', 'token') # These are the fields we want in the JSON!

user_schema = UserSchema()
users_schema = UserSchema(many=True)
