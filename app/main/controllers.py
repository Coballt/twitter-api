# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods
from flask import Blueprint

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return "Hello from a Blueprint!"
