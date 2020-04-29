"""
Replace some settings.
"""

import os

import dj_database_url

from server.settings import *

INSTALLED_APPS.remove('gerapy.server.core')
INSTALLED_APPS.append('core')

ROOT_URLCONF = 'dev_server.urls'

if os.getcwd() == '/app':
    DEBUG = False

    DATABASES = {
        'default': dj_database_url.config(
            default=os.getenv('DATABASE_URL')
    )
}
