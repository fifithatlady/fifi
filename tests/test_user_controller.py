#!/usr/bin/python3

import pytest
from backend.controllers.nanny_controller import create_nanny, update_nanny, delete_nanny, get_nanny

# Test NannyController
def test_create_nanny():
    # Test creating a nanny job listing
    nanny_data = {'title': 'Nanny Job', 'description': 'Looking for a nanny', 'salary': 1000}
    nanny_id = create_nanny(nanny_data)
    assert nanny_id is not None

def test_update_nanny():
    # Test updating a nanny job listing
    nanny_data = {'title': 'Nanny Job', 'description': 'Looking for a nanny', 'salary': 1000}
    nanny_id = create_nanny(nanny_data)
    updated_nanny_data = {'title': 'Updated Nanny Job', 'description': 'Looking for an experienced nanny', 'salary': 1500}
    result = update_nanny(nanny_id, updated_nanny_data)
    assert result is True

def test_delete_nanny():
    # Test deleting a nanny job listing
    nanny_data = {'title': 'Nanny Job', 'description': 'Looking for a nanny', 'salary': 1000}
    nanny_id = create_nanny(nanny_data)
    result = delete_nanny(nanny_id)
    assert result is True

def test_get_nanny():
    # Test getting a nanny job listing
    nanny_data = {'title': 'Nanny Job', 'description': 'Looking for a nanny', 'salary': 1000}
    nanny_id = create_nanny(nanny_data)
    nanny = get_nanny(nanny_id)
    assert nanny['title'] == 'Nanny Job'
    assert nanny['description'] == 'Looking for a nanny'
    assert nanny['salary'] == 1000
# Additional Test Cases for NannyController

def test_create_invalid_nanny():
    # Test creating a nanny job listing with invalid data
    with pytest.raises(ValueError):
        invalid_nanny_data = {'description': 'Looking for a nanny', 'salary': 1000}
        create_nanny(invalid_nanny_data)

def test_update_invalid_nanny():
    # Test updating a nanny job listing with invalid data
    nanny_data = {'title': 'Nanny Job', 'description': 'Looking for a nanny', 'salary': 1000}
    nanny_id = create_nanny(nanny_data)
    with pytest.raises(ValueError):
        invalid_nanny_data = {'description': 'Looking for an experienced nanny', 'salary': 1500}
        update_nanny(nanny_id, invalid_nanny_data)

def test_get_invalid_nanny():
    # Test getting a non-existent nanny job listing
    non_existent_nanny_id = '1234567890'
    nanny = get_nanny(non_existent_nanny_id)
    assert nanny is None

def test_delete_invalid_nanny():
    # Test deleting a non-existent nanny job listing
    non_existent_nanny_id = '1234567890'
    result = delete_nanny(non_existent_nanny_id)
    assert result is False

