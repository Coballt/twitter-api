# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods
from datetime import datetime
from app import db

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String())
    token = db.Column(db.String())
    tweets = db.relationship("Tweet")

    def __repr__(self):
        return '<id {}>'.format(self.id)

class Tweet(db.Model):
    __tablename__ = "tweet"
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String())
    created_at = db.Column(db.DateTime(), default=datetime.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<id {}>'.format(self.id)

