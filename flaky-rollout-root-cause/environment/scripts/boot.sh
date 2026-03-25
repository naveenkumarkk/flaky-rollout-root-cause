#!/bin/bash
set -e

cd /app

if [ -f /app/api/.env.example ]; then
  source /app/api/.env.example
fi

mkdir -p /app/data

nginx

gunicorn --bind ${APP_HOST:-127.0.0.1}:${APP_PORT:-5000} api.app:app &
APP_PID=$!

python3 /app/api/migrate.py

wait $APP_PID