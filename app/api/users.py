# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods
import json
from flask import Blueprint, jsonify, request
from app import db
from app.models import User
from app.schemas import user_schema, users_schema
from datetime import datetime
import secrets

api = Blueprint('user', __name__)

@api.route('/users', methods=['GET'])
def get_all_users():
    list_users = db.session.query(User).all()
    return users_schema.jsonify(list_users), 200

@api.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    user = db.session.query(User).get(id)
    if user is not None :
        return user_schema.jsonify(user)
    return jsonify({"error": "User not found"}), 404

@api.route('/users', methods=['POST'])
def post_user():
    try:
        payload = json.loads(request.data)
    except ValueError :
        return jsonify({"error" : "Bad payload received"}), 422
    if 'username' not in payload:
        return jsonify({"error" : "Bad payload received"}), 422
    user = User(username=payload['username'], token=secrets.token_hex(16))
    db.session.add(user)
    db.session.flush()
    db.session.commit()
    return user_schema.jsonify(user), 201

@api.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = db.session.query(User).get(id)
    if user is not None :
        db.session.delete(user)
        db.session.flush()
        db.session.commit()
        return '', 204
    return jsonify({"error": "User not found"}), 404

@api.route('/users/<int:id>', methods=['PATCH'])
def change_user(id):
    try:
        payload = json.loads(request.data)
    except ValueError :
        return jsonify({"error" : "Bad payload received"}), 422
    if 'username' not in payload:
        return jsonify({"error" : "Bad payload received"}), 422
    user = db.session.query(User).get(id)
    if user is not None :
        user.username = payload['username']
        db.session.commit()
        return '', 204
    return jsonify({"error": "User not found"}), 404
