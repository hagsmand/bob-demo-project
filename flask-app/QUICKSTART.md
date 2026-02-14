# Quick Start Guide

Get the Flask application running in 3 simple steps!

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

## Option 1: Using the Run Script (Recommended)

```bash
cd flask-app
./run.sh
```

The script will automatically:
- Create a virtual environment
- Install dependencies
- Start the Flask server

## Option 2: Manual Setup

### Step 1: Create Virtual Environment

```bash
cd flask-app
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Run the Application

```bash
python app.py
```

## Verify Installation

Once the server is running, test the API:

### Using curl:
```bash
# Health check
curl http://localhost:8080/health

# Get all users
curl http://localhost:8080/api/users
```

### Using a browser:
Open your browser and navigate to:
- http://localhost:8080/health
- http://localhost:8080/api/users

### Using the test script:
```bash
# In a new terminal (keep the server running)
cd flask-app
pip install -r requirements-test.txt
python test_app.py
```

## Expected Output

### Health Check Response:
```json
{
  "status": "healthy",
  "service": "demo-app"
}
```

### Users Response:
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

## Troubleshooting

### Port Already in Use
If port 8080 is already in use, you can change it in `config.py`:
```python
PORT = 8081  # or any available port
```

### Module Not Found Error
Make sure you've activated the virtual environment:
```bash
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Permission Denied (run.sh)
Make the script executable:
```bash
chmod +x run.sh
```

## Next Steps

- Read the full [README.md](README.md) for detailed documentation
- Check [MIGRATION.md](MIGRATION.md) to understand the migration from Spring Boot
- Explore the code in `app.py` and `models/user.py`

---
*Made with Bob - Issue #2*