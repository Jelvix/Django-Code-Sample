from .base import *

"""
Settings for stage
"""

DEBUG = False
ALLOWED_HOSTS = ['192.168.88.167']


RAVEN_CONFIG = {
    'dsn': 'http://221465099f95441c9cb779821646d676:99e58c0c08de47ed8326caacf61008d5@31.202.123.239:3012/10',
}

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