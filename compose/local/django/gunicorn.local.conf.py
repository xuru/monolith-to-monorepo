import gunicorn
from uvicorn.workers import UvicornWorker

gunicorn.SERVER = "undisclosed"
bind = "0.0.0.0:8000"


class DjangoWorker(UvicornWorker):
    CONFIG_KWARGS = {"lifespan": "off"}


# worker processes
workers = 2
timeout = 60
threads = 2
reload = True
reload_extra_files = ["compose/local/django/gunicorn.local.conf.py"]
loglevel = "info"
worker_class = "__config__.DjangoWorker"
