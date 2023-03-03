from environ import Env, Path

# Build paths inside the project like this: BASE_DIR.joinpath('some')
# `pathlib` is better than writing: dirname(dirname(dirname(__file__)))
ROOT_DIR = Path(__file__) - 3  # (project/config/settings/utils.py - 3 = project/)
APPS_DIR = ROOT_DIR.path("mtom")

# Loading `.env` files
# See docs: https://github.com/joke2k/django-environ
env = Env()

# https://django-environ.readthedocs.io/en/latest/tips.html#escape-proxy
env.escape_proxy = True
