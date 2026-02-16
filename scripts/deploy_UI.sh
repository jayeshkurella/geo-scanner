#!/bin/bash
set -e

PROJECT_DIR="/var/geoscanner"
NEW_PROJECT_ZIP="/var/geoscanner.zip"
BACKUP_DIR="/var/backups/test/geoscanner"

echo "=== UI Deployment Started ==="

# Create required directories
sudo mkdir -p "$PROJECT_DIR"
sudo mkdir -p "$BACKUP_DIR"

# Backup existing project if not empty
if [ "$(ls -A "$PROJECT_DIR" 2>/dev/null)" ]; then
    echo "Existing UI found. Creating backup..."
    BACKUP_ZIP="$BACKUP_DIR/geoscanner_$(date +'%Y%m%d%H%M%S').zip"
    sudo zip -r "$BACKUP_ZIP" "$PROJECT_DIR"
    echo "Backup created at: $BACKUP_ZIP"
else
    echo "No existing UI found. Skipping backup."
fi

# Extract new UI
echo "Extracting new UI package..."
TEMP_DIR=$(mktemp -d)
sudo unzip -q -o "$NEW_PROJECT_ZIP" -d "$TEMP_DIR"

# Remove old files
echo "Cleaning old UI files..."
sudo rm -rf "$PROJECT_DIR"/*

# Detect extracted folder dynamically
EXTRACTED_DIR=$(find "$TEMP_DIR" -maxdepth 1 -type d ! -path "$TEMP_DIR" | head -n 1)

if [ -z "$EXTRACTED_DIR" ]; then
    echo "❌ Extraction failed. No files found."
    exit 1
fi

# Deploy new UI
echo "Deploying new UI..."
sudo mv "$EXTRACTED_DIR"/* "$PROJECT_DIR"

# Update <base href> in index.html
BASE_HREF="/"
INDEX_FILE="$PROJECT_DIR/index.html"

if [ -f "$INDEX_FILE" ]; then
    echo "Updating <base href> in index.html to $BASE_HREF..."
    sudo sed -i "s|<base href=\"[^\"]*\"|<base href=\"$BASE_HREF\"|g" "$INDEX_FILE"
    echo "<base href> updated successfully"
else
    echo "⚠️ index.html not found, skipping base href update"
fi

# Cleanup
sudo rm -rf "$TEMP_DIR"

echo "🎉 UI deployment completed successfully"
