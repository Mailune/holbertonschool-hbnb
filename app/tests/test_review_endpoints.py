import unittest
import json
from app import create_app

class ReviewEndpointsTestCase(unittest.TestCase):
    """
    Test case for the review endpoints of the API.
    """

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_create_review(self):
        response = self.client.post('/api/api_reviews/', data=json.dumps({
            'user_id': 'user_1',
            'place_id': 'place_1',
            'rating': 5,
            'text': 'Great place!'
        }), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIn('id', response.get_json())

    def test_get_review(self):
        response = self.client.post('/api/api_reviews/', data=json.dumps({
            'user_id': 'user_1',
            'place_id': 'place_1',
            'rating': 5,
            'text': 'Great place!'
        }), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        review_id = response.get_json()['id']
        response = self.client.get(f'/api/api_reviews/{review_id}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()['text'], 'Great place!')

    def test_update_review(self):
        response = self.client.post('/api/api_reviews/', data=json.dumps({
            'user_id': 'user_1',
            'place_id': 'place_1',
            'rating': 5,
            'text': 'Great place!'
        }), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        review_id = response.get_json()['id']
        response = self.client.put(f'/api/api_reviews/{review_id}', data=json.dumps({
            'user_id': 'user_1',
            'place_id': 'place_1',
            'rating': 4,
            'text': 'Updated review'
        }), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()['text'], 'Updated review')

    def test_delete_review(self):
        response = self.client.post('/api/api_reviews/', data=json.dumps({
            'user_id': 'user_1',
            'place_id': 'place_1',
            'rating': 5,
            'text': 'Great place!'
        }), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        review_id = response.get_json()['id']
        response = self.client.delete(f'/api/api_reviews/{review_id}')
        self.assertEqual(response.status_code, 204)

if __name__ == '__main__':
    unittest.main()