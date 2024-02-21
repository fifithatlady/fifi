#!/usr/bin/python3

from flask import request, jsonify
from functools import wraps

def verify_token(func):
    """Decorator to verify authentication token."""
    @wraps(func)
    def decorated(*args, **kwargs):
        # Implement token verification logic here
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'error': 'Missing token'}), 401
        # Example token verification logic
        if token != 'valid_token':
            return jsonify({'error': 'Invalid token'}), 401
        return func(*args, **kwargs)
    return decorated
