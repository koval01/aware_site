"""
Django settings for awse_web project.

Generated by 'django-admin startproject' using Django 3.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os.path

build_ = hex(175326092021)[2:]

# settings.configure(
#     image_proxy_key = os.environ['IMAGE_PROXY_KEY'],
#     image_link_key = os.environ['IMAGE_LINK_KEY'],
# )

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = os.environ['SECRET_KEY_DJANGO']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

LOCAL_DATABASE = False
CACHE_IN_MEMORY_SERVER = True

CLOUDFLARE = True
IS_HEROKU = False

# USE_SRI = True

if DEBUG:
    SECRET_KEY = 'debugsecretkey'
    ALLOWED_HOSTS = ['*']
    LOG_HANDLERS = ['console']
    append_gunicorn_config = False

else:
    from dotenv import load_dotenv
    load_dotenv()
    SECRET_KEY = os.environ['SECRET_KEY_DJANGO']
    ALLOWED_HOSTS = ['awse.us']
    LOG_HANDLERS = ['console']
    append_gunicorn_config = False  # Heroku mode
    SECURE_SSL_REDIRECT = True
    PREPEND_WWW = False


if LOCAL_DATABASE:
    # Local database
    DB_HOST = 'localhost'
    DB_PASS = ''
    DB_USER = 'template1'
    DB_NAME = 'template1'
    ssl_mode = None

else:
    DB_HOST = os.environ['DB_HOST']
    DB_USER = os.environ['DB_USER']
    DB_NAME = os.environ['DB_NAME']
    DB_PASS = os.environ['DB_PASS']
    ssl_mode = None  # 'require'


NEWSAPI_TOKEN = os.environ['NEWS_API_TOKEN'].split()

DEPLOY_RETOKEN_PUBLIC = os.environ['RECAPTCHA_PUBLIC_KEY']
DEPLOY_RETOKEN_PRIVATE = os.environ['RECAPTCHA_PRIVATE_KEY']

# INFOBOT_TOKEN = os.environ['INFOBOT_TOKEN']

REQ_USER_AGENT = os.environ['REQ_USER_AGENT']

TEST_RETOKEN_PUBLIC = '6Lep8tEaAAAAAKr5V662XA4LK9O-NsE23rrqo2CI'
TEST_RETOKEN_PRIVATE = '6Lep8tEaAAAAACckN_qxPgcyuBsbEPxRF_jRqThA'

MAX_SEARCH_LENGTH = 700

AVAILABLE_COUNTRY = ['ua']

if DEBUG:
    RETOKEN_PUBLIC = TEST_RETOKEN_PUBLIC
    RETOKEN_PRIVATE = TEST_RETOKEN_PRIVATE
else:
    RETOKEN_PUBLIC = DEPLOY_RETOKEN_PUBLIC
    RETOKEN_PRIVATE = DEPLOY_RETOKEN_PRIVATE

IMAGE_PROXY_KEY = os.environ['IMAGE_PROXY_KEY']
IMAGE_PROXY_LINK_KEY = os.environ['IMAGE_LINK_KEY']
LOAD_ENCRYPT_KEY = os.environ['LOAD_MORE_KEY']
SIGN_ENCRYPT_KEY = os.environ['SIGN_ENCRYPT_KEY']

SEARCH_CX = os.environ['SEARCH_CX']
SEARCH_API_HOST = os.environ['SEARCH_API_HOST']
SEARCH_API_KEYS = os.environ['SEARCH_API_KEYS']
BOT_CHECK_TOKEN = os.environ['BOT_CHECK_TOKEN']

BOT_BLOCK_ADD = False

ADVERTISE_BOT_KEY = os.environ['ADVERTISE_BOT_KEY']

WEATHER_API_KEYS = os.environ['WEATHER_API_KEYS']

if IS_HEROKU:
    HEROKU_API_KEY = os.environ['HEROKU_API_KEY']
    HEROKU_APP_NAME = os.environ['HEROKU_APP_NAME']
else:
    BUILD_ID = build_

TWITTER_BEARER = os.environ['TWITTER_BEARER']
NEWSAPI_AI = os.environ['NEWSAPI_AI']

IMAGES_SEARCH_ENABLED = True
NEED_IMAGES_DESC = False

# Application definition

INSTALLED_APPS = [
    'awse',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'compressor',
    'blacklist',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # 'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'blacklist.middleware.BlacklistMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.gzip.GZipMiddleware',
]

ROOT_URLCONF = 'awse_web.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'awse_web.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': DB_NAME,
        'USER': DB_USER,
        'PASSWORD': DB_PASS,
        'HOST': DB_HOST,
        'PORT': '5432',
        'OPTIONS': {'sslmode': ssl_mode},
    }
}

if CACHE_IN_MEMORY_SERVER:
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
            'LOCATION': 'unique-snowflake',
        }
    }

else:
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
            'LOCATION': 'awse_cache_table',
        }
    }

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            # 'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
    },
    'loggers': {
        'django': {
            'handlers': LOG_HANDLERS,
            'propagate': True,
        },
    }
}

GUNICORN_CONFIG = {
    'gunicorn': {
        'level': 'DEBUG',
        'class': 'logging.handlers.RotatingFileHandler',
        'formatter': 'verbose',
        'filename': '/var/log/gunicorn/awse.log',
        'maxBytes': 1024 * 1024 * 40,  # bytes * kilobytes * 40 megabytes
    },
}

if append_gunicorn_config:
    LOGGING['handlers'].update(GUNICORN_CONFIG)

STATICFILES_FINDERS = (
   'django.contrib.staticfiles.finders.FileSystemFinder',
   'django.contrib.staticfiles.finders.AppDirectoriesFinder',
   'compressor.finders.CompressorFinder',
)

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# COMPRESS_ENABLED = True
# COMPRESS_OFFLINE = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
# STATICFILES_DIRS = (
#    # os.path.join(BASE_DIR, '../awse/static'),
#    '/home/code/awse_web/awse/static',
# )

# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# 16.09.2021
