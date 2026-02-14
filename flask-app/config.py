import os

class Config:
    """Application configuration"""
    
    # Server Configuration
    PORT = 8080
    HOST = '0.0.0.0'
    
    # Application Name
    APP_NAME = 'demo-app'
    
    # JSON Data File Location
    DATA_FILE = os.path.join(os.path.dirname(__file__), 'data', 'users.json')
    
    # Debug mode
    DEBUG = True

# Made with Bob