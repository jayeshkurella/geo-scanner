#!/bin/bash

project_directory="/home/administrator/backend_project/workspace/geo-scanner"

echo "Changing directory to project workspace directory"
cd $project_directory || { echo "Failed to change directory to $project_directory"; exit 1; }

echo "Validate the present working directory"
pwd

if [ -d "venv" ]; then
    echo "Python virtual environment exists."
else
    echo "Python virtual environment does not exist. Creating a new one..."
    python3 -m venv venv || { echo "Failed to create virtual environment"; exit 1; }
fi

echo "Activating the virtual environment!"
source venv/bin/activate || { echo "Failed to activate the virtual environment"; exit 1; }

echo "Checking if virtual environment is active after activation"
if [ -z "$VIRTUAL_ENV" ]; then
  echo "No virtual environment is active."
  exit 1
else
  echo "Virtual environment is active: $VIRTUAL_ENV"
fi

echo "Installing Python dependencies!"
pip install -r requirements.txt || { echo "Failed to install dependencies"; exit 1; }

echo "Deactivating the virtual environment"
deactivate

echo "Checking if virtual environment is active after deactivation"
if [ -z "$VIRTUAL_ENV" ]; then
  echo "No virtual environment is active."
else
  echo "Virtual environment is active: $VIRTUAL_ENV"
fi
