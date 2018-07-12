# pylint: disable=missing-docstring
try:
    from dotenv import load_dotenv
    load_dotenv()
except:
    pass
from app.config import Config
from flask import Flask # This line already exists

from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
db = SQLAlchemy()
ma = Marshmallow()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    app.db  = db
    ma.init_app(app)
    app.ma = ma
    # Remove the previous code using `@app` and replace it with:
    from .main.controllers import main
    app.register_blueprint(main)
    from .api.tweets import api as tweet_api
    app.register_blueprint(tweet_api, url_prefix="/api/v1")

    return app
