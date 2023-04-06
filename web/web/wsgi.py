"""
WSGI config for web project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os
import pathlib

import dotenv
from django.core.wsgi import get_wsgi_application

# Current file's Directory 
CURRENT_DIR = pathlib.Path(__file__).resolve().parent

# Root Directory (where 'manage.py' stands)
BASE_DIR = CURRENT_DIR.parent

ENV_FILE_PATH = BASE_DIR / ".env"

# Read the environment variables file
dotenv.read_dotenv(str(ENV_FILE_PATH))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'web.settings')

application = get_wsgi_application()
