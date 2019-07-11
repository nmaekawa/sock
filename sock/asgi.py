"""
ASGI entrypoint. Configures Django and then runs the application
defined in the ASGI_APPLICATION setting
"""
from dotenv import load_dotenv
import os
from channels.routing import get_default_application
import django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sock.settings.dev")

# if dotenv file, load it
dotenv_path = os.environ.get(
    'SOCK_DOTENV_PATH', 'sock.settings.dev')
if dotenv_path:
    load_dotenv(dotenv_path)

django.setup()
application = get_default_application()
