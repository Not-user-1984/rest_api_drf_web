from pathlib import Path
import environ
import os

BASE_DIR = Path(__file__).resolve().parent.parent

ENV_FILE_PATH = BASE_DIR.parent / 'src' / '.env'

env = environ.Env()
environ.Env.read_env(ENV_FILE_PATH)

SECRET_KEY = env('SECRET_KEY')

DEBUG = True

# Константы для моделей
MIN_RATING = env.int('MIN_RATING', default=1)
MAX_RATING = env.int('MAX_RATING', default=5)

ALLOWED_HOSTS = []


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'dogs_api',
    'ninja',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'config.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_DB', 'dogs_db'),
        'USER': os.getenv('POSTGRES_USER', 'dogs_user'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD', 'dogs_password'),
        'HOST': os.getenv('POSTGRES_HOST', 'db'),
        'PORT': os.getenv('POSTGRES_PORT', '5432'),
    }
}

# # Настройки для тестов
# if os.environ.get("DJANGO_ENV") == "test":
#     DATABASES = {
#         "default": {
#             "ENGINE": "django.db.backends.sqlite3",
#             "NAME": ":memory:",
#         }
#     }
#     PASSWORD_HASHERS = [
#         "django.contrib.auth.hashers.MD5PasswordHasher",
#     ]
#     MIDDLEWARE = [
#         middleware
#         for middleware in MIDDLEWARE
#         if middleware != "django.middleware.csrf.CsrfViewMiddleware"
#     ]

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
