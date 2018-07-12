from app import ma
from marshmallow import fields
from .models import Tweet, User

class UserSchema(ma.Schema):
    class Meta:
        model = User
        fields = ('id', 'username', 'token') # These are the fields we want in the JSON!

user_schema = UserSchema()
users_schema = UserSchema(many=True)

class TweetSchema(ma.Schema):
    class Meta:
        model = Tweet
        fields = ('id', 'text', 'created_at', 'user_id') # These are the fields we want in the JSON!

tweet_schema = TweetSchema()
tweets_schema = TweetSchema(many=True)
