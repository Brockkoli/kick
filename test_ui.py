import unittest
from app import app

class FlaskAppTests(unittest.TestCase):

    def setUp(self):
        # Set up the test client
        app.testing = True
        self.client = app.test_client()

    def test_home_page(self):
        # Test the home page response
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Search Page', response.data)

    def test_valid_search(self):
        # Test a valid search
        response = self.client.post('/', data={'search': 'Flask'})
        self.assertEqual(response.status_code, 302)
        self.assertIn('/search', response.headers['Location'])

    def test_invalid_search(self):
        # Test an invalid search (XSS attempt)
        response = self.client.post('/', data={'search': '<script>'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Invalid input.', response.data)

    def test_search_result_page(self):
        # Test the search result page
        response = self.client.get('/search?term=Flask')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Search Term: Flask', response.data)

if __name__ == "__main__":
    unittest.main()
