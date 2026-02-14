"""
Simple test script to verify the Flask application
"""
import requests
import json

BASE_URL = "http://localhost:8080"

def test_health_check():
    """Test the health check endpoint"""
    print("Testing health check endpoint...")
    try:
        response = requests.get(f"{BASE_URL}/health")
        print(f"Status Code: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
        assert response.status_code == 200
        print("✓ Health check passed\n")
        return True
    except Exception as e:
        print(f"✗ Health check failed: {e}\n")
        return False

def test_get_users():
    """Test the get users endpoint"""
    print("Testing get users endpoint...")
    try:
        response = requests.get(f"{BASE_URL}/api/users")
        print(f"Status Code: {response.status_code}")
        users = response.json()
        print(f"Number of users: {len(users)}")
        print(f"Response: {json.dumps(users, indent=2)}")
        assert response.status_code == 200
        assert len(users) > 0
        print("✓ Get users passed\n")
        return True
    except Exception as e:
        print(f"✗ Get users failed: {e}\n")
        return False

if __name__ == "__main__":
    print("=" * 50)
    print("Flask Application Test Suite")
    print("=" * 50)
    print()
    
    print("Make sure the Flask application is running on port 8080")
    print("Run: python app.py")
    print()
    
    input("Press Enter to start tests...")
    print()
    
    results = []
    results.append(test_health_check())
    results.append(test_get_users())
    
    print("=" * 50)
    print("Test Results")
    print("=" * 50)
    passed = sum(results)
    total = len(results)
    print(f"Passed: {passed}/{total}")
    
    if passed == total:
        print("✓ All tests passed!")
    else:
        print("✗ Some tests failed")

# Made with Bob