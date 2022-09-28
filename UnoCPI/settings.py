"""
Django settings for UnoCPI project.
Generated by 'django-admin startproject' using Django 2.1.
For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""


import os
from django.contrib.messages import constants as messages
import dj_database_url
from django.urls import reverse_lazy

SESSION_EXPIRE_AT_BROWSER_CLOSE = True
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ')z8d*5_%@v!h@bl3-vl2gn@mwcd@6vlz061+b=o02jc5@2r1gg'

# SECURITY WARNING: don't run with debug turned on in production!
SECURE_SSL_REDIRECT = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
DEBUG = os.environ.get('DEBUG', False)


ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'account',
    'home',
    'partners',
    'projects',
    'university',
    'bootstrapform',
    'django_filters',
    'import_export',
    'logentry_admin',
    'simple_history',
    'wagtail.contrib.forms',
    'wagtail.contrib.redirects',
    'wagtail.embeds',
    'wagtail.sites',
    'wagtail.users',
    'wagtail.snippets',
    'wagtail.documents',
    'wagtail.images',
    'wagtail.search',
    'wagtail.admin',
    'wagtail.core',
    'session_security',
    'modelcluster',
    'taggit',
    'storages',
    'django.contrib.admin',
    ]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'wagtail.core.middleware.SiteMiddleware',
    'wagtail.contrib.redirects.middleware.RedirectMiddleware',
    'simple_history.middleware.HistoryRequestMiddleware',
    'crum.CurrentRequestUserMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'session_security.middleware.SessionSecurityMiddleware',
]

SESSION_SECURITY_EXPIRE_AFTER=1800
SESSION_SECURITY_WARN_AFTER=5
SESSION_EXPIRE_AT_BROWSER_CLOSE=True
ROOT_URLCONF = 'UnoCPI.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'home.context_processors.global_settings',
                'home.views.resourceData',
            ],
        },
    },
]

WSGI_APPLICATION = 'UnoCPI.wsgi.application'


# Database

# https://docs.djangoproject.com/en/2.1/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD':os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': os.environ.get('DB_PORT'),
    }
}

# Thousand separator
USE_THOUSAND_SEPARATOR = True



##Extending the user model to home

AUTH_USER_MODEL = 'home.User'

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Chicago'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')

MESSAGE_TAGS = {
    messages.DEBUG: 'alert-info',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)

# Update database configuration with $DATABASE_URL.
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

###Email settings
LOGIN_REDIRECT_URL = reverse_lazy('/')
LOGIN_URL = reverse_lazy('account:loginPage')
#LOGOUT_REDIRECT_URL = reverse_lazy('logout')


## Sample Import files download source location, DONOT DELETE
## MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
## MEDIA_URL = '/media/'

##
EMAIL_HOST = os.environ.get('MAILGUN_SMTP_SERVER')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
EMAIL_PORT = os.environ.get('MAILGUN_SMTP_PORT')
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'UNO Community Partnership Initiative <partnerships@unomaha.edu>'


# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/

#STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
#STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'
# Internationalization

WAGTAIL_SITE_NAME = 'UNO-CPI'


GOOGLE_MAPS_API_KEY = os.environ.get('GOOGLE_MAPS_API_KEY')

AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
AWS_ACCESS_KEY_ID=os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY=os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

MEDIA_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

SAML_FOLDER = os.path.join(BASE_DIR, 'saml_uno')
SAML_HOST_URL = os.environ.get('SAML_HOST_URL')
APP_ENV = os.environ.get('APP_ENV')

# when using other websites that track visitors or use their iframe on your website.
SECURE_REFERRER_POLICY = "strict-origin-when-cross-origin"

# Necessary to show Iframe from your own server (such as PDFs on your website)
X_FRAME_OPTIONS = 'SAMEORIGIN'

try:
    from local_settings import *
except ImportError:
    pass