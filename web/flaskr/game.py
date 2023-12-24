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
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from wtforms import TextAreaField, RadioField, SubmitField, FileField

bp = Blueprint("game", __name__, url_prefix="/game")

class ActionGameForm(FlaskForm):
     id = StringField('id', render_kw={'readonly': True}, validators=[DataRequired()])
     action = RadioField('action', choices=[('resume','resume'),('quit', 'quit')], validators=[DataRequired()])
     submit = SubmitField('Process')


@bp.route("/", methods=("GET", "POST"))
def index():
    actionForm = ActionGameForm()

    if request.method == "POST":
        if not actionForm.validate_on_submit():
            if actionForm.action.data == "resume":
                return redirect(url_for("play.index"))
            elif actionForm.action.data == "quit":
                return redirect(url_for("index"))
            else:
                flash("Invalid action")
        else:
            flash("Invalid form")


    games = [
        {"id":"1", "name":"Keep on the Borderlands", "user":"player 1","progress":"Tavern"}, 
        {"id":"2", "name":"UFO", "user":"player 2","progress":"Moonbase Alpha"},
        {"id":"3", "name":"House", "user":"player 3","progress":"Basement"},
    ]
    #games = get_api_data("/world")
    data = {"games":games, "actionForm":actionForm}
    return render_template("game/index.html", data=data)

