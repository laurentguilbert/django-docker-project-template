"""
Local settings.
"""
from .base import *  # noqa


##################################################
#                     Debug                      #
##################################################

DEBUG = True

TEMPLATE_DEBUG = DEBUG

DEBUG_TOOLBAR = False

if DEBUG_TOOLBAR:
    INSTALLED_APPS += (
        'debug_toolbar',
    )
    DEBUG_TOOLBAR_CONFIG = {
        'INTERCEPT_REDIRECTS': False,
        'SHOW_TOOLBAR_CALLBACK': (lambda x: True),
    }
    MIDDLEWARE_CLASSES += (
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    )


##################################################
#                    Logging                     #
##################################################

import logging.config
logging.config.dictConfig(LOGGING)


##################################################
#                      WSGI                      #
##################################################

# Setting WSGI_APPLICATION to None will force django to use the default
# get_wsgi_application for its runserver.
WSGI_APPLICATION = None
