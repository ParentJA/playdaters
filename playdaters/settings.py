__author__ = 'jason.a.parent@gmail.com (Jason Parent)'

# Standard playdaters imports...
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'i=!h_*o3*frlkp*627=y17w%bf7j1dgf3rvsgd%j&2#4i^b-ko'

DEBUG = True

ALLOWED_HOSTS = []

AUTH_USER_MODEL = 'accounts.User'

DEFAULT_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

THIRD_PARTY_APPS = (
    'django_hstore',
    'debug_toolbar',
    'localflavor',
    'rest_framework',
)

LOCAL_APPS = (
    'accounts',
    'chats',
    'children',
    'friends',
    'play_dates',
)

INSTALLED_APPS = ('grappelli',) + DEFAULT_APPS + THIRD_PARTY_APPS + LOCAL_APPS

REST_METHODS = {
    'get': 'list',
    'post': 'create'
}

REST_METHODS_PK = {
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
}

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'playdaters.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'www/app/'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'playdaters.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'www/app/'),
    os.path.join(BASE_DIR, 'www/bower_components/'),
)

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

MEDIA_URL = '/media/'

DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'


try:
    from .local_settings import *
except ImportError:
    pass
