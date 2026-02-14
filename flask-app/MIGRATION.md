# Migration from Spring Boot to Flask

This document outlines the migration from the Spring Boot Java application to Python Flask.

## Overview

**Issue:** #2 - Code migration  
**Task:** Migrate project to Python Flask  
**Status:** Completed

## Architecture Comparison

### Spring Boot (Java)
```
src/
├── main/
│   ├── java/com/example/demo/
│   │   ├── DemoApplication.java      # Main application
│   │   ├── controller/
│   │   │   └── UserController.java   # REST controller
│   │   └── model/
│   │       └── User.java             # User model
│   └── resources/
│       ├── application.properties    # Configuration
│       └── data/
│           └── users.json            # Data storage
└── pom.xml                           # Maven dependencies
```

### Flask (Python)
```
flask-app/
├── app.py                  # Main application & routes
├── config.py               # Configuration
├── models/
│   ├── __init__.py
│   └── user.py            # User model
├── data/
│   └── users.json         # Data storage
├── requirements.txt       # Python dependencies
└── README.md             # Documentation
```

## Component Mapping

| Spring Boot Component | Flask Equivalent | Notes |
|----------------------|------------------|-------|
| `DemoApplication.java` | `app.py` | Main application entry point |
| `UserController.java` | `app.py` (routes) | REST endpoints defined in main app |
| `User.java` | `models/user.py` | Data model with similar structure |
| `application.properties` | `config.py` | Configuration settings |
| `pom.xml` | `requirements.txt` | Dependency management |

## API Endpoints

Both applications expose the same REST API:

### GET /api/users
Returns list of all users

**Request:**
```bash
curl http://localhost:8080/api/users
```

**Response:**
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

### GET /health (Flask only)
Health check endpoint

**Request:**
```bash
curl http://localhost:8080/health
```

**Response:**
```json
{
  "status": "healthy",
  "service": "demo-app"
}
```

## Configuration

### Spring Boot
```properties
server.port=8080
spring.application.name=demo-app
app.data.file=classpath:data/users.json
```

### Flask
```python
PORT = 8080
HOST = '0.0.0.0'
APP_NAME = 'demo-app'
DATA_FILE = 'data/users.json'
```

## Dependencies

### Spring Boot (Maven)
- Spring Boot Starter Web
- Jackson (JSON processing)
- Spring Boot Starter Test

### Flask (pip)
- Flask 3.0.0
- Werkzeug 3.0.1

## Key Differences

1. **Language**: Java → Python
2. **Framework**: Spring Boot → Flask
3. **Build Tool**: Maven → pip
4. **Configuration**: Properties file → Python module
5. **Dependency Injection**: Spring DI → Manual instantiation
6. **Annotations**: Java annotations → Python decorators

## Advantages of Flask Migration

1. **Simplicity**: Fewer lines of code, easier to understand
2. **Lightweight**: Smaller memory footprint
3. **Flexibility**: More control over application structure
4. **Python Ecosystem**: Access to extensive Python libraries
5. **Rapid Development**: Faster iteration and testing

## Running the Applications

### Spring Boot
```bash
mvn spring-boot:run
# or
java -jar target/demo-0.0.1-SNAPSHOT.jar
```

### Flask
```bash
cd flask-app
python app.py
# or
./run.sh
```

## Testing

### Spring Boot
```bash
mvn test
```

### Flask
```bash
cd flask-app
pip install -r requirements-test.txt
python test_app.py
```

## Data Compatibility

Both applications use the same JSON data format, making data migration seamless:

```json
{
  "id": 1,
  "name": "John Doe",
  "email": "john.doe@example.com",
  "age": 30,
  "city": "New York"
}
```

## Migration Checklist

- [x] Create Flask application structure
- [x] Implement User model
- [x] Implement REST endpoints
- [x] Configure application settings
- [x] Copy user data
- [x] Add documentation
- [x] Create run scripts
- [x] Add test suite
- [x] Verify API compatibility

## Future Enhancements

Potential improvements for the Flask application:

1. Add database support (SQLAlchemy)
2. Implement CRUD operations (POST, PUT, DELETE)
3. Add authentication and authorization
4. Implement input validation
5. Add logging and monitoring
6. Create Docker container
7. Add API documentation (Swagger/OpenAPI)
8. Implement unit tests with pytest

## Conclusion

The migration from Spring Boot to Flask has been completed successfully. The Flask application maintains the same functionality while providing a simpler, more lightweight alternative.

**Related Issue:** Closes #2

---
*Made with Bob*