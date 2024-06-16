import unittest
import json
from app import create_app
from sqlalchemy.exc import IntegrityError

class AmenityEndpointsTestCase(unittest.TestCase):
    """
    Test case for the Amenity endpoints.
    """
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_create_amenity(self):
        response = self.client.post('/api/api_amenities/', data=json.dumps({
            'name': 'WiFi'
        }), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIn('id', response.get_json())

    def test_get_amenity(self):
        response = self.client.post('/api/api_amenities/', data=json.dumps({
            'name': 'WiFi'
        }), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        amenity_id = response.get_json()['id']
        response = self.client.get(f'/api/api_amenities/{amenity_id}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()['name'], 'WiFi')

    def test_update_amenity(self):
        response = self.client.post('/api/api_amenities/', data=json.dumps({
            'name': 'WiFi'
        }), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        amenity_id = response.get_json()['id']
        response = self.client.put(f'/api/api_amenities/{amenity_id}', data=json.dumps({
            'name': 'Updated Amenity'
        }), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()['name'], 'Updated Amenity')

    def test_delete_amenity(self):
        response = self.client.post('/api/api_amenities/', data=json.dumps({
            'name': 'WiFi'
        }), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        amenity_id = response.get_json()['id']
        response = self.client.delete(f'/api/api_amenities/{amenity_id}')
        self.assertEqual(response.status_code, 204)
        
        # Verify that the amenity has been deleted
        get_response = self.client.get(f'/api/api_amenities/{amenity_id}')
        self.assertEqual(get_response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
