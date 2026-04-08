from flask import jsonify
from flask import render_template
from flask import request

from . import app


@app.route("/", defaults={"js": "fetch"})
@app.route("/<any(xhr, jquery, fetch):js>")
def index(js):
    pass


@app.route("/add", methods=["POST"])
def add():
    pass
