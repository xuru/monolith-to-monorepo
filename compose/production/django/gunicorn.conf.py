import gunicorn
from uvicorn.workers import UvicornWorker


class DjangoWorker(UvicornWorker):
    CONFIG_KWARGS = {"lifespan": "off"}


gunicorn.SERVER = "undisclosed"
bind = "0.0.0.0:8000"

# worker processes
timeout = 0
worker_class = "__config__.DjangoWorker"
