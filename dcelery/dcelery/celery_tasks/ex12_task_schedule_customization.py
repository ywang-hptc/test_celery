from datetime import timedelta
from dcelery.celery_config import app

app.conf.beat_schedule = {
    "task1": {
        "task": "dcelery.celery_tasks.ex12_task_schedule_customization.test1",
        "schedule": timedelta(seconds=5),
        "kwargs": {"foo": "bar"},
        "args": (1, 2),
        "options": {"queue": "tasks", "priority": 5},
    },
    "task2": {
        "task": "dcelery.celery_tasks.ex12_task_schedule_customization.test2",
        "schedule": timedelta(seconds=10),
    },
}


@app.task(queue="tasks")
def test1(a, b, foo):
    print(f"Running Task 1...,  {a=} {b=} {foo=}")


@app.task(queue="tasks")
def test2():
    print("Running Task 2...")
