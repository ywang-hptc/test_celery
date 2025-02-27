"""
* * * * *
| | | | |
| | | | +---- Day of the week (range: 0-6, 0 standing for Sunday)
| | | +------ Month of the year (range: 1-12)
| | +-------- Day of the month (range: 1-31)
| +---------- Hour (range: 0-23)
+------------ Minute (range: 0-59)

Example:
* * * * *          Every minute
*/5 * * * *        Every 5 minutes
30 * * * *         Every hour at the 30th minute
0 9 * * *          9:00 AM every day
0 9 * * 1          9:00 AM every Monday
0 0 1,15 * *       Midnight on the 1st and 15th of every month
0 20,23 * * *      8:00 PM and 11:00 PM every day
0 0 1-7 * *        Midnight on the first 7 days of every month
0 0/2 * * *        Every 2 hours
0 */2 * * *        Every 2 hours
0 0-8/2 * * *      Every 2 hours from midnight to 8:00 AM
0 0 1 1 *          Midnight on January 1st
0 0 1 jan *        Midnight on January 1st
0 0 1 1 Mon        Midnight on the first Monday of January
"""

from datetime import timedelta
from dcelery.celery_config import app
from celery.schedules import crontab

app.conf.beat_schedule = {
    "task1": {
        "task": "dcelery.celery_tasks.ex13_task_schedule_crontab.test1",
        "schedule": crontab(minute="*/2"),
        "kwargs": {"foo": "barbar"},
        "args": (2, 5),
        "options": {"queue": "tasks", "priority": 5},
    },
}


@app.task(queue="tasks")
def test1(a, b, foo):
    print(f"Running Task 1 with crontab...,  {a=} {b=} {foo=}")
