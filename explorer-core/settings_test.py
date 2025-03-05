"""
Django settings for explorer-core project.

Generated by 'django-admin startproject' using Django 4.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os
import dj_database_url
from dotenv import load_dotenv


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(os.path.join(BASE_DIR, '.env'))
# load_dotenv(os.path.join(BASE_DIR, '.env_gcr'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DJANGO_DEBUG', 'False') == 'True'
# SECURITY WARNING: don't run with wildcard in production!
# ALLOWED_HOSTS = os.getenv('DJANGO_ALLOWED_HOSTS', '*').split(',')
ALLOWED_HOSTS = os.getenv('DJANGO_ALLOWED_HOSTS').split(',')

    # SECURE_SSL_REDIRECT = True
    # SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    #
    # CSRF_COOKIE_SECURE = True
    # SESSION_COOKIE_SECURE = True
    #
    # # Recommended security settings
    # SECURE_HSTS_SECONDS = 31536000  # Enforce HTTP Strict Transport Security (HSTS) for 1 year
    # SECURE_HSTS_INCLUDE_SUBDOMAINS = True  # Apply HSTS to all subdomains
    # SECURE_HSTS_PRELOAD = True  # Preload HSTS in browsers
    #
    # # Prevent browser from inferring MIME types
    # SECURE_CONTENT_TYPE_NOSNIFF = True
    #
    # # X-Content-Type-Options header set to nosniff
    # X_FRAME_OPTIONS = 'DENY'


# INTERNAL_IPS = os.getenv('DJANGO_INTERNAL_IPS')

# API Authentication
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        # 'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
        # 'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ),
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

SPECTACULAR_SETTINGS = {
    'TITLE': 'Collections Explorer API',
    'DESCRIPTION': 'This is the API for the explorer-core project of California Academy of Sciences\' Scientific Computing',
    'VERSION': 'beta',
    'SERVE_INCLUDE_SCHEMA': False,  # Set True if you want to include the schema in the UI
    # Optional: customize URLs or other settings here
}

CORS_ORIGIN_ALLOW_ALL = True

# CORS_ORIGIN_WHITELIST = [
#     'http://your-frontend-domain.com',
#     'https://your-frontend-domain.com',
# ]


CORS_ALLOW_METHODS = [
    'GET',
    'OPTIONS'
]

CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
]

# WSGI_APPLICATION = "explorer-core.wsgi.application"

# Application definition

INSTALLED_APPS = [
    "django_extensions",
    # "jazzmin",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "debug_toolbar",
    "collections_app_api",
    "corsheaders",
    "rest_framework",
    "rest_framework.authtoken",
    "drf_spectacular",
    # 'collections_app_api.apps.APIConfig'
]


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    'corsheaders.middleware.CorsMiddleware',
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "collections_app_api.middleware.CustomMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    # "collections_app_api.middleware_test.LogEndpointMiddleware",
]

ROOT_URLCONF = "explorer-core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, 'templates')],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
            # must have default database, will look into removing/setting up dummy default db
            "default": dj_database_url.config(
                default=os.environ.get('DATABASE_URL')),
            "collections": {
                 'ENGINE': 'django.db.backends.mysql',
                 'NAME': os.getenv('MYSQL_DATABASE'),
                 'USER': os.getenv('MYSQL_USER'),
                 'PASSWORD': os.getenv('MYSQL_PASSWORD'),
                 'HOST': os.getenv('DB_HOST'),
                 'PORT': os.getenv('DB_PORT'),
                'OPTIONS': {
                    'init_command': "SET SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED",
                    'connect_timeout': 10,
                }
             },
}

DATABASE_ROUTERS = ['collections_app_api.routers.CollectionsDatabaseRouter']


# AUTH_USER_MODEL = 'collections_app_api.UserProfile'
#
# AUTHENTICATION_BACKENDS = ['django.contrib.auth.backends.ModelBackend',
#                            ]


# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname}: {asctime} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'django.log'),
            'formatter': 'verbose',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'file'],
            'level': 'INFO',
            'propagate': True,
        },
        'collections_app_api': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
    },
}



# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

X_FRAME_OPTIONS = 'SAMEORIGIN'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'
# STATIC_ROOT = '/collections_app_api/static/'
# STATICFILES_DIRS = [ BASE_DIR / 'collections_app_api' / 'static']

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
###### The following line is configured to GCR nginx service

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
