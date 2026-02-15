"""
Configuration settings for Flask application.
"""

import os


class Config:
    """Base configuration class."""
    
    # Flask settings
    DEBUG = False
    TESTING = False
    
    # Application settings
    APP_NAME = 'demo-app'
    
    # Data file path
    DATA_FILE = os.path.join(os.path.dirname(__file__), 'data', 'users.json')
    
    # Server settings
    HOST = '0.0.0.0'
    PORT = 5000


class DevelopmentConfig(Config):
    """Development configuration."""
    DEBUG = True


class ProductionConfig(Config):
    """Production configuration."""
    DEBUG = False


class TestingConfig(Config):
    """Testing configuration."""
    TESTING = True
    DEBUG = True


# Configuration dictionary
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}


# Made with Bob