#!/usr/bin/env python3

from flask import jsonify
from .models import NannyJob

def create_nanny_job(data):
    try:
        nanny_job = NannyJob.create(**data)
        return jsonify(nanny_job), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

def delete_nanny_job(nanny_job_id):
    try:
        nanny_job = NannyJob.get_by_id(nanny_job_id)
        nanny_job.delete()
        return jsonify({'message': 'Nanny job deleted successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 404

def update_nanny_job(nanny_job_id, data):
    try:
        nanny_job = NannyJob.get_by_id(nanny_job_id)
        nanny_job.update(**data)
        return jsonify(nanny_job), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 404

def get_nanny_job(nanny_job_id):
    try:
        nanny_job = NannyJob.get_by_id(nanny_job_id)
        return jsonify(nanny_job), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 404

def get_nanny_jobs(filters):
    try:
        nanny_jobs = NannyJob.query(filters)
        return jsonify(nanny_jobs), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

