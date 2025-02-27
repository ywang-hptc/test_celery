from celery import group
from dcelery.celery_config import app
import time


app.conf.task_acks_late = True
app.conf.task_reject_on_worker_lost = True


@app.task(time_limit=10, queue="tasks")
def long_running_task():
    time.sleep(7)
    return "Task Completed"


def execute_task_examples():
    result = long_running_task.delay()
    try:
        task_result = result.get(timeout=4)
    except TimeoutError:
        print("Task Timeout Error Occurred...")
        result.revoke(terminate=True)
