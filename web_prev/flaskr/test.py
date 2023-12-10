from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from werkzeug.exceptions import abort
import requests


bp = Blueprint("test", __name__)


@bp.route("/test/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        
        return redirect(url_for("test.index"))
    #data = requests.get(url).json()
    data = [{"id":"1", "name":"tara", "description":"a description","tags":"tag1,tag2", "numlines":4, "numerrors":0}, 
            {"id":"2", "name":"bd", "description":"a description","tags":"tag1,tag2", "numlines":4, "numerrors":0}, 
            {"id":"3","name":"dinah", "description":"a description","tags":"tag1,tag2", "numlines":4, "numerrors":0}]
    return render_template("test/index.html", worlds=data)

    
