#!/usr/bin/env python3
from flask import jsonify
from flask_bcrypt import Bcrypt
from .models import User, NannyJob
from .utils.error import errorHandler

bcrypt = Bcrypt()

def test():
    return jsonify({
        'message': 'API route is working!'
    })

def update_user(user_id, data):
    if not data['password']:
        data.pop('password', None)
    else:
        data['password'] = bcrypt.generate_password_hash(data['password']).decode('utf-8')

    updated_user = User.query.get(user_id)
    if not updated_user:
        return jsonify({'error': 'User not found!'}), 404

    updated_user.update(data)
    return jsonify(updated_user), 200

def delete_user(user_id):
    deleted_user = User.query.get(user_id)
    if not deleted_user:
        return jsonify({'error': 'User not found!'}), 404

    deleted_user.delete()
    return jsonify('User has been deleted!'), 200

def get_user_nanny_jobs(user_id):
    if user_id != current_user.id:
        return jsonify({'error': 'You can only view your own nanny job listings!'}), 401

    try:
        nanny_jobs = NannyJob.query.filter_by(user_id=user_id).all()
        return jsonify(nanny_jobs), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def get_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found!'}), 404

    user_data = {key: value for key, value in user.__dict__.items() 
            if key != '_sa_instance_state' and key != 'password'}
    return jsonify(user_data), 200

