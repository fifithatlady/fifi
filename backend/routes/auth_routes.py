from flask import Blueprint, request, jsonify, current_app
import jwt
from functools import wraps

auth_bp = Blueprint('auth', __name__)

# Secret key for JWT encoding/decoding
SECRET_KEY = 'your_secret_key'

# Dummy user data (replace with database integration)
users = {
    'username': 'password'
}

# Route handler for user login
@auth_bp.route('/api/login', methods=['POST'])
def login():
    auth = request.authorization
    if auth and auth.username in users and users[auth.username] == auth.password:
        token = jwt.encode({'user': auth.username}, current_app.config['SECRET_KEY'])
        return jsonify({'token': token.decode('UTF-8')})
    return jsonify({'error': 'Invalid credentials'}), 401

# Decorator for token verification
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token')
        if not token:
            return jsonify({'error': 'Token is missing'}), 401
        try:
            data = jwt.decode(token, current_app.config['SECRET_KEY'])
        except:
            return jsonify({'error': 'Token is invalid'}), 401
        return f(*args, **kwargs)
    return decorated

# Example protected route that requires authentication
@auth_bp.route('/api/protected')
@token_required
def protected():
    return jsonify({'message': 'This is a protected endpoint'})

