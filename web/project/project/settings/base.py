"""
Base settings.
"""
from os.path import abspath
from os.path import basename
from os.path import dirname
from os.path import join
from os.path import normpath


##################################################
#                     Paths                      #
##################################################

DJANGO_ROOT = dirname(dirname(abspath(__file__)))

SITE_ROOT = dirname(DJANGO_ROOT)

SITE_NAME = basename(DJANGO_ROOT)


##################################################
#                     Debug                      #
##################################################

DEBUG = False

TEMPLATE_DEBUG = DEBUG


##################################################
#                    Manager                     #
##################################################

ADMINS = (
    ('Laurent Guilbert', 'laurent@guilbert.me'),
)

MANAGERS = ADMINS


##################################################
#                    Database                    #
##################################################

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': join(DJANGO_ROOT, 'db.sqlite3'),
    }
}


##################################################
#                     Cache                      #
##################################################

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}


##################################################
#                    General                     #
##################################################

TIME_ZONE = 'Europe/Paris'

LANGUAGE_CODE = 'fr'

SITE_ID = 1

USE_I18N = True

USE_L10N = True

USE_TZ = True

ALLOWED_HOSTS = ['*']


##################################################
#                     Medias                     #
##################################################

MEDIA_ROOT = normpath(join(SITE_ROOT, 'media'))

MEDIA_URL = '/media/'


##################################################
#                    Statics                     #
##################################################

STATIC_ROOT = normpath(join(SITE_ROOT, 'assets'))

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    normpath(join(SITE_ROOT, 'static')),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)


##################################################
#                     Secret                     #
##################################################

SECRET_KEY = r"@8dtqpd9xfm&=8b@)v)sdhaapg8$&jxt=+!ddon2v@e-%gm5ti"


##################################################
#                   Templates                    #
##################################################

DJANGO_CONTEXT_PROCESSORS = (
    'django.template.context_processors.debug',
    'django.template.context_processors.request',
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
)

LOCAL_CONTEXT_PROCESSORS = (
)

TEMPLATE_CONTEXT_PROCESSORS = (
    LOCAL_CONTEXT_PROCESSORS +
    DJANGO_CONTEXT_PROCESSORS
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            normpath(join(SITE_ROOT, 'templates')),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': TEMPLATE_CONTEXT_PROCESSORS,
        }
    }
]


##################################################
#                  Middlewares                   #
##################################################

DJANGO_MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

LOCAL_MIDDLEWARE_CLASSES = (
)

MIDDLEWARE_CLASSES = DJANGO_MIDDLEWARE_CLASSES + LOCAL_MIDDLEWARE_CLASSES


##################################################
#                      Urls                      #
##################################################

ROOT_URLCONF = '%s.urls' % SITE_NAME


##################################################
#                      Apps                      #
##################################################

DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

THIRD_PARTY_APPS = (
)

LOCAL_APPS = (
    'core',
)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS


##################################################
#                    Logging                     #
##################################################

LOGGING_CONFIG = None

LOGGING = {
    'version': 1,
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s',  # noqa
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'loggers': {
    },
}


##################################################
#                      WSGI                      #
##################################################

WSGI_APPLICATION = 'wsgi.application'
