from celery import shared_task


@shared_task
def task1():
    print("Task 1")
    return


@shared_task
def task2():
    print("Task 2")
    return
