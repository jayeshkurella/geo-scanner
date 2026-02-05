#!/bin/bash
set -e

# Accept environment name as argument, default to 'dev'
ENV="${1:-dev}"
ENV_FILE="env/.env.$ENV"

# Check if ENV_FILE exists
if [ ! -f "$ENV_FILE" ]; then
  echo "❌ Environment file not found: $ENV_FILE"
  exit 1
fi

# Export all variables from the env file to current shell
export $(grep -v '^#' "$ENV_FILE" | xargs)

echo "✅ Loaded environment variables from $ENV_FILE"
