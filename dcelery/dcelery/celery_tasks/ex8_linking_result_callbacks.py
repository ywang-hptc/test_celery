import sys
from celery import group
from dcelery.celery_config import app
import time


app.conf.task_acks_late = True
app.conf.task_reject_on_worker_lost = True


@app.task(queue="tasks")
def long_running_task():
    raise ValueError("Value Error Occurred...")


@app.task(queue="tasks")
def process_task_result(result):
    sys.stdout.write(f"Task Result: {result}\n")
    sys.stdout.flush()


@app.task(queue="tasks")
def process_error(result, exc, traceback):
    sys.stdout.write(">>>>>>>")
    sys.stdout.write(f"Task Error: {result}\n")
    sys.stdout.write("<<<<<<<")
    sys.stdout.flush()


def execute_task_examples():
    long_running_task.apply_async(
        link=[
            process_task_result.s(),
        ],
        link_error=process_error.s(),
    )
