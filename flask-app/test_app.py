"""
Unit tests for Flask application.
Tests all endpoints and functionality.
"""

import unittest
import json
import os
from app import create_app
from models import User


class FlaskAppTestCase(unittest.TestCase):
    """Test cases for Flask application."""
    
    def setUp(self):
        """Set up test client and test data."""
        self.app = create_app('testing')
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
    
    def tearDown(self):
        """Clean up after tests."""
        self.app_context.pop()
    
    def test_app_exists(self):
        """Test that the app exists."""
        self.assertIsNotNone(self.app)
    
    def test_app_is_testing(self):
        """Test that the app is in testing mode."""
        self.assertTrue(self.app.config['TESTING'])
    
    def test_index_endpoint(self):
        """Test the root endpoint returns API information."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        
        data = json.loads(response.data)
        self.assertIn('name', data)
        self.assertIn('version', data)
        self.assertIn('description', data)
        self.assertIn('endpoints', data)
        self.assertEqual(data['name'], 'demo-app')
    
    def test_health_endpoint(self):
        """Test the health check endpoint."""
        response = self.client.get('/health')
        self.assertEqual(response.status_code, 200)
        
        data = json.loads(response.data)
        self.assertIn('status', data)
        self.assertEqual(data['status'], 'healthy')
    
    def test_get_users_success(self):
        """Test GET /api/users returns user list successfully."""
        response = self.client.get('/api/users')
        self.assertEqual(response.status_code, 200)
        
        data = json.loads(response.data)
        self.assertIsInstance(data, list)
        self.assertGreater(len(data), 0)
        
        # Verify first user structure
        first_user = data[0]
        self.assertIn('id', first_user)
        self.assertIn('name', first_user)
        self.assertIn('email', first_user)
        self.assertIn('age', first_user)
        self.assertIn('city', first_user)
    
    def test_get_users_data_integrity(self):
        """Test that user data matches expected values."""
        response = self.client.get('/api/users')
        data = json.loads(response.data)
        
        # Check specific user data
        john_doe = next((user for user in data if user['id'] == 1), None)
        self.assertIsNotNone(john_doe)
        self.assertEqual(john_doe['name'], 'John Doe')
        self.assertEqual(john_doe['email'], 'john.doe@example.com')
        self.assertEqual(john_doe['age'], 30)
        self.assertEqual(john_doe['city'], 'New York')
    
    def test_get_users_returns_json(self):
        """Test that /api/users returns JSON content type."""
        response = self.client.get('/api/users')
        self.assertEqual(response.content_type, 'application/json')
    
    def test_invalid_endpoint(self):
        """Test that invalid endpoints return 404."""
        response = self.client.get('/api/invalid')
        self.assertEqual(response.status_code, 404)
    
    def test_method_not_allowed(self):
        """Test that POST to GET-only endpoint returns 405."""
        response = self.client.post('/api/users')
        self.assertEqual(response.status_code, 405)


class UserModelTestCase(unittest.TestCase):
    """Test cases for User model."""
    
    def test_user_creation(self):
        """Test creating a User instance."""
        user = User(
            id=1,
            name='Test User',
            email='test@example.com',
            age=25,
            city='Test City'
        )
        
        self.assertEqual(user.id, 1)
        self.assertEqual(user.name, 'Test User')
        self.assertEqual(user.email, 'test@example.com')
        self.assertEqual(user.age, 25)
        self.assertEqual(user.city, 'Test City')
    
    def test_user_to_dict(self):
        """Test User.to_dict() method."""
        user = User(
            id=1,
            name='Test User',
            email='test@example.com',
            age=25,
            city='Test City'
        )
        
        user_dict = user.to_dict()
        
        self.assertIsInstance(user_dict, dict)
        self.assertEqual(user_dict['id'], 1)
        self.assertEqual(user_dict['name'], 'Test User')
        self.assertEqual(user_dict['email'], 'test@example.com')
        self.assertEqual(user_dict['age'], 25)
        self.assertEqual(user_dict['city'], 'Test City')
    
    def test_user_from_dict(self):
        """Test User.from_dict() class method."""
        user_data = {
            'id': 1,
            'name': 'Test User',
            'email': 'test@example.com',
            'age': 25,
            'city': 'Test City'
        }
        
        user = User.from_dict(user_data)
        
        self.assertIsInstance(user, User)
        self.assertEqual(user.id, 1)
        self.assertEqual(user.name, 'Test User')
        self.assertEqual(user.email, 'test@example.com')
        self.assertEqual(user.age, 25)
        self.assertEqual(user.city, 'Test City')
    
    def test_user_repr(self):
        """Test User.__repr__() method."""
        user = User(
            id=1,
            name='Test User',
            email='test@example.com',
            age=25,
            city='Test City'
        )
        
        repr_str = repr(user)
        self.assertIn('Test User', repr_str)
        self.assertIn('test@example.com', repr_str)
        self.assertIn('25', repr_str)
        self.assertIn('Test City', repr_str)
    
    def test_user_default_values(self):
        """Test User creation with default values."""
        user = User()
        
        self.assertIsNone(user.id)
        self.assertIsNone(user.name)
        self.assertIsNone(user.email)
        self.assertIsNone(user.age)
        self.assertIsNone(user.city)


class ConfigTestCase(unittest.TestCase):
    """Test cases for application configuration."""
    
    def test_development_config(self):
        """Test development configuration."""
        app = create_app('development')
        self.assertTrue(app.config['DEBUG'])
        self.assertFalse(app.config['TESTING'])
    
    def test_testing_config(self):
        """Test testing configuration."""
        app = create_app('testing')
        self.assertTrue(app.config['TESTING'])
        self.assertTrue(app.config['DEBUG'])
    
    def test_production_config(self):
        """Test production configuration."""
        app = create_app('production')
        self.assertFalse(app.config['DEBUG'])
        self.assertFalse(app.config['TESTING'])
    
    def test_default_config(self):
        """Test default configuration."""
        app = create_app()
        self.assertTrue(app.config['DEBUG'])  # Default is development


def run_tests():
    """Run all tests and display results."""
    # Create test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add test cases
    suite.addTests(loader.loadTestsFromTestCase(FlaskAppTestCase))
    suite.addTests(loader.loadTestsFromTestCase(UserModelTestCase))
    suite.addTests(loader.loadTestsFromTestCase(ConfigTestCase))
    
    # Run tests with verbose output
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Return exit code based on results
    return 0 if result.wasSuccessful() else 1


if __name__ == '__main__':
    exit_code = run_tests()
    exit(exit_code)


# Made with Bob