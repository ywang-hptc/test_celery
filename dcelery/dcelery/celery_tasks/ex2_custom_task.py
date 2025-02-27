from celery import Task
from dcelery.celery_config import app
import logging

logging.basicConfig(
    filename="app.log",
    level=logging.ERROR,
    format="%(asctime)s %(levelname)s %(message)s",
)


# class CustomTask(Task):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)

#     def on_failure(self, exc, task_id, args, kwargs, einfo):
#         if isinstance(exc, ConnectionError):
#             logging.error(f"Error: {exc} - Admin Notified")
#             return "Connection Error Occurred..."
#         else:
#             print("{0!r} failed: {1!r}".format(task_id, exc))


# app.task = CustomTask


# @app.task(queue="tasks")
# def my_task_2():
#     try:
#         raise ConnectionError("Connection Error Occurred...")
#     except ConnectionError as e:
#         logging.error(f"Error: {e}")
#         raise ConnectionError("Connection Error Occurred...")
