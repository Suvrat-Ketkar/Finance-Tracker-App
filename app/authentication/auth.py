from flask import Flask, Blueprint, render_template, request, session, jsonify, redirect, url_for
from flask_session import Session
# from werkzeug.security import generate_password_hash, check_password_hash
from app.extensions import db
from app.authentication.auth_model import User
from functools import wraps



auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/')
def display_home_page():
    return render_template('LoginPage.html')

@auth_bp.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()
    if User.query.filter_by(username=data['username']).first():
        return jsonify({"error": "User already exists"}), 400

    new_user = User(username=data['username'], email=data['email'])
    new_user.set_password(data['password'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User registered successfully"}), 201

@auth_bp.route('/login', methods=['POST'])
def login_user():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    if user and user.check_password(data['password']):
        session['user_id'] = user.id  # Store user ID in session
        session['username'] = user.username  # Optional
        return jsonify({"message": "Login successful"}), 200
    return jsonify({"error": "Invalid username or password"}), 401

@auth_bp.route('/logout', methods=['POST'])
def logout_user():
    session.clear()  # Clear session data
    return jsonify({"message": "Logged out successfully"}), 200

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:  # Check if user is logged in
            # Render the error page if the user is not logged in
            return render_template('ErrorPage.html'), 401
        return f(*args, **kwargs)
    return decorated_function



# @auth_bp.route('/protected', methods=['GET'])
# def protected_route():
#     if 'user_id' not in session:
#         return jsonify({"error": "Unauthorized"}), 401
#     return jsonify({"message": f"Hello, {session['username']}!"}), 200
