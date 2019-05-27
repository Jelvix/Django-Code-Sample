from .base import *

"""
Settings for prod
"""


DEBUG = False
ALLOWED_HOSTS = ['192.168.88.167']


RAVEN_CONFIG = {
    'dsn': 'http://6b0478066f1d484d82cdcd18f2ffd54e:405794779a86421a884a46d03b400970@31.202.123.239:3012/9',
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
