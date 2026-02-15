# Flask REST API - User Management

Python Flask implementation of the Spring Boot demo application. This is a simple REST API that serves user data from a JSON file.

## Overview

This Flask application is a direct migration from the Java Spring Boot application, providing identical functionality:
- **Endpoint:** `GET /api/users`
- **Data Source:** JSON file (`data/users.json`)
- **Port:** 5000 (Flask default)

## Features

- ✅ RESTful API endpoint for user data
- ✅ JSON file-based data storage
- ✅ Clean MVC architecture
- ✅ Error handling
- ✅ Health check endpoint
- ✅ Configuration management

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

## Installation

### 1. Navigate to Flask Application Directory

```bash
cd flask-app
```

### 2. Create Virtual Environment (Recommended)

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## Running the Application

### Development Mode

```bash
python app.py
```

The application will start on `http://localhost:5000`

### With Environment Variable

```bash
# Development mode (default)
FLASK_ENV=development python app.py

# Production mode
FLASK_ENV=production python app.py
```

## API Endpoints

### 1. Get All Users

**Endpoint:** `GET /api/users`

**Description:** Retrieves all users from the JSON data file

**Response:**
```json
[
  {
    "id": 1,
    "name": "John Doe",
    "email": "john.doe@example.com",
    "age": 30,
    "city": "New York"
  },
  {
    "id": 2,
    "name": "Jane Smith",
    "email": "jane.smith@example.com",
    "age": 28,
    "city": "Los Angeles"
  }
]
```

**Status Codes:**
- `200 OK` - Success
- `404 Not Found` - Data file not found
- `500 Internal Server Error` - Server error

### 2. Root Endpoint

**Endpoint:** `GET /`

**Description:** API information and available endpoints

**Response:**
```json
{
  "name": "demo-app",
  "version": "1.0.0",
  "description": "Flask REST API - Migrated from Spring Boot",
  "endpoints": {
    "/api/users": "GET - Retrieve all users"
  }
}
```

### 3. Health Check

**Endpoint:** `GET /health`

**Description:** Application health status

**Response:**
```json
{
  "status": "healthy"
}
```

## Testing the API

### Using curl

```bash
# Get all users
curl http://localhost:5000/api/users

# Get API info
curl http://localhost:5000/

# Health check
curl http://localhost:5000/health
```

### Using Browser

Simply navigate to:
- http://localhost:5000/api/users
- http://localhost:5000/
- http://localhost:5000/health

### Using Python requests

```python
import requests

response = requests.get('http://localhost:5000/api/users')
users = response.json()
print(users)
```

## Project Structure

```
flask-app/
├── app.py                 # Main Flask application
├── config.py              # Configuration settings
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── models/
│   ├── __init__.py       # Models package
│   └── user.py           # User model class
└── data/
    └── users.json        # User data file
```

## Configuration

Configuration is managed in `config.py` with three environments:

- **Development** - Debug mode enabled
- **Production** - Debug mode disabled
- **Testing** - Testing mode enabled

Default configuration:
- **Host:** 0.0.0.0 (all interfaces)
- **Port:** 5000
- **Debug:** True (development mode)

## Data Model

### User

| Field | Type | Description |
|-------|------|-------------|
| id | Integer | Unique user identifier |
| name | String | User's full name |
| email | String | User's email address |
| age | Integer | User's age |
| city | String | User's city |

## Comparison with Spring Boot

| Feature | Spring Boot | Flask |
|---------|-------------|-------|
| Language | Java 17 | Python 3.8+ |
| Framework | Spring Boot 3.1.0 | Flask 3.0.0 |
| Port | 8080 | 5000 |
| Endpoint | /api/users | /api/users |
| Data Format | JSON | JSON |
| Response | Identical | Identical |

## Error Handling

The application includes comprehensive error handling:

- **404 Not Found** - When data file is missing
- **500 Internal Server Error** - For JSON parsing errors or other exceptions
- Detailed error messages in development mode

## Development

### Adding New Endpoints

Add new routes in `app.py`:

```python
@app.route('/api/new-endpoint', methods=['GET'])
def new_endpoint():
    return jsonify({'message': 'New endpoint'}), 200
```

### Modifying User Model

Edit `models/user.py` to add new fields or methods.

### Changing Configuration

Edit `config.py` to modify application settings.

## Troubleshooting

### Port Already in Use

If port 5000 is already in use, modify the port in `config.py`:

```python
PORT = 5001  # or any available port
```

### Module Not Found Error

Ensure you're in the flask-app directory and virtual environment is activated:

```bash
cd flask-app
source venv/bin/activate  # On macOS/Linux
pip install -r requirements.txt
```

### Data File Not Found

Ensure `data/users.json` exists in the flask-app directory.

## License

This project is part of the bob-demo-project repository.

## Author

Made with Bob - AI-powered development assistant

---

**Note:** This Flask application provides identical functionality to the Spring Boot version and can run alongside it on different ports.