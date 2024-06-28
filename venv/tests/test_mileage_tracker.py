# test_mileage_tracker.py

import pytest
from mileage_tracker import load_data, add_run, add_new_shoe, delete_shoe

# Test load_data function
def test_load_data():
    data = load_data()
    assert isinstance(data, dict)
    # Add more specific tests based on expected data structure or initial conditions

# Test add_run function
def test_add_run():
    data = {}
    shoe_name = "Nike Air Zoom Pegasus"
    distance = 10.5
    add_run(data, shoe_name, distance)
    assert data.get(shoe_name) == distance
    # Add more assertions to test different scenarios

# Test add_new_shoe function
def test_add_new_shoe():
    data = {}
    shoe_name = "Adidas Ultraboost"
    add_new_shoe(data, shoe_name)
    assert shoe_name in data
    assert data.get(shoe_name) == 0
    # Add more assertions to test edge cases or other scenarios

# Test delete_shoe function
def test_delete_shoe():
    data = {"Nike Air Zoom Pegasus": 10.5, "Adidas Ultraboost": 0}
    shoe_name = "Adidas Ultraboost"
    delete_shoe(data, shoe_name)
    assert shoe_name not in data
    # Add more assertions to test other aspects of deleting shoes

# You can add more test functions as needed for other functions in your project
