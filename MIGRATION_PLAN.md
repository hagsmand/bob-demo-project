# Spring Boot to Flask Migration Plan

## Issue Reference
**GitHub Issue:** [#6 - Code Modernize](https://github.com/hagsmand/bob-demo-project/issues/6)
**Objective:** Modernize Java Spring Boot to Python Flask

## Current Application Analysis

### Existing Spring Boot Application
- **Framework:** Spring Boot 3.1.0 with Java 17
- **Port:** 8080
- **Endpoint:** GET /api/users
- **Data Source:** JSON file (src/main/resources/data/users.json)
- **Functionality:** Returns list of users with fields: id, name, email, age, city

### User Model Structure
```json
{
  "id": number,
  "name": string,
  "email": string,
  "age": number,
  "city": string
}
```

## Migration Strategy

### Approach
- **Keep both implementations** - Spring Boot code remains intact
- **Create Flask in separate directory** - `flask-app/`
- **Port:** 5000 (Flask default)
- **No additional features** - Direct equivalent implementation

## Flask Application Structure

```
flask-app/
├── app.py                 # Main Flask application
├── models/
│   └── user.py           # User model class
├── data/
│   └── users.json        # User data (copied from Spring Boot)
├── config.py             # Configuration settings
├── requirements.txt      # Python dependencies
└── README.md            # Setup and run instructions
```

## Implementation Steps

### 1. Project Structure Setup
- Create `flask-app/` directory
- Create subdirectories: `models/`, `data/`

### 2. Core Files Implementation

#### app.py
- Initialize Flask application
- Configure JSON file path
- Implement GET /api/users endpoint
- Error handling for file operations
- Run on port 5000

#### models/user.py
- User class with properties: id, name, email, age, city
- to_dict() method for JSON serialization
- from_dict() class method for deserialization

#### config.py
- Application configuration
- Data file path configuration
- Environment-specific settings

### 3. Data Migration
- Copy users.json from `src/main/resources/data/` to `flask-app/data/`
- Maintain exact same data structure

### 4. Dependencies
**requirements.txt:**
- Flask==3.0.0
- python-dotenv==1.0.0 (for environment variables)

### 5. Documentation
**README.md includes:**
- Project description
- Prerequisites (Python 3.8+)
- Installation steps
- Running the application
- API endpoint documentation
- Testing instructions

## API Compatibility

### Endpoint Mapping
| Spring Boot | Flask | Method | Response |
|-------------|-------|--------|----------|
| /api/users | /api/users | GET | List of users (JSON) |

### Response Format
Both implementations return identical JSON structure:
```json
[
  {
    "id": 1,
    "name": "John Doe",
    "email": "john.doe@example.com",
    "age": 30,
    "city": "New York"
  },
  ...
]
```

## Testing Plan

1. **Start Flask application** - Verify it runs on port 5000
2. **Test /api/users endpoint** - Confirm JSON response matches Spring Boot
3. **Error handling** - Test with missing/corrupted data file
4. **Compare responses** - Ensure both implementations return identical data
5. **Create Unittest for Flask application** - Ensure 80% coverage

## Git Workflow

1. Create feature branch: `feature/flask-migration`
2. Commit Flask implementation with message: `Fixes #6: Add Flask implementation alongside Spring Boot`
3. Create pull request referencing issue #6
4. Update issue status to `in-review`

## Success Criteria

- ✅ Flask application runs successfully on port 5000
- ✅ GET /api/users returns same data as Spring Boot version
- ✅ Both implementations coexist in the repository
- ✅ Complete documentation for Flask setup and usage
- ✅ All dependencies listed in requirements.txt
- ✅ Pull request created and linked to issue #6

## Architecture Diagram

```mermaid
graph TB
    subgraph "Repository Structure"
        A[bob-demo-project]
        B[Spring Boot App]
        C[Flask App]
        A --> B
        A --> C
    end
    
    subgraph "Spring Boot"
        B --> D[Port 8080]
        D --> E[/api/users]
        E --> F[users.json]
    end
    
    subgraph "Flask"
        C --> G[Port 5000]
        G --> H[/api/users]
        H --> I[users.json]
    end
    
    style B fill:#6db33f
    style C fill:#000000
    style D fill:#lightblue
    style G fill:#lightblue
```

## Timeline

- **Planning:** Complete ✅
- **Implementation:** Ready to start
- **Testing:** After implementation
- **PR & Review:** After testing
- **Estimated Duration:** 1-2 hours

## Notes

- Spring Boot application remains fully functional
- Flask provides modern Python alternative
- Both can run simultaneously on different ports
- Easy comparison and testing between implementations