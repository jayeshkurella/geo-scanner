#!/bin/bash
set -e

ENV="dev"

# Load env vars
source scripts/load_env.sh $ENV

# Run migration script (which assumes env vars are loaded)
./scripts/run_migration.sh
