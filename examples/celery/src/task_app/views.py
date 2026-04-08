from celery.result import AsyncResult
from flask import Blueprint
from flask import request

from . import tasks

bp = Blueprint("tasks", __name__, url_prefix="/tasks")


@bp.get("/result/<id>")
def result(id: str) -> dict[str, object]:
    pass


@bp.post("/add")
def add() -> dict[str, object]:
    pass


@bp.post("/block")
def block() -> dict[str, object]:
    pass


@bp.post("/process")
def process() -> dict[str, object]:
    pass
