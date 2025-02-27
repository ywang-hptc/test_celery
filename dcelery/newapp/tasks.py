# from time import sleep
# from celery import shared_task


# @shared_task(queue="celery")
# def tp1():
#     sleep(3)
#     print("Task 1")
#     return "Task 1"


# @shared_task(queue="celery:1")
# def tp2():
#     sleep(3)
#     print("Task 2")
#     return "Task 2"


# @shared_task(queue="celery:2")
# def tp3():
#     sleep(3)
#     print("Task 3")
#     return "Task 3"


# @shared_task(queue="celery:3")
# def tp4():
#     sleep(3)
#     print("Task 4")
#     return "Task 4"
