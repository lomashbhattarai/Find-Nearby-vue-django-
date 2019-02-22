from .settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'test',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
        }
}

CORS_ORIGIN_WHITELIST=(
    'localhost:8081',
    '127.0.0.1:8081'
)
DEBUG =True

# INSTALLED_APPS += [
#
#     'debug_toolbar',
#
# ]
#
# MIDDLEWARE += [
#     'debug_toolbar.middleware.DebugToolbarMiddleware',

# ]
# INTERNAL_IPS = '127.0.0.1'
