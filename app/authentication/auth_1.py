# from flask import Blueprint, request, jsonify
# from app.authentication.auth_model import User
# from app.extensions import db, jwt
# from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity

# auth_bp = Blueprint('auth', __name__)

# @auth_bp.route('/register', methods=['POST'])
# def register_user():
#     data = request.get_json()
#     if User.query.filter_by(username=data['username']).first():
#         return jsonify({"error": "User already exists"}), 400

#     new_user = User(username=data['username'], email=data['email'])
#     new_user.set_password(data['password'])
#     db.session.add(new_user)
#     db.session.commit()
#     return jsonify({"message": "User registered successfully"}), 201

# @auth_bp.route('/login', methods=['POST'])
# def login_user():
#     data = request.get_json()
#     user = User.query.filter_by(username=data['username']).first()
#     if user and user.check_password(data['password']):
#         access_token = create_access_token(identity=user.username)
#         refresh_token = create_refresh_token(identity=user.username)
#         return jsonify({"access_token": access_token, "refresh_token": refresh_token}), 200
#     return jsonify({"error": "Invalid username or password"}), 401
