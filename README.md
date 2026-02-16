# Demo Flask API

A Python Flask REST API migrated from Spring Boot Java application. This API provides endpoints to retrieve user data from a JSON file.

## 🚀 Migration from Spring Boot to Flask

This project has been migrated from a Java Spring Boot application to Python Flask as part of Issue #7.

### Original Java Structure
- **Spring Boot Application**: `DemoApplication.java`
- **REST Controller**: `UserController.java`
- **Model**: `User.java`
- **Configuration**: `application.properties`

### New Flask Structure
- **Flask Application**: `app.py`
- **Model**: `models/user.py`
- **Configuration**: `config.py`
- **Data**: `data/users.json`

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

## 🛠️ Installation

### 1. Clone the repository

```bash
git clone <repository-url>
cd bob-demo-project
```

### 2. Create a virtual environment

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## 🏃 Running the Application

### Development Mode

```bash
python app.py
```

The application will start on `http://localhost:8080`

### Using Flask CLI

```bash
# Set Flask app
export FLASK_APP=app.py

# Run in development mode
flask run --host=0.0.0.0 --port=8080
```

### Environment Variables

You can customize the application using environment variables:

```bash
# Set port (default: 8080)
export PORT=8080

# Set host (default: 0.0.0.0)
export HOST=0.0.0.0

# Enable debug mode
export FLASK_DEBUG=true

# Set environment
export FLASK_ENV=development
```

## 📡 API Endpoints

### Get All Users

**Endpoint**: `GET /api/users`

**Description**: Retrieves all users from the JSON data file.

**Response**: 200 OK

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

**Error Response**: 500 Internal Server Error

```json
{
  "error": "Internal server error",
  "details": "Error message"
}
```

### Health Check

**Endpoint**: `GET /health`

**Description**: Check if the application is running.

**Response**: 200 OK

```json
{
  "status": "healthy",
  "app": "demo-app"
}
```

### Root Endpoint

**Endpoint**: `GET /`

**Description**: Get API information.

**Response**: 200 OK

```json
{
  "message": "Flask Demo API",
  "version": "1.0.0",
  "endpoints": {
    "users": "/api/users",
    "health": "/health"
  }
}
```

## 🧪 Testing the API

### Using curl

```bash
# Get all users
curl http://localhost:8080/api/users

# Health check
curl http://localhost:8080/health

# Root endpoint
curl http://localhost:8080/
```

### Using httpie

```bash
# Get all users
http GET http://localhost:8080/api/users

# Health check
http GET http://localhost:8080/health
```

### Using a web browser

Simply navigate to:
- http://localhost:8080/api/users
- http://localhost:8080/health
- http://localhost:8080/

## 📁 Project Structure

```
bob-demo-project/
├── app.py                      # Flask application entry point
├── config.py                   # Configuration settings
├── requirements.txt            # Python dependencies
├── models/
│   └── user.py                # User data model
├── data/
│   └── users.json             # User data file
├── src/                       # Original Java Spring Boot code
│   └── main/
│       ├── java/
│       └── resources/
└── README.md                  # This file
```

## 🔧 Configuration

The application can be configured through `config.py` or environment variables:

| Setting | Environment Variable | Default | Description |
|---------|---------------------|---------|-------------|
| Port | `PORT` | 8080 | Server port |
| Host | `HOST` | 0.0.0.0 | Server host |
| Debug | `FLASK_DEBUG` | False | Debug mode |
| Environment | `FLASK_ENV` | development | Application environment |
| Data File | - | data/users.json | Path to user data file |

## 🆚 Comparison: Spring Boot vs Flask

| Feature | Spring Boot (Java) | Flask (Python) |
|---------|-------------------|----------------|
| Main File | `DemoApplication.java` | `app.py` |
| Controller | `@RestController` | `@app.route()` |
| Model | POJO with getters/setters | `@dataclass` |
| Config | `application.properties` | `config.py` |
| Port | 8080 | 8080 |
| Endpoint | `/api/users` | `/api/users` |
| Response | `ResponseEntity<List<User>>` | `jsonify(users_list)` |

## 🐛 Troubleshooting

### Port already in use

If port 8080 is already in use, you can change it:

```bash
export PORT=8081
python app.py
```

### Module not found errors

Make sure you've activated the virtual environment and installed dependencies:

```bash
source venv/bin/activate
pip install -r requirements.txt
```

### Data file not found

Ensure the `data/users.json` file exists in the project root directory.

## 📝 Development

### Adding New Endpoints

Add new routes in `app.py` within the `register_routes()` function:

```python
@app.route('/api/new-endpoint', methods=['GET'])
def new_endpoint():
    return jsonify({'message': 'New endpoint'}), 200
```

### Modifying User Model

Edit `models/user.py` to add or modify user fields.

## 🤝 Contributing

1. Create a feature branch
2. Make your changes
3. Test thoroughly
4. Submit a pull request

## 📄 License

This project is part of a code modernization initiative (Issue #7).

## 👨‍💻 Made with Bob

This Flask migration was implemented by Bob, following best practices for Python web development.

---

**Original Java Spring Boot Application**: See `src/main/java/` directory
**Flask Python Application**: See root directory files