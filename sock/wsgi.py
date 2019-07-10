"""
WSGI config for sock project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""
from dotenv import load_dotenv
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sock.settings")

# if dotenv file, load it
dotenv_path = os.environ.get(
    'HXMIRADOR_DOTENV_PATH', 'sock.settings')
if dotenv_path:
    load_dotenv(dotenv_path)

application = get_wsgi_application()
