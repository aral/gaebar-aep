# -*- coding: utf-8 -*-
from appenginepatcher import on_production_server
import os
DEBUG = not on_production_server
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)
MANAGERS = ADMINS

DATABASE_ENGINE = 'appengine'

MEDIA_URL = '/media/'

# Email server settings
EMAIL_HOST = 'localhost'
EMAIL_PORT = 25
EMAIL_HOST_USER = 'user'
EMAIL_HOST_PASSWORD = 'password'
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'user@localhost'
SERVER_EMAIL = 'user@localhost'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'ragendja.template.app_prefixed_loader',
    'django.template.loaders.app_directories.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.common.CommonMiddleware',
    'ragendja.middleware.LoginRequiredMiddleware',
)

ROOT_URLCONF = 'urls'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.webdesign',
    'appenginepatcher',
    'app1',
    'app2',
    'gaebar',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.auth',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
)

TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(__file__), 'templates'),
)

CACHE_BACKEND = 'memcached://?timeout=0'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '1234567890'

#
# Gaebar settings
#

GAEBAR_LOCAL_URL = 'http://localhost:8000'

GAEBAR_BACKUPS_FOLDER = '/Users/aral/projects/gaebar-gaed/gaebar/backups/'

GAEBAR_SECRET_KEY = 'change_this_to_something_random'

GAEBAR_SERVERS = {
     u'Local Test': u'http://localhost:8080',
     # Other servers...
}

GAEBAR_MODELS = (
     (
          'app1.models', 
          (u'Profile', u'GoogleAccount', u'AllOtherTypes', u'PlasticMan', u'GrandFather', u'Father', u'Child', ),
     ),
     (
          'app2.models', 
          (u'Simple',),
     ),
)
