from .base import *

"""
Setting for testing/debugging the project
"""


DEBUG = True
ALLOWED_HOSTS = ['*']

INSTALLED_APPS += [
    'debug_toolbar',
    'django_extensions',
]

RAVEN_CONFIG = {
    'dsn': 'http://cd080bdc4c93416582eb9bef13592bb5:c39749cb478344a68d5e4fe627bdb334@192.168.88.181:9000/8',
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