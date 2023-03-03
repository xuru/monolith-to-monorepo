import sys

from celery import shared_task


@shared_task
def debug_task(self):
    sys.stdout.write(f"Request: {self.request!r}")
