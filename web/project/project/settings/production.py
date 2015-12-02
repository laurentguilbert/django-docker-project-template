"""
Production settings.
"""
from .base import *  # noqa


##################################################
#                     Debug                      #
##################################################

DEBUG = False


##################################################
#                   Databases                    #
##################################################

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': 'postgres',
        'PORT': 5432,
    }
}


##################################################
#                    Logging                     #
##################################################

RAVEN_CONFIG = {
    'dsn': '',
}

INSTALLED_APPS += (
    'raven.contrib.django.raven_compat',
)

LOGGING['root'] = {
    'level': 'WARNING',
    'handlers': ['sentry'],
}

LOGGING['handlers']['sentry'] = {
    'level': 'ERROR',
    'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
}

LOGGING['loggers']['raven'] = {
    'level': 'DEBUG',
    'handlers': ['console'],
    'propagate': False,
}

LOGGING['loggers']['sentry.errors'] = {
    'level': 'DEBUG',
    'handlers': ['console'],
    'propagate': False,
}

import logging.config
logging.config.dictConfig(LOGGING)
