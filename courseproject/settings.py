from pathlib import Path
from django.utils.translation import gettext_lazy as _

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

# Internationalization (i18n) configuré pour le bilinguisme au Cameroun
LANGUAGE_CODE = 'fr'  # Langue par défaut à l'ouverture du site

TIME_ZONE = 'Africa/Douala'  # Fuseau horaire du Cameroun

USE_I18N = True

USE_TZ = True

LANGUAGES = [
    ('fr', _('Français')),
    ('en', _('Anglais')),
]

# Le dossier où Django va stocker les dictionnaires de traduction (.po)
LOCALE_PATHS = [
    BASE_DIR / 'locale',
]

# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'

# Dossier final de production où collectstatic va compiler le CSS Tailwind purifié
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Indique à Django d'inclure les fichiers compilés par l'application theme de Tailwind
STATICFILES_DIRS = [
    BASE_DIR / 'theme' / 'static',
]


MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Gestion intelligente du stockage statique (Dev vs Production)
if DEBUG:
    STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
else:
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
