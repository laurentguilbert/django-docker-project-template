"""
Test settings.
"""
from .base import *  # noqa


##################################################
#                    Database                    #
##################################################

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
        "USER": "",
        "PASSWORD": "",
        "HOST": "",
        "PORT": "",
    },
}


##################################################
#                     Cache                      #
##################################################

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'test-cache',
    }
}


##################################################
#                    Logging                     #
##################################################

LOGGING['root'] = {
    'level': 'ERROR',
}

import logging.config
logging.config.dictConfig(LOGGING)
