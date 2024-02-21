#!/usr/bin/python3

import pytest
from backend.models import Nanny

# Test Nanny Model
def test_create_nanny():
    # Test creating a nanny job listing
    nanny = Nanny(title='Nanny Job', description='Looking for a nanny', salary=1000)
    assert nanny.title == 'Nanny Job'
    assert nanny.description == 'Looking for a nanny'
    assert nanny.salary == 1000

def test_update_nanny():
    # Test updating a nanny job listing
    nanny = Nanny(title='Nanny Job', description='Looking for a nanny', salary=1000)
    nanny.title = 'Updated Nanny Job'
    nanny.description = 'Looking for an experienced nanny'
    nanny.salary = 1500
    assert nanny.title == 'Updated Nanny Job'
    assert nanny.description == 'Looking for an experienced nanny'
    assert nanny.salary == 1500

def test_delete_nanny():
    # Test deleting a nanny job listing
    nanny = Nanny(title='Nanny Job', description='Looking for a nanny', salary=1000)
    del nanny
    with pytest.raises(NameError):
        nanny

def test_nanny_representation():
    # Test nanny representation
    nanny = Nanny(title='Nanny Job', description='Looking for a nanny', salary=1000)
    assert str(nanny) == '<Nanny Nanny Job>'

