#!/usr/bin/env python3

from flask import Blueprint, jsonify, request
from backend.controllers.nanny_controller import (delete_nanny, test, update_nanny, 
                                                  get_nanny_listings, get_nanny,
                                                  create_nanny, reset_password)
from utils.verify_user import verify_token

nanny_routes = Blueprint('nanny_routes', __name__)

@nanny_routes.route('/test', methods=['GET'])
def test_route():
    return test()

@nanny_routes.route('/create', methods=['POST'])
def create():
    data = request.get_json()
    return create_nanny(data)

@nanny_routes.route('/update/<int:id>', methods=['POST'])
@verify_token
def update(id):
    data = request.get_json()
    return update_nanny(id, data)

@nanny_routes.route('/delete/<int:id>', methods=['DELETE'])
@verify_token
def delete(id):
    return delete_nanny(id)

@nanny_routes.route('/listings/<int:id>', methods=['GET'])
@verify_token
def listings(id):
    return get_nanny_listings(id)

@nanny_routes.route('/<int:id>', methods=['GET'])
@verify_token
def get(id):
    return get_nanny(id)

@nanny_routes.route('/reset-password/<int:id>', methods=['POST'])
@verify_token
def reset_password_route(id):
    data = request.get_json()
    return reset_password(id, data)

# Export the Blueprint
nanny_routes_blueprint = nanny_routes

