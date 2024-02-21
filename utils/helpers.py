#!/usr/bin/python3

import uuid
import re
import hashlib

def generate_unique_id():
    """Generate a unique ID."""
    return str(uuid.uuid4())

def validate_email(email):
    """Validate an email address."""
    # Regular expression for email validation
    pattern = re.compile(r'^[\w\.-]+@[\w\.-]+\.\w+$')
    return bool(re.match(pattern, email))

def hash_password(password):
    """Hash a password."""
    # Hash the password using SHA-256 algorithm
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password

def verify_password(password, hashed_password):
    """Verify a password."""
    # Hash the input password and compare it with the hashed password
    return hash_password(password) == hashed_password
