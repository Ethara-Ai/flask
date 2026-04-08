import time

from celery import shared_task
from celery import Task


@shared_task(ignore_result=False)
def add(a: int, b: int) -> int:
    pass


@shared_task()
def block() -> None:
    pass


@shared_task(bind=True, ignore_result=False)
def process(self: Task, total: int) -> object:
    pass
