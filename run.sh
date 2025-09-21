#!/bin/bash

# Anime vs Real Image Sorter
# Created by amkitpro

echo "========================================"
echo "   Anime vs Real Image Sorter"
echo "   Created by amkitpro"
echo "========================================"
echo ""

# Check if Python is installed
if ! command -v python &> /dev/null; then
    echo "Error: Python is not installed or not in PATH"
    echo "Please install Python 3.7+ from https://python.org"
    exit 1
fi

# Check if virtual environment exists
if [ ! -d "dd-env" ]; then
    echo "Creating virtual environment..."
    python -m venv dd-env
    if [ $? -ne 0 ]; then
        echo "Error: Failed to create virtual environment"
        exit 1
    fi
fi

# Activate virtual environment
echo "Activating virtual environment..."
source dd-env/bin/activate
if [ $? -ne 0 ]; then
    echo "Error: Failed to activate virtual environment"
    exit 1
fi

# Install dependencies
echo "Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt
if [ $? -ne 0 ]; then
    echo "Error: Failed to install dependencies"
    exit 1
fi

# Check if dependencies are installed correctly
echo "Checking dependencies..."
python check_dependencies.py
if [ $? -ne 0 ]; then
    echo "Warning: Some dependencies may not be installed correctly"
fi

# Run the application
echo ""
echo "========================================"
echo "   Starting Anime vs Real Image Sorter"
echo "========================================"
echo ""
python anime_real_sorter.py

echo ""
echo "Application closed."