from celery import shared_task


class CeleryQueue:
    HIGH = "high"  # high priority, run ASAP
    MEDIUM = "medium"  # medium priority, run soon
    LOW = "low"  # low priority, run whenever


@shared_task(queue=CeleryQueue.LOW)
def dev_server_handle_xxxx_event(event):
    pass
