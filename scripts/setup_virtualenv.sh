#!/bin/bash

# Load environment variables
set -o allexport
source env/.env.dev
set +o allexport

echo "Changing directory to project workspace directory"
cd "$PROJECT_DIR" || { echo "Failed to change directory to $PROJECT_DIR"; exit 1; }

echo "Validate The Present working directory"
pwd

if [ -d "$VENV_DIR" ]; then
    echo "Python virtual environment exists."
else
    echo "Python virtual environment does not exist. Creating a new one..."
    $PYTHON_BIN -m venv "$VENV_DIR" || { echo "Failed to create virtual environment"; exit 1; }
fi

echo "Activating the virtual environment!"
source "$VENV_DIR/bin/activate" || { echo "Failed to activate the virtual environment"; exit 1; }

echo "Checking if virtual environment is active after activation"
if [ -z "$VIRTUAL_ENV" ]; then
  echo "No virtual environment is active."
  exit 1
else
  echo "Virtual environment is active: $VIRTUAL_ENV"
fi

echo "Installing Python dependencies!"
pip install -r "$REQUIREMENTS_FILE" || { echo "Failed to install dependencies"; exit 1; }

echo "Deactivating the virtual environment"
deactivate

echo "Checking if virtual environment is active after deactivation"
if [ -z "$VIRTUAL_ENV" ]; then
  echo "No virtual environment is active."
else
  echo "Virtual environment is active: $VIRTUAL_ENV"
fi
