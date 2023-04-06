#!/bin/bash

APP_PORT=${PORT:-8008}
cd /app/
/opt/venv/bin/python3 manage.py collectstatic --noinput
/opt/venv/bin/gunicorn --worker-tmp-dir /dev/shm web.wsgi:application --bind "0.0.0.0:${APP_PORT}"
