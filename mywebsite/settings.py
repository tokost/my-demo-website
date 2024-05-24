##import environ
import os
from pathlib import Path
##import dj_database_url
from dotenv import load_dotenv
from decouple import config     # funkcia používanú na čítanie konfiguračných premenných
                                # z premenných prostredia alebo súboru .env

# Initialize environment variables
##env = environ.Env(DEBUG=(bool, False))

# Load environment variables from .env file
##load_dotenv(dotenv_path=os.path.join(BASE_DIR, '.env'))
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

# Load environment variables from .env file
##load_dotenv(os.path.join(BASE_DIR, ".env"))

# Project environment
PROJECT_ENV = os.getenv("PROJECT_ENV", "development")

# Secret key
DJANGO_SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'default-secret-key')
#print("DJANGO_SECRET_KEY: ", os.getenv('DJANGO_SECRET_KEY'))

# Debug mode
DEBUG = os.getenv('DEBUG', 'False') == 'True'

# Allowed hosts
##ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', 'localhost').split(',')
####ALLOWED_HOSTS = [config('WEB_HOST', default='localhost'), 'localhost']
#ALLOWED_HOSTS = ['my-demo-website-fmnd.onrender.com', 'localhost', '127.0.0.1']
ALLOWED_HOSTS = [os.getenv('RENDER_SERVICE_NAME') + '.onrender.com', 'localhost']
#print(f"ALLOWED_HOSTS: {ALLOWED_HOSTS}")  # Print the ALLOWED_HOSTS value to debug

#Example of using the service name
#SERVICE_NAME = os.getenv('RENDER_SERVICE_NAME', 'my-demo-website-fmnd.onrender.com')
SERVICE_NAME = os.getenv('RENDER_SERVICE_NAME', 'default-service-name')

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'crispy_bootstrap5',
    'allauth',
    'allauth.account',
    'rest_framework',
    'ckeditor',
    'website.apps.WebsiteConfig',
    'users.apps.UsersConfig',
    'whitenoise.runserver_nostatic',
    'debug_toolbar',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'mywebsite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

'''
DATABASES = {
    'default': dj_database_url.config(
        default=f'postgres://{env("POSTGRES_USER")}:{env("POSTGRES_PASSWORD")}@{env("POSTGRES_HOST")}:{env("POSTGRES_PORT")}/{env("POSTGRES_NAME")}'
    )
}
'''
'''
DATABASES = {
    'default': {
        'ENGINE': env('POSTGRES_ENGINE', default='django.db.backends.postgresql_psycopg2'),
        'NAME': env('POSTGRES_NAME', default='my_web_db'),
        'USER': env('POSTGRES_USER', default='postgres'),
        'PASSWORD': env('POSTGRES_PASSWORD', default='postgres'),
        'HOST': env('POSTGRES_HOST', default='localhost'),
        'PORT': env('POSTGRES_PORT', default='5432'),
    }
}
'''

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('POSTGRES_NAME'),
        'USER': config('POSTGRES_USER'),
        'PASSWORD': config('POSTGRES_PASSWORD'),
        'HOST': config('POSTGRES_HOST', 'localhost'),
        'PORT': '5432',
    }
}


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

# Logging configuration
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'DEBUG',
    },
}

LANGUAGE_CODE = 'sk-SK'             # Specifies the language code for the application.
TIME_ZONE = 'Europe/Bratislava'     # 'UTC' (Coordinated Universal Time)
USE_I18N = True                     # Specifies the default time zone for the application. 
USE_TZ = True                       # This setting affects how Django interprets and 
                                    # displays date and time information.
AUTH_USER_MODEL = 'users.CustomUser'

LOGIN_REDIRECT_URL = '/'
ACCOUNT_LOGOUT_REDIRECT = '/'
ACCOUNT_SESSION_REMEMBER = True
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
SITE_ID = 1

CRISPY_ALLOWED_TEMPLATE_PACKS = 'bootstrap5'
CRISPY_TEMPLATE_PACK = 'bootstrap5'

STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'mediafiles'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

WHITENOISE_USE_FINDERS = True

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ],
}

# Session settings
##SESSION_ENGINE = 'django.contrib.sessions.backends.db'  # Use database-backed sessions
SESSION_ENGINE = 'django.contrib.sessions.backends.cache'  # Use cache-backed sessions
# SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'  # Use combined database and cache-backed sessions
