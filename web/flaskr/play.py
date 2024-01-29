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

bp = Blueprint("play", __name__, url_prefix="/play")


@bp.route("/")
def index():
    name = "Space Station Sally"
    location = "Loading Bay"
    choices = [("Continue","Continue"),("Skip","Skip")]
    oitems = [("Wrench","Hammer"),("Pistol","Raygun")]
    text = """
    Hello, and welcome to Space Station Sally! You are Sally, a space station
        mechanic. You have been called to the loading bay to fix a broken
        hyperdrive. You have a wrench and a pistol in your inventory. What do
        you do?

    """
    status = {"name":name, "location":location, "choices":choices, "oitems":oitems
              ,"text":text}
    return render_template("play/index.html", data=status)


