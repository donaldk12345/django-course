from pathlib import Path
from django.utils.translation import gettext_lazy as _
from decouple import config
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-w&eu7(1$@)@n7&aoic9200h*gyjt2=ov&u=cur+3=j&r%renn5'

# Mettre à True en local pour le dev, passera à False sur le VPS avec Certbot
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tailwind',
    'theme',
    'polls',
]

TAILWIND_APP_NAME = 'theme'

INTERNAL_IPS = [
    "127.0.0.1",
]

# Configurez la bonne ligne selon votre environnement de dev actuel
NPM_BIN_PATH = r"C:\nvm4w\nodejs\npm.cmd"  # Windows
# NPM_BIN_PATH = "/usr/bin/npm"          # Décocher sur Ubuntu / VPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Gestion optimale des fichiers statiques
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',  # INDISPENSABLE pour détecter et changer la langue (FR/EN)
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'courseproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Permet d'avoir un dossier global pour vos pages HTML
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',  # Permet d'accéder aux outils de langues dans les templates
            ],
        },
    },
]

WSGI_APPLICATION = 'courseproject.wsgi.application'

# Database
# Database configurée pour PostgreSQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'db_blog_sante',       
        'USER': 'postgres',       
        'PASSWORD': 'titanic',
        'HOST': 'localhost',             
        'PORT': '5432',
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = config('EMAIL_HOST', default='ssl0.ovh.net')
EMAIL_PORT = config('EMAIL_PORT', default=465, cast=int)
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
EMAIL_USE_SSL = config('EMAIL_USE_SSL', default=True, cast=bool)
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

LANGUAGE_CODE = 'fr' 

TIME_ZONE = 'Africa/Douala'  

USE_I18N = True

USE_TZ = True

LANGUAGES = [
    ('fr', _('Français')),
    ('en', _('Anglais')),
]

LOCALE_PATHS = [
    BASE_DIR / 'locale',
]


STATIC_URL = 'static/'

STATIC_ROOT = BASE_DIR / 'staticfiles'

STATICFILES_DIRS = [
    BASE_DIR / 'theme' / 'static',
]


MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


if DEBUG:
    STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
else:
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
