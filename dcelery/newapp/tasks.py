from time import sleep
from celery import shared_task


@shared_task
def tp1(queue="celery"):
    sleep(3)
    print("Task 1")
    return "Task 1"


@shared_task
def tp2(queue="celery:1"):
    sleep(3)
    print("Task 2")
    return "Task 2"


@shared_task
def tp3(queue="celery:2"):
    sleep(3)
    print("Task 3")
    return "Task 3"


@shared_task
def tp4(queue="celery:3"):
    sleep(3)
    print("Task 4")
    return "Task 4"
