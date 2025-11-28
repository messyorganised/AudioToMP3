#!/bin/bash
cd "$(dirname "$0")"

echo "Checking for Python..."
if ! command -v python3 &> /dev/null; then
    echo "Python 3 is not installed."
    echo "Please install it from https://www.python.org/downloads/"
    read -p "Press enter to exit..."
    exit 1
fi

echo "Installing/Updating dependencies..."
python3 -m pip install -r requirements.txt

echo ""
echo "Starting Audio Converter..."
python3 convert_audio.py

read -p "Press enter to exit..."
