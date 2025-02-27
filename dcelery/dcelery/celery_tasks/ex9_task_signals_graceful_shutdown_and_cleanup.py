from celery.signals import task_failure
from dcelery.celery_config import app
import sys


@app.task(queue="tasks")
def cleanup_failed_task(task_id, *args, **kwargs):
    sys.stdout.write(f"Clean up task ID: {task_id}\n")


@app.task(queue="tasks")
def my_task():
    raise ValueError("Task Failed")


@task_failure.connect(sender=my_task)
def handle_task_failure(sender=None, task_id=None, **kwargs):
    cleanup_failed_task.delay(task_id)


def run_task():
    my_task.apply_async()
