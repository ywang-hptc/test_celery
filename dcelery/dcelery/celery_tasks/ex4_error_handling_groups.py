from dcelery.celery_config import app
from celery import group
import logging

logging.basicConfig(
    filename="app.log",
    level=logging.ERROR,
    format="%(asctime)s %(levelname)s %(message)s",
)


@app.task(queue="tasks", priority=10)
def my_task(number: int):
    if number == 3:
        raise ValueError("Value Error Occurred...")
    return number * 2


def handle_result(result):
    if result.successful():
        print(f"Task Result: {result.get()}")
    elif result.failed() and isinstance(result.result, ValueError):
        print(f"Task Failed: {result.result}")
    elif result.status == "REVOKED":
        print("Task Revoked")


def run_tasks():
    task_group = group(my_task.s(i) for i in range(5))
    result_group = task_group.apply_async()
    result_group.get(disable_sync_subtasks=False, propagate=False)

    for result in result_group:
        handle_result(result)
