from .base import *

"""
Setting for development
"""

DEBUG = True

ALLOWED_HOSTS = ['*']

# settings for testing
INTERNAL_IPS = ['172.29.0.1']

INSTALLED_APPS += [
    'debug_toolbar',
    'django_extensions',
]

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

AUTH_PASSWORD_VALIDATORS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': 'db',
        'PORT': 5432,
        'ATOMIC_REQUESTS': True
    }
}
REDIS_PORT = os.environ.get("REDIS_PORT", '6379')
REDIS_HOST = os.environ.get("REDIS_HOST", "redis")
