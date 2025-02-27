from datetime import timedelta
from dcelery.celery_config import app

app.conf.beat_schedule = {
    "task1": {
        "task": "dcelery.celery_tasks.ex11_task_scheduling.test1",
        "schedule": timedelta(seconds=5),
    },
    "task2": {
        "task": "dcelery.celery_tasks.ex11_task_scheduling.test2",
        "schedule": timedelta(seconds=10),
    },
}


@app.task(queue="tasks")
def test1():
    print("Running Task 1...")


@app.task(queue="tasks")
def test2():
    print("Running Task 2...")
