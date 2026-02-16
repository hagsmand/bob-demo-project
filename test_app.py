"""
Simple test script to verify Flask application functionality.
Tests the /api/users endpoint without starting the full server.
"""

import json
from app import create_app


def test_flask_app():
    """Test the Flask application endpoints."""
    
    # Create test app
    app = create_app('development')
    app.config['TESTING'] = True
    
    # Create test client
    client = app.test_client()
    
    print("Testing Flask Application...")
    print("-" * 50)
    
    # Test 1: Root endpoint
    print("\n1. Testing root endpoint (GET /)...")
    response = client.get('/')
    print(f"   Status Code: {response.status_code}")
    print(f"   Response: {response.get_json()}")
    assert response.status_code == 200, "Root endpoint failed"
    print("   ✅ Root endpoint working!")
    
    # Test 2: Health check endpoint
    print("\n2. Testing health check (GET /health)...")
    response = client.get('/health')
    print(f"   Status Code: {response.status_code}")
    print(f"   Response: {response.get_json()}")
    assert response.status_code == 200, "Health check failed"
    print("   ✅ Health check working!")
    
    # Test 3: Users endpoint
    print("\n3. Testing users endpoint (GET /api/users)...")
    response = client.get('/api/users')
    print(f"   Status Code: {response.status_code}")
    
    if response.status_code == 200:
        users = response.get_json()
        print(f"   Number of users: {len(users)}")
        print(f"   First user: {users[0] if users else 'No users'}")
        assert len(users) == 5, f"Expected 5 users, got {len(users)}"
        
        # Verify user structure
        first_user = users[0]
        required_fields = ['id', 'name', 'email', 'age', 'city']
        for field in required_fields:
            assert field in first_user, f"Missing field: {field}"
        
        print("   ✅ Users endpoint working!")
        print(f"   ✅ All {len(users)} users loaded successfully!")
    else:
        print(f"   ❌ Failed with status code: {response.status_code}")
        print(f"   Error: {response.get_json()}")
        return False
    
    print("\n" + "=" * 50)
    print("✅ All tests passed! Flask application is working correctly.")
    print("=" * 50)
    
    return True


if __name__ == '__main__':
    try:
        success = test_flask_app()
        exit(0 if success else 1)
    except Exception as e:
        print(f"\n❌ Test failed with error: {e}")
        import traceback
        traceback.print_exc()
        exit(1)


# Made with Bob