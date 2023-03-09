from config.settings.environments.local import *  # noqa


CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
    }
}


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3"
    },
    "timescale": {
        "ENGINE": "django.db.backends.sqlite3"
    }
}
