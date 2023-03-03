# Celery settings
# ------------------------------------------------------------------------------

from config.settings.utils import env

CELERY_TIMEZONE = 'UTC'
CELERY_BROKER_URL = env('CELERY_BROKER_URL', default=f"redis://redis:6379/2?client_class=django_redis.client.DefaultClient")

CELERY_TASK_ALWAYS_EAGER = env.bool('CELERY_TASK_ALWAYS_EAGER', default=True)
CELERY_TASK_EAGER_PROPAGATES = env.bool('CELERY_TASK_EAGER_PROPAGATES', default=True)
