# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods
from datetime import datetime
from app import db

class Tweet(db.Model):
    __tablename__ = "tweet"
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String())
    created_at = db.Column(db.DateTime(), default=datetime.now())

    def __repr__(self):
        return '<id {}>'.format(self.id)
