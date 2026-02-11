#!/bin/bash

# Load environment variables
set -o allexport
source env/.env.dev
set +o allexport

echo "Change directory to python project directory"
cd "$PROJECT_DIR" || { echo "Failed to change directory"; exit 1; }

echo "Activating the virtual environment"
source "$VENV_DIR/bin/activate" || { echo "Failed to activate venv"; exit 1; }

echo "Checking if virtual environment is active after activation"
if [ -z "$VIRTUAL_ENV" ]; then
  echo "No virtual environment is active."
  exit 1
else
  echo "Virtual environment is active: $VIRTUAL_ENV"
fi

echo "Processing for migrations"
$PYTHON_BIN "$MANAGE_FILE" migrate --noinput || { echo "Migration failed"; exit 1; }

echo "Migrations Done"

echo "Deactivating the virtual environment"
deactivate

echo "Checking if virtual environment is active after deactivation"
if [ -z "$VIRTUAL_ENV" ]; then
  echo "No virtual environment is active."
else
  echo "Virtual environment is active: $VIRTUAL_ENV"
fi
