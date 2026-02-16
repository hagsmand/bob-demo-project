"""
Flask application - Migration from Spring Boot Java to Python Flask.
This application provides a REST API to retrieve user data from a JSON file.

Equivalent to:
- DemoApplication.java (Spring Boot main class)
- UserController.java (REST controller)
"""

import json
import os
from flask import Flask, jsonify, Response
from flask_cors import CORS
from config import get_config
from models.user import User


def create_app(config_name=None):
    """
    Application factory pattern for creating Flask app.
    
    Args:
        config_name: Configuration environment name (development/production)
        
    Returns:
        Flask application instance
    """
    app = Flask(__name__)
    
    # Load configuration
    config = get_config(config_name)
    app.config.from_object(config)
    
    # Enable CORS if configured
    if app.config.get('CORS_ENABLED', True):
        CORS(app)
    
    # Register routes
    register_routes(app)
    
    return app


def register_routes(app: Flask):
    """
    Register all application routes.
    Equivalent to @RestController and @RequestMapping in Spring Boot.
    """
    
    @app.route('/api/users', methods=['GET'])
    def get_users():
        """
        Get all users from JSON file.
        
        Equivalent to UserController.getUsers() in Spring Boot:
        - Reads data from JSON file
        - Returns list of users as JSON response
        - Handles errors with 500 status code
        
        Returns:
            JSON response with list of users or error message
        """
        try:
            # Get data file path from configuration
            data_file_path = app.config['DATA_FILE']
            
            # Check if file exists
            if not os.path.exists(data_file_path):
                return jsonify({
                    'error': 'Data file not found',
                    'path': data_file_path
                }), 404
            
            # Read and parse JSON file
            with open(data_file_path, 'r', encoding='utf-8') as file:
                users_data = json.load(file)
            
            # Convert to User objects (optional, for validation)
            users = [User.from_dict(user_data) for user_data in users_data]
            
            # Convert back to dictionaries for JSON response
            users_list = [user.to_dict() for user in users]
            
            # Return JSON response with 200 OK status
            return jsonify(users_list), 200
            
        except json.JSONDecodeError as e:
            # Handle JSON parsing errors
            return jsonify({
                'error': 'Invalid JSON format in data file',
                'details': str(e)
            }), 500
            
        except Exception as e:
            # Handle any other errors (equivalent to catch IOException in Java)
            return jsonify({
                'error': 'Internal server error',
                'details': str(e)
            }), 500
    
    @app.route('/health', methods=['GET'])
    def health_check():
        """Health check endpoint."""
        return jsonify({
            'status': 'healthy',
            'app': app.config.get('APP_NAME', 'demo-app')
        }), 200
    
    @app.route('/', methods=['GET'])
    def index():
        """Root endpoint with API information."""
        return jsonify({
            'message': 'Flask Demo API',
            'version': '1.0.0',
            'endpoints': {
                'users': '/api/users',
                'health': '/health'
            }
        }), 200


def main():
    """
    Main entry point for the application.
    Equivalent to SpringApplication.run() in Spring Boot.
    """
    # Create Flask application
    app = create_app()
    
    # Get configuration
    port = app.config.get('PORT', 8080)
    host = app.config.get('HOST', '0.0.0.0')
    debug = app.config.get('DEBUG', False)
    
    # Print startup information
    print(f"Starting {app.config.get('APP_NAME', 'Flask App')}...")
    print(f"Server running on http://{host}:{port}")
    print(f"API endpoint: http://{host}:{port}/api/users")
    print(f"Debug mode: {debug}")
    
    # Run the application
    app.run(host=host, port=port, debug=debug)


if __name__ == '__main__':
    main()


# Made with Bob