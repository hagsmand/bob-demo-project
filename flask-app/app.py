from flask import Flask, jsonify
import json
import os

app = Flask(__name__)

# Configuration
app.config['PORT'] = 8080
app.config['DATA_FILE'] = os.path.join(os.path.dirname(__file__), 'data', 'users.json')

def load_users():
    """Load users from JSON file"""
    try:
        with open(app.config['DATA_FILE'], 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

@app.route('/api/users', methods=['GET'])
def get_users():
    """Get all users endpoint"""
    try:
        users = load_users()
        return jsonify(users), 200
    except Exception as e:
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({'status': 'healthy', 'service': 'demo-app'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=app.config['PORT'], debug=True)

# Made with Bob