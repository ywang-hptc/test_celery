from celery import Task
import celery
from dcelery.celery_config import app
import logging

logging.basicConfig(
    filename="app.log",
    level=logging.ERROR,
    format="%(asctime)s %(levelname)s %(message)s",
)


class CustomTask(Task):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


# app.task = CustomTask


@app.task(
    base=CustomTask,
    queue="tasks",
    autoretry_for=(ConnectionError,),
    retry_kwargs={"max_retries": 3, "countdown": 5},
)
def my_task_3():
    raise ConnectionError("Connection Error Occurred...")
