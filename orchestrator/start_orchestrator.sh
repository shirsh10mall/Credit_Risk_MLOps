#!/bin/bash
set -e

echo "⏳ Ensuring required databases exist..."
python /opt/orchestrator/db_init.py

echo "🚀 Setting up orchestrator services..."

#!/usr/bin/env bash
set -euo pipefail

# Set defaults if not provided via .env
POSTGRES_USER="${POSTGRES_USER:-mlops_user}"
POSTGRES_PASSWORD="${POSTGRES_PASSWORD:-mlops_pass}"
POSTGRES_HOST="${POSTGRES_HOST:-postgres}"
POSTGRES_PORT="${POSTGRES_PORT:-5432}"

MLFLOW_BACKEND_STORE_URI="${MLFLOW_BACKEND_STORE_URI:-postgresql+psycopg2://${POSTGRES_USER}:${POSTGRES_PASSWORD}@${POSTGRES_HOST}:${POSTGRES_PORT}/mlflow_tracking_db}"
MLFLOW_ARTIFACT_ROOT="${MLFLOW_ARTIFACT_ROOT:-file:///mlflow/artifacts}"

# Start MLflow server
echo "Starting MLflow server..."
mlflow server \
  --backend-store-uri "${MLFLOW_BACKEND_STORE_URI}" \
  --default-artifact-root "${MLFLOW_ARTIFACT_ROOT}" \
  --host 0.0.0.0 --port 5001 &

sleep 3

# Initialize Airflow DB
export AIRFLOW_HOME="${AIRFLOW_HOME:-/opt/airflow}"

echo "Migrating Airflow DB..."
airflow db migrate

# Create a default Airflow user if not exists
echo "👤 Bootstrapping Airflow admin user..."

# Start scheduler & webserver
echo "Starting Airflow scheduler..."
airflow scheduler &

echo "Starting Airflow API server..."
exec airflow api-server
