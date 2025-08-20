#!/usr/bin/env bash
set -e

echo "⏳ Running DB bootstrap..."
python /app/db_init.py

set -euo pipefail

# Start Gradio app in background (port 7860)
echo "Starting Gradio UI..."
python /app/gradio_app.py &

# Wait briefly for gradio to start
sleep 2

# Start FastAPI (uvicorn)
echo "Starting FastAPI (uvicorn) on 0.0.0.0:8000 ..."
exec uvicorn app.inference_api:app --host 0.0.0.0 --port 8000 --workers 1