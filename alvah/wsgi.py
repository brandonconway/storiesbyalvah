"""
WSGI config for mez4proj project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os
import sys

path = '/home/storiesbyalvah.com/htdocs'  # use your own username here
if path not in sys.path:
    sys.path.append(path)

from django.core.wsgi import get_wsgi_application
from mezzanine.utils.conf import real_project_name

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "alvah.settings")

application = get_wsgi_application()
