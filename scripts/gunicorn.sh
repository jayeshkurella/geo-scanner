#!/bin/bash

# Load environment variables
set -o allexport
source .env.dev
set +o allexport

echo "Changing directory to project workspace directory"
cd "$PROJECT_DIR" || { 
    echo "Failed to change directory to $PROJECT_DIR"
    exit 1
}

echo "Validate the present working directory"
pwd

SERVICE_FILE="$PROJECT_DIR/scripts/$SERVICE_FILE_NAME"

# Check if service file exists
if [ -f "$SERVICE_FILE" ]; then
    echo "$SERVICE_FILE_NAME found. Copying the service file..."
    
    sudo cp "$SERVICE_FILE" "$SYSTEMD_PATH/"
    sudo systemctl daemon-reload
    sudo systemctl enable "$SERVICE_NAME"
    sudo systemctl restart "$SERVICE_NAME"
    
    echo "$SERVICE_NAME has been started and enabled."
else
    echo "Error: $SERVICE_FILE_NAME not found at $SERVICE_FILE"
    exit 1
fi

# Check service status
SERVICE_STATUS=$(sudo systemctl is-active "$SERVICE_NAME")

if [ "$SERVICE_STATUS" == "active" ]; then
    echo "$SERVICE_NAME is running successfully."
else
    echo "$SERVICE_NAME failed to start. Status: $SERVICE_STATUS"
    exit 1
fi

# Create log directory if not exists
if [ -d "$LOG_DIR" ]; then
    echo "Log directory $LOG_DIR is present."
else
    echo "Log directory $LOG_DIR not found. Creating..."
    
    sudo mkdir -p "$LOG_DIR"
    sudo touch "$LOG_DIR/error.log" "$LOG_DIR/access.log"
    sudo chown -R $USER:$USER "$LOG_DIR"
    
    echo "Log directory and log files created at $LOG_DIR"
fi
