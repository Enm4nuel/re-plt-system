"""
Django settings for re_sys project.

Generated by 'django-admin startproject' using Django 3.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '7qk21&4apcnvj1b07p8@3*16^41no^afzfaq(dd_x^#_#6073='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'plantillas',
    'datos',
    'urlparams'
]

MIDDLEWARE = [
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 're_sys.urls'

URL_PARAMS_CONF = 'my_custom.url_conf'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
<<<<<<< HEAD
            'C:/Users/Leonor Fischer/Documents/re-sys-main/home/templates/',
            'C:/Users/Leonor Fischer/Documents/re-sys-main/plantillas/templates/',
            'C:/Users/Leonor Fischer/Documents/re-sys-main/datos/templates/'
            ],
=======
            os.path.join(BASE_DIR, 'home/templates'),
            os.path.join(BASE_DIR, 'plantillas/static')
        ],
>>>>>>> master
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

WSGI_APPLICATION = 're_sys.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
#DATABASE_ROUTERS = ['plantillas.routers.PlantillaRouter']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

"""
'plantilla_db': {
        'NAME': 'FACTURA',
        'ENGINE': 'mssql',
        'USER': 'Data_Editor',
        'PASSWORD': 'jr03124300',
        'HOST': '172.24.1.39',
        'PORT': '1433',
        'OPTIONS': {'driver': 'ODBC Driver 17 for SQL Server',}
    },
"""


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'es-es'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'home/static'),
    os.path.join(BASE_DIR, 'plantillas/static'),
    os.path.join(BASE_DIR, 'datos/static')
    )