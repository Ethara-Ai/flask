import sqlite3
from datetime import datetime

import click
from flask import current_app
from flask import g


def get_db():
    """Connect to the application's configured database. The connection
    is unique for each request and will be reused if this is called
    again.
    """
    pass


def close_db(e=None):
    """If this request connected to the database, close the
    connection.
    """
    pass


def init_db():
    """Clear existing data and create new tables."""
    pass


@click.command("init-db")
def init_db_command():
    """Clear existing data and create new tables."""
    pass


sqlite3.register_converter("timestamp", lambda v: datetime.fromisoformat(v.decode()))


def init_app(app):
    """Register database functions with the Flask app. This is called by
    the application factory.
    """
    pass
