"""
This is a django-split-settings main file.
For more information read this:
https://github.com/sobolevn/django-split-settings
https://sobolevn.me/2017/04/managing-djangos-settings
To change settings file:
`DJANGO_ENV=local python manage.py runserver`
"""
import os
from os import environ
from pathlib import Path

import django_stubs_ext
from split_settings.tools import include, optional

from config.settings.utils import ROOT_DIR

"""
Monkeypatching Django, so stubs will work for all generics,
see: https://github.com/typeddjango/django-stubs
"""
django_stubs_ext.monkeypatch()

# Managing environment via `DJANGO_ENV` variable:
environ.setdefault('DJANGO_ENV', 'local')
ENV = environ.get("DJANGO_ENV").lower()

from config.settings.utils import env  # noqa

# Load dot env file if it exists
# ------------------------------------------------------------------------------
DOT_ENV_FILE = env("DJANGO_DOT_ENV_FILE", default=None)
READ_ENV_FILE = env.bool("DJANGO_READ_DOT_ENV_FILE", default=True)

# resolve dot file
if READ_ENV_FILE is True:
    if DOT_ENV_FILE:
        dot_file = Path(DOT_ENV_FILE)
        env.read_env(str(dot_file))

_base_settings = [
    'components/common.py',
    'components/authentication.py',
    'components/cache.py',
    'components/email.py',
    'components/celery.py',
    'components/secrets.py',
    'components/security.py',
    'components/storage.py',
]

# Now load up settings for the specific environment and overide if needed.
_base_settings += [
    # Select the right env:
    optional(f'environments/{ENV}.py'),
]

# Include settings:
include(*_base_settings)
