#!/bin/bash

# Flask Application Startup Script
# Made with Bob

echo "=================================="
echo "Flask Demo Application"
echo "=================================="
echo ""

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
    echo "✓ Virtual environment created"
    echo ""
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate
echo "✓ Virtual environment activated"
echo ""

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt --quiet
echo "✓ Dependencies installed"
echo ""

# Run the application
echo "Starting Flask application on port 8080..."
echo "Press Ctrl+C to stop the server"
echo ""
python app.py