"""
Flask application - Python equivalent of Spring Boot demo application.
Provides REST API endpoint to retrieve user data from JSON file.
"""

import json
import os
from flask import Flask, jsonify
from config import config
from models import User


def create_app(config_name='default'):
    """
    Application factory pattern for creating Flask app.
    
    Args:
        config_name (str): Configuration name (development, production, testing)
        
    Returns:
        Flask: Configured Flask application instance
    """
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    
    @app.route('/api/users', methods=['GET'])
    def get_users():
        """
        GET endpoint to retrieve all users from JSON file.
        Equivalent to Spring Boot's UserController.getUsers()
        
        Returns:
            JSON response with list of users or error message
        """
        try:
            data_file = app.config['DATA_FILE']
            
            # Check if file exists
            if not os.path.exists(data_file):
                return jsonify({'error': 'Data file not found'}), 404
            
            # Read and parse JSON file
            with open(data_file, 'r', encoding='utf-8') as f:
                users_data = json.load(f)
            
            # Convert to User objects and back to dict for consistent structure
            users = [User.from_dict(user_data).to_dict() for user_data in users_data]
            
            return jsonify(users), 200
            
        except json.JSONDecodeError as e:
            return jsonify({'error': f'Invalid JSON format: {str(e)}'}), 500
        except Exception as e:
            return jsonify({'error': f'Internal server error: {str(e)}'}), 500
    
    @app.route('/', methods=['GET'])
    def index():
        """Root endpoint with API information."""
        return jsonify({
            'name': app.config['APP_NAME'],
            'version': '1.0.0',
            'description': 'Flask REST API - Migrated from Spring Boot',
            'endpoints': {
                '/api/users': 'GET - Retrieve all users'
            }
        }), 200
    
    @app.route('/health', methods=['GET'])
    def health():
        """Health check endpoint."""
        return jsonify({'status': 'healthy'}), 200
    
    return app


if __name__ == '__main__':
    # Get environment (default to development)
    env = os.getenv('FLASK_ENV', 'development')
    
    # Create app with specified environment
    app = create_app(env)
    
    # Run the application
    print(f"Starting Flask application in {env} mode...")
    print(f"Server running on http://{app.config['HOST']}:{app.config['PORT']}")
    print(f"API endpoint: http://localhost:{app.config['PORT']}/api/users")
    
    app.run(
        host=app.config['HOST'],
        port=app.config['PORT'],
        debug=app.config['DEBUG']
    )


# Made with Bob