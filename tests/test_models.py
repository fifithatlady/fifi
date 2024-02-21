#!/usr/bin/python3

import pytest
from backend.models.models import (
    City, County, Province, State, Continent, Suburb, Review, Preference
)

# Test City Model
def test_city_creation():
    city = City(name="Johannesburg", state_id="12345")
    assert city.name == "Johannesburg"
    assert city.state_id == "12345"

def test_city_creation_invalid_data():
    with pytest.raises(ValueError):
        City(name=None, state_id="12345")

def test_city_name_max_length():
    max_length = 255
    long_name = "a" * max_length
    city = City(name=long_name, state_id="12345")
    assert len(city.name) == max_length

def test_city_name_type():
    with pytest.raises(TypeError):
        City(name=123, state_id="12345")

def test_state_id_type():
    with pytest.raises(TypeError):
        City(name="Johannesburg", state_id=None)

# Test Province Model
def test_province_creation():
    province = Province(name="Gauteng", country_id="54321")
    assert province.name == "Gauteng"
    assert province.country_id == "54321"

def test_province_creation_invalid_data():
    with pytest.raises(ValueError):
        Province(name=None, country_id="12345")

def test_province_name_max_length():
    max_length = 255
    long_name = "a" * max_length
    province = Province(name=long_name, country_id="12345")
    assert len(province.name) == max_length

def test_province_name_type():
    with pytest.raises(TypeError):
        Province(name=123, country_id="12345")

def test_country_id_type():
    with pytest.raises(TypeError):
        Province(name="South Africa", country_id=None)

# Test State Model
def test_state_creation():
    state = State(name="Mpumalanga", province_id="67890")
    assert state.name == "Mpumalanga"
    assert state.province_id == "67890"

def test_state_creation_invalid_data():
    with pytest.raises(ValueError):
        State(name=None, province_id="12345")

def test_state_name_max_length():
    max_length = 255
    long_name = "a" * max_length
    state = State(name=long_name, province_id="12345")
    assert len(state.name) == max_length

def test_state_name_type():
    with pytest.raises(TypeError):
        State(name=123, province_id="12345")

def test_province_id_type():
    with pytest.raises(TypeError):
        State(name="Mpumalanga", province_id=None)

# Test Continent Model
def test_continent_creation():
    continent = Continent(name="Southern Africa")
    assert continent.name == "Southern Africa"

def test_continent_creation_invalid_data():
    with pytest.raises(ValueError):
        Continent(name=None)

def test_continent_name_max_length():
    max_length = 255
    long_name = "a" * max_length
    continent = Continent(name=long_name)
    assert len(continent.name) == max_length

def test_continent_name_type():
    with pytest.raises(TypeError):
        Continent(name=123)

# Test Suburb Model
def test_suburb_creation():
    suburb = Suburb(name="Soweto", city_id="12345")
    assert suburb.name == "Soweto"
    assert suburb.city_id == "12345"

def test_suburb_creation_invalid_data():
    with pytest.raises(ValueError):
        Suburb(name=None)

def test_suburb_name_max_length():
    max_length = 255
    long_name = "a" * max_length
    suburb = Suburb(name=long_name)
    assert len(suburb.name) == max_length

def test_suburb_name_type():
    with pytest.raises(TypeError):
        Suburb(name=123)

# Test Review Model
def test_review_creation():
    review = Review(text="Great place to work as a nanny", place_id="12345", user_id="67890")
    assert review.text == "Great place to work as a nanny"
    assert review.place_id == "12345"
    assert review.user_id == "67890"

def test_review_creation_invalid_data():
    with pytest.raises(ValueError):
        Review(text=None, place_id="123456", user_id="54321")

def test_review_representation():
    review = Review(text="This is a test review", place_id="123456", user_id="54321")
    expected_str = f"[Review] ({review.id}) {{'text': 'This is a test review', 'place_id': '123456', 'user_id': '54321'}}"
    assert str(review) == expected_str

def test_review_save_method():
    review = Review(text="This is a test review", place_id="123456", user_id="54321")
    review.save()
    assert review.id is not None

# Test Preference Model
def test_preference_creation():
    preference = Preference(user_id="67890", min_salary=500, max_salary=2000, min_experience=1, city_id="12345")
    assert preference.user_id == "67890"
    assert preference.min_salary == 500
    assert preference.max_salary == 2000
    assert preference.min_experience == 1
    assert preference.city_id == "12345"

def test_preference_creation_invalid_data():
    with pytest.raises(ValueError):
        Preference(user="Test User", min_salary="1000.00", max_salary=2000.00, min_experience=2, city="Test City")

def test_preference_representation():
    preference = Preference(user="Test User", min_salary=1000.00, max_salary=2000.00, min_experience=2, city="Test City")
    expected_str = f"[Preference] ({preference.id}) {{'user': 'Test User', 'city': 'Test City'}}"
    assert str(preference) == expected_str

def test_preference_save_method():
    preference = Preference(user="Test User", min_salary=1000.00, max_salary=2000.00, min_experience=2, city="Test City")
    preference.save()
    assert preference.id is not None
# Test County Model
def test_county_creation():
    county = County(name="XYZ County", province_id="67890")
    assert county.name == "XYZ County"
    assert county.province_id == "67890"

def test_county_creation_invalid_data():
    with pytest.raises(ValueError):
        County(name=None, province_id="54321")

def test_county_name_max_length():
    max_length = 255
    long_name = "a" * max_length
    county = County(name=long_name, province_id="54321")
    assert len(county.name) == max_length

def test_county_name_type():
    with pytest.raises(TypeError):
        County(name=123, province_id="54321")

def test_province_id_type():
    with pytest.raises(TypeError):
        County(name="Los Angeles", province_id=None)

# Test Amenity Model
def test_amenity_creation():
    amenity = Amenity(name="WiFi")
    assert amenity.name == "WiFi"

def test_amenity_creation_invalid_data():
    with pytest.raises(ValueError):
        Amenity(name=None)

def test_amenity_representation():
    amenity = Amenity(name="Gym")
    expected_str = f"[Amenity] ({amenity.id}) {{'name': 'Gym'}}"
    assert str(amenity) == expected_str

def test_amenity_save_method():
    amenity = Amenity(name="Tennis Court")
    amenity.save()
    assert amenity.id is not None

