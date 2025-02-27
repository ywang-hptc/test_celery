import os
from celery import Celery
from kombu import Queue, Exchange
from time import sleep

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dcelery.settings")
app = Celery("dcelery")
app.config_from_object("django.conf:settings", namespace="CELERY")

app.conf.task_queues = [
    Queue(
        "tasks",
        Exchange("tasks"),
        routing_key="tasks",
        queue_arguments={"x-max-priority": 10},
    ),
    Queue("dead_letter_queue", routing_key="dead_letter_queue"),
]


app.conf.task_acks_late = True
app.conf.task_default_priority = 5
app.conf.worker_prefetch_multiplier = (
    1  # Force the worker to only select one job at a time
)
app.conf.worker_concurrency = 1  # Force the worker to only process one job at a time

base_dir = os.getcwd()
task_folder = os.path.join(base_dir, "dcelery", "celery_tasks")
if os.path.exists(task_folder) and os.path.isdir(task_folder):
    task_modules = []
    for filename in os.listdir(task_folder):
        if filename.startswith("ex") and filename.endswith(".py"):
            module_name = f"dcelery.celery_tasks.{filename[:-3]}"
            module = __import__(module_name, fromlist=["*"])
            for name in dir(module):
                obj = getattr(module, name)
                if callable(obj) and name.startswith("my_task"):
                    task_modules.append(f"{module_name}.{name}")
    app.autodiscover_tasks(task_modules)
