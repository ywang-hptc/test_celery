from dcelery.celery_config import app
from celery import chain
import logging

logging.basicConfig(
    filename="app.log",
    level=logging.ERROR,
    format="%(asctime)s %(levelname)s %(message)s",
)


@app.task(queue="tasks", priority=10)
def add(x, y):
    return x + y


@app.task(queue="tasks", priority=10)
def multiple(result):
    if result == 5:
        raise ValueError("Value Error Occurred...")
    return result * 2


def run_task_chain():
    task_chain = chain(add.s(3, 2), multiple.s())
    if result := task_chain.apply_async():
        result.get()
