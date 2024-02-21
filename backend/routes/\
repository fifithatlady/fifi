#!/usr/bin/python3

from flask import Blueprint, jsonify

property_routes = Blueprint('property_routes', __name__)

@property_routes.route("/properties", methods=["GET"])
def get_properties():
    return jsonify({'message': 'Get properties route'})

@property_routes.route("/properties/<int:property_id>", methods=["GET"])
def get_property(property_id):
    return jsonify({'message': f'Get property with ID {property_id}'})

@property_routes.route("/properties", methods=["POST"])
def create_property():
    return jsonify({'message': 'Create property route'})

@property_routes.route("/properties/<int:property_id>", methods=["PUT"])
def update_property(property_id):
    return jsonify({'message': f'Update property with ID {property_id}'})

@property_routes.route("/properties/<int:property_id>", methods=["DELETE"])
def delete_property(property_id):
    return jsonify({'message': f'Delete property with ID {property_id}'})

property_routes_blueprint = property_routes
