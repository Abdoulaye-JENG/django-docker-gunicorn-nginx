#!/bin/bash

SUPERUSER_EMAIL=${DANGO_SUPERUSER_EMAIL:-"admin@admin.com"}
SUPERUSER_USERNAME=${DANGO_SUPERUSER_USERNAME:-"administrator"}
SUPERUSER_PASSWORD=${DANGO_SUPERUSER_PASSWORD:-"admin2023"}

cd /app/

/opt/venv/bin/python3 manage.py makemigrations --noinput || true
/opt/venv/bin/python3 manage.py migrate --noinput
/opt/venv/bin/python3 manage.py createsuperuser  --username $SUPERUSER_USERNAME  --noinput || true
