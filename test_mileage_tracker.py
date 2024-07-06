import pytest
import json
from mileage_tracker import load_data, save_data, add_run, add_new_shoe, delete_shoe

# Pytest fixture to load and set up test data
@pytest.fixture
def setup_data():
    # data for testing
    initial_data = {
        "Nike Pegasus": 500,  # Update this to reflect the correct initial mileage
        "Adidas Ultraboost": 500,
        "New Balance Fresh Foam": 700
    }
    # Save data to a temporary file and overwrite
    with open('test_shoe_database.json', 'w') as f:
        json.dump(initial_data, f)
    
    yield 'test_shoe_database.json'  # Provide values
    
    # remove everything after testing
    import os
    os.remove('test_shoe_database.json')



def test_load_data(setup_data):
    data = load_data()
    assert isinstance(data, dict)
    assert len(data) == 3
    assert "Nike Pegasus" in data
    assert data["Adidas Ultraboost"] == 500

def test_add_run(setup_data):
    data = load_data()
    shoe_name = "Nike Pegasus"
    distance = 200
    add_run(data, shoe_name, distance)
    assert data[shoe_name] == 500 + distance

def test_add_new_shoe(setup_data):
    data = load_data()
    shoe_name = "Brooks Ghost"
    add_new_shoe(data, shoe_name)
    assert shoe_name in data
    assert data[shoe_name] == 0

def test_delete_shoe(setup_data):
    data = load_data()
    shoe_name = "Adidas Ultraboost"
    delete_shoe(data, shoe_name)
    assert shoe_name not in data

def test_invalid_distance(setup_data):
    data = load_data()
    shoe_name = "Nike Pegasus"
    distance = "abc"  
    with pytest.raises(TypeError):
        add_run(data, shoe_name, distance)



if __name__ == "__main__":
    pytest.main()
