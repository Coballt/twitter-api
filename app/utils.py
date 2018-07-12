from app.models import User
from app import db

def validate_token(token):
    return db.session.query(User).filter_by(token=token).first()
