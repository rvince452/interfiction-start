from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from werkzeug.exceptions import abort

from .auth import login_required
from .db import get_db

bp = Blueprint("game", __name__, url_prefix="/game")


@bp.route("/")
def index():
    """Show all the posts, most recent first."""
    data = [{"id":"1", "name":"tara", "description":"a description","tags":"tag1,tag2", "numlines":4, "numerrors":0}, 
            {"id":"2", "name":"bd", "description":"a description","tags":"tag1,tag2", "numlines":4, "numerrors":0}, 
            {"id":"3","name":"dinah", "description":"a description","tags":"tag1,tag2", "numlines":4, "numerrors":0}]
    return render_template("game/index.html", worlds=data)

