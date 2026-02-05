#!/bin/bash
set -e

ENV="${1:-dev}"

# Use Jenkins workspace (repo root) as base directory
BASE_DIR="$(cd "$(dirname "$0")/.." && pwd)"
ENV_FILE="$BASE_DIR/.env.$ENV"

if [ ! -f "$ENV_FILE" ]; then
    echo "❌ Environment file not found: $ENV_FILE"
    exit 1
fi

export $(grep -v '^#' "$ENV_FILE" | xargs)
echo "✅ Loaded environment variables from $ENV_FILE"
