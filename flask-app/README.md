# Flask Demo Application

Python Flask migration of the Spring Boot demo application.

## Features

- REST API for user management
- JSON-based data storage
- Simple and lightweight Flask framework
- Easy setup and deployment

## Requirements

- Python 3.8 or higher
- pip (Python package manager)

## Installation

1. Navigate to the flask-app directory:
```bash
cd flask-app
```

2. Create a virtual environment (recommended):
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

Start the Flask server:
```bash
python app.py
```

The application will be available at `http://localhost:8080`

## API Endpoints

### Get All Users
```
GET /api/users
```

Returns a list of all users in JSON format.

**Example Response:**
```json
[
  {
    "id": 1,
    "name": "John Doe",
    "email": "john.doe@example.com",
    "age": 30,
    "city": "New York"
  }
]
```

### Health Check
```
GET /health
```

Returns the health status of the application.

**Example Response:**
```json
{
  "status": "healthy",
  "service": "demo-app"
}
```

## Project Structure

```
flask-app/
├── app.py              # Main application file
├── config.py           # Configuration settings
├── requirements.txt    # Python dependencies
├── models/            # Data models
│   ├── __init__.py
│   └── user.py        # User model
├── data/              # JSON data storage
│   └── users.json     # User data
└── README.md          # This file
```

## Configuration

The application can be configured in `config.py`:
- `PORT`: Server port (default: 8080)
- `HOST`: Server host (default: 0.0.0.0)
- `DEBUG`: Debug mode (default: True)
- `DATA_FILE`: Path to users JSON file

## Migration from Spring Boot

This Flask application maintains the same functionality as the original Spring Boot application:
- Same API endpoints (`/api/users`)
- Same data structure
- Same port configuration (8080)
- Compatible JSON data format

## Contributing

Feel free to submit pull requests for improvements.

## Notes

- Made with Bob
- Migrated from Spring Boot to Python Flask (Issue #2)