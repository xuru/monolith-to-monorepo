"""
Base settings to build other settings files upon.
"""
import socket

import saml2  # noqa
import saml2.saml  # noqa
from django.utils.translation import gettext_lazy as _

from config.settings.utils import env, ROOT_DIR, APPS_DIR
from config.settings.components.version import *  # noqa

# GENERAL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = env.bool("DJANGO_DEBUG", False)

HOSTNAME = socket.gethostname()

# Local time zone. Choices are
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# though not all of them may be available with every OS.
# In Windows, this must be set to your system time zone.
TIME_ZONE = "UTC"
# https://docs.djangoproject.com/en/dev/ref/settings/#language-code
LANGUAGE_CODE = "en-us"
# https://docs.djangoproject.com/en/dev/ref/settings/#site-id
SITE_ID = 1
# https://docs.djangoproject.com/en/dev/ref/settings/#use-i18n
USE_I18N = True
# https://docs.djangoproject.com/en/dev/ref/settings/#use-l10n
USE_L10N = True
# https://docs.djangoproject.com/en/dev/ref/settings/#use-tz
USE_TZ = True
# https://docs.djangoproject.com/en/dev/ref/settings/#locale-paths
LOCALE_PATHS = [ROOT_DIR.path("locale")]
DATETIME_FORMAT = 'm/d/Y H:i:s'

# language translation with django-modeltranslation
# https://django-modeltranslation.readthedocs.io/en/latest/installation.html
LANGUAGES = (
    ('en', _('English')),
)

# URLS
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#root-urlconf
ROOT_URLCONF = "config.urls"
# https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
WSGI_APPLICATION = "config.wsgi.application"
ASGI_APPLICATION = "config.asgi.application"

ROOT_DOMAIN = "mtom.com"

# APPS
# ------------------------------------------------------------------------------
DJANGO_APPS: tuple[str, ...] = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    # http://whitenoise.evans.io/en/stable/django.html#using-whitenoise-in-development
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
)

THIRD_PARTY_APPS: tuple[str, ...] = (
    'rest_framework',
    'django_filters',
    'corsheaders',
    'rest_framework_jwt',
)

LOCAL_APPS: tuple[str, ...] = (
    'mtom.api.apps.ApiConfig',
    'mtom.authentication.apps.AuthenticationConfig',
    'mtom.core.apps.CoreConfig',
    'mtom.common.apps.CommonConfig',
    'mtom.tasks.apps.TasksConfig',
    'mtom.users.apps.UsersConfig',
    'mtom.errors.apps.ErrorsConfig',
    'mtom.testing_examples.apps.TestingExamplesConfig',
    'mtom.integrations.apps.IntegrationsConfig',
    'mtom.files.apps.FilesConfig',
    'mtom.emails.apps.EmailsConfig',
)

# https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# MIGRATIONS
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#migration-modules
MIGRATION_MODULES = {}  # type: ignore

# MIDDLEWARE
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# DATABASE
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
DATABASES = {
    # read os.environ['DATABASE_URL'] and raises ImproperlyConfigured exception if not found
    "default": env.db(default="postgres://root:root@postgres:5432/mtom-dev"),
}

# TEMPLATES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#templates
TEMPLATES = [
    {
        # https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-TEMPLATES-BACKEND
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        # https://docs.djangoproject.com/en/dev/ref/settings/#template-dirs
        "DIRS": [str(APPS_DIR.path("templates"))],
        "OPTIONS": {
            # https://docs.djangoproject.com/en/dev/ref/settings/#template-loaders
            # https://docs.djangoproject.com/en/dev/ref/templates/api/#loader-types
            "loaders": [  # type: ignore[index] # noqa F405
                (
                    "django.template.loaders.cached.Loader",
                    [
                        "django.template.loaders.filesystem.Loader",
                        "django.template.loaders.app_directories.Loader",
                        "jnt_admin_tools.template_loaders.Loader"
                    ],
                )
            ],
            # https://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
                "django_admin_env_notice.context_processors.from_settings",
            ],
        },
    }
]

# NOTIFICATIONS
# ------------------------------------------------------------------------------
DEFAULT_NOTIFS_MAX = 2
DEFAULT_NOTIFS_COOLDOWN = 600

# FIXTURES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#fixture-dirs
FIXTURE_DIRS = (str(APPS_DIR.path("fixtures")),)

# ADMIN
# ------------------------------------------------------------------------------
# Django Admin URL.
ADMINS = [("""Admin""", "admin@something.com"), ("""Primary""", "something@something.com")]
# https://docs.djangoproject.com/en/dev/ref/settings/#managers
MANAGERS = ADMINS


# django rest framework
# ------------------------------------------------------------------------------
REST_FRAMEWORK = {
    "PAGE_SIZE": 25,
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],
    'TEST_REQUEST_DEFAULT_FORMAT': 'json',
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    "DEFAULT_THROTTLE_RATES": {
        "anon_burst": "100/minute",
        "anon_sustained": "1000/day",
        "user_burst": "250/minute",
        "user_sustained": "2500/day",
    },
    "DEFAULT_FILTER_BACKENDS": ["django_filters.rest_framework.DjangoFilterBackend"],
    "EXCEPTION_HANDLER": "mtom.api.exception_handlers.drf_default_with_modifications_exception_handler",
}
APP_DOMAIN = env("APP_DOMAIN", default="http://localhost:8000")
