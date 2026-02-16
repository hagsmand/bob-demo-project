"""
Configuration settings for the Flask application.
Equivalent to application.properties from the Spring Boot application.
"""

import os


class Config:
    """Base configuration class."""
    
    # Server Configuration (equivalent to server.port=8080)
    PORT = int(os.environ.get('PORT', 8080))
    HOST = os.environ.get('HOST', '0.0.0.0')
    
    # Application Name (equivalent to spring.application.name=demo-app)
    APP_NAME = 'demo-app'
    
    # JSON Data File Location (equivalent to app.data.file=classpath:data/users.json)
    DATA_FILE = os.path.join(os.path.dirname(__file__), 'data', 'users.json')
    
    # Flask Configuration
    DEBUG = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    JSON_SORT_KEYS = False  # Preserve JSON key order
    
    # CORS Configuration (if needed)
    CORS_ENABLED = os.environ.get('CORS_ENABLED', 'True').lower() == 'true'


class DevelopmentConfig(Config):
    """Development configuration."""
    DEBUG = True


class ProductionConfig(Config):
    """Production configuration."""
    DEBUG = False


# Configuration dictionary
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}


def get_config(env=None):
    """Get configuration based on environment."""
    if env is None:
        env = os.environ.get('FLASK_ENV', 'development')
    return config.get(env, config['default'])


# Made with Bob