from dcelery.celery_config import app
import logging

logging.basicConfig(
    filename="app.log",
    level=logging.ERROR,
    format="%(asctime)s %(levelname)s %(message)s",
)


# @app.task(queue="tasks", priority=10)
# def my_task():
#     try:
#         raise ConnectionError("Connection Error Occurred...")
#     except ConnectionError as e:
#         logging.error(f"Error: {e}")
#         raise ConnectionError("Connection Error Occurred...")
