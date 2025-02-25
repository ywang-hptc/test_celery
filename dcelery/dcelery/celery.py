import os
from celery import Celery
from kombu import Queue, Exchange
from time import sleep

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dcelery.settings")
app = Celery("dcelery")
app.config_from_object("django.conf:settings", namespace="CELERY")

app.conf.task_queues = (
    [
        Queue(
            "tasks",
            Exchange("tasks"),
            routing_key="tasks",
            queue_arguments={"x-max-priority": 10},
        )
    ],
)
app.conf.task_acks_late = True
app.conf.task_default_priority = 5
app.conf.worker_prefetch_multiplier = (
    1  # Force the worker to only select one job at a time
)
app.conf.worker_concurrency = 1  # Force the worker to only process one job at a time


# app.conf.task_routes = {
#     "newapp.tasks.task1": {"queue": "queue1"},
#     "newapp.tasks.task2": {"queue": "queue2"},
# }
@app.task(queue="tasks", priority=2)
def t1():
    sleep(3)
    print("Task 1")
    return "Task 1"


@app.task(queue="tasks", priority=5)
def t2():
    sleep(3)
    print("Task 2")
    return "Task 2"


@app.task(queue="tasks", priority=8)
def t3():
    sleep(3)
    print("Task 3")
    return "Task 3"


# app.conf.broker_transport_options={
#     "priority_steps": range(10),
#     "sep":":",
#     "queue_order_strategy":"priority",
# }
app.autodiscover_tasks()
