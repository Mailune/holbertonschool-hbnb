import requests

BASE_URL = "http://localhost:5001/users"

def test_create_user():
    """
    Test case for creating a user.

    Sends a POST request to the BASE_URL with user data and checks if the response
    status code is 201 (Created) and if the response contains the 'id' key in the JSON.
    """
    # Given
    user_data = {
        'email': 'test@example.com',
        'password': 'password',
        'first_name': 'Test',
        'last_name': 'User'
    }

    # When
    response = requests.post(BASE_URL, json=user_data)

    # Then
    assert response.status_code == 201, f"Expected status code 201, but got {response.status_code}"
    assert 'id' in response.json(), "Expected 'id' in response JSON, but it was not found"

def test_get_users():
    """
    Test case for retrieving a list of users.

    Sends a GET request to the BASE_URL and checks if the response
    status code is 200 (OK) and if the response JSON is a list.
    """
    # When
    response = requests.get(BASE_URL)

    # Then
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    assert isinstance(response.json(), list), "Expected response JSON to be a list, but it was not"

if __name__ == "__main__":
    test_create_user()
    test_get_users()
