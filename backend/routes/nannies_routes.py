#!/usr/bin/python3

from flask import Blueprint, request, jsonify
from .middleware import token_required

nanny_bp = Blueprint('nanny', __name__)

# Dummy nanny data (replace with database integration)
nannies = [
    {'id': 1, 'name': 'Nanny 1', 'hourly_rate': 15},
    {'id': 2, 'name': 'Nanny 2', 'hourly_rate': 20},
    {'id': 3, 'name': 'Nanny 3', 'hourly_rate': 18}
]

# Route handler for creating a new nanny
@nanny_bp.route('/api/nannies', methods=['POST'])
@token_required
def create_nanny():
    data = request.json
    nannies.append(data)
    return jsonify({'message': 'Nanny created successfully'}), 201

# Route handler for getting all nannies
@nanny_bp.route('/api/nannies', methods=['GET'])
def get_nannies():
    return jsonify(nannies)

# Route handler for getting a specific nanny by ID
@nanny_bp.route('/api/nannies/<int:nanny_id>', methods=['GET'])
def get_nanny(nanny_id):
    nanny = next((n for n in nannies if n['id'] == nanny_id), None)
    if nanny:
        return jsonify(nanny)
    else:
        return jsonify({'error': 'Nanny not found'}), 404

# Route handler for updating an existing nanny
@nanny_bp.route('/api/nannies/<int:nanny_id>', methods=['PUT'])
@token_required
def update_nanny(nanny_id):
    data = request.json
    nanny = next((n for n in nannies if n['id'] == nanny_id), None)
    if nanny:
        nanny.update(data)
        return jsonify({'message': 'Nanny updated successfully'})
    else:
        return jsonify({'error': 'Nanny not found'}), 404

# Route handler for deleting a nanny
@nanny_bp.route('/api/nannies/<int:nanny_id>', methods=['DELETE'])
@token_required
def delete_nanny(nanny_id):
    global nannies
    nannies = [n for n in nannies if n['id'] != nanny_id]
    return jsonify({'message': 'Nanny deleted successfully'})

