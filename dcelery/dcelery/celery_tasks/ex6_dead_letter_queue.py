from celery import group
from dcelery.celery_config import app


app.conf.task_acks_late = True
app.conf.task_reject_on_worker_lost = True


@app.task(queue="tasks")
def my_task(z):
    try:
        if z == 2:
            raise ValueError("Value Error Occurred...")
    except Exception as e:
        handle_failed_task.apply_async(args=(z, str(e)))
        raise ValueError("Value Error Occurred...")


@app.task(queue="dead_letter_queue")
def handle_failed_task(z, exception):
    return "Custom logic to process"


def run_task_group():
    task_group = group(my_task.s(i) for i in range(5))
    result_group = task_group.apply_async()
