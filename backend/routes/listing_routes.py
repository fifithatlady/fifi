#!/usr/bin/env python3

from flask import Blueprint, request, jsonify
from backend.controllers.nanny_controller import create_nanny, delete_nanny, update_nanny, get_nanny, get_nannies
from utils.verify_user import verify_token

nanny_routes = Blueprint('nanny_routes', __name__)

@nanny_routes.route('/create', methods=['POST'])
@verify_token
def create():
    # Implement create nanny logic here
    return jsonify({'message': 'Create nanny route'})

@nanny_routes.route('/delete/<int:id>', methods=['DELETE'])
@verify_token
def delete(id):
    # Implement delete nanny logic here
    return jsonify({'message': f'Delete nanny {id} route'})

@nanny_routes.route('/update/<int:id>', methods=['POST'])
@verify_token
def update(id):
    # Implement update nanny logic here
    return jsonify({'message': f'Update nanny {id} route'})

@nanny_routes.route('/get/<int:id>', methods=['GET'])
def get(id):
    # Implement get nanny by ID logic here
    return jsonify({'message': f'Get nanny {id} route'})

@nanny_routes.route('/get', methods=['GET'])
def get_all():
    # Implement get all nannies logic here
    return jsonify({'message': 'Get all nannies route'})

# Add more routes as needed

# Export the Blueprint
nanny_routes_blueprint = nanny_routes

