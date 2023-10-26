"""
ASGI config for config project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application


from os.path import join, dirname
from dotenv import load_dotenv


dotenv_path = join(dirname(__file__),'configSettings','.env')
load_dotenv(dotenv_path)

from django.core.wsgi import get_wsgi_application

if os.environ.get("DEBUG")=="True":
      os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.configSettings.localSettings')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.configSettings.prodSettings')


application = get_asgi_application()
