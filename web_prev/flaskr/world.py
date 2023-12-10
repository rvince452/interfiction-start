from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db
import requests
import os

bp = Blueprint("world", __name__)

API_URL = os.environ['API_URL']

@bp.route("/world/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        
        name = request.form["name"]
        description = request.form["description"]
        error = None
        if not name:
            error = "Name is required."
        elif not description:
            error = "Description is required."

        if error is not None:
            flash(error)
        else:
            url = API_URL + "/items"
            data = {"name":name, "description":description}
            #requests.post(url, json=data)
            return redirect(url_for("world.index"))

    """Show all the posts, most recent first."""
    url = API_URL + "/items"
    #data = requests.get(url).json()
    data = [{"id":"1", "name":"tara", "description":"a description","tags":"tag1,tag2", "numlines":4, "numerrors":0}, 
            {"id":"2", "name":"bd", "description":"a description","tags":"tag1,tag2", "numlines":4, "numerrors":0}, 
            {"id":"3","name":"dinah", "description":"a description","tags":"tag1,tag2", "numlines":4, "numerrors":0}]
    return render_template("world/index.html", worlds=data)


def get_post(id, check_author=True):
    """Get a post and its author by id.

    Checks that the id exists and optionally that the current user is
    the author.

    :param id: id of post to get
    :param check_author: require the current user to be the author
    :return: the post with author information
    :raise 404: if a post with the given id doesn't exist
    :raise 403: if the current user isn't the author
    """
    post = (
        get_db()
        .execute(
            "SELECT p.id, title, body, created, author_id, username"
            " FROM post p JOIN user u ON p.author_id = u.id"
            " WHERE p.id = ?",
            (id,),
        )
        .fetchone()
    )

    if post is None:
        abort(404, f"Post id {id} doesn't exist.")

    if check_author and post["author_id"] != g.user["id"]:
        abort(403)

    return post


@bp.route("/world/create", methods=("GET", "POST"))
@login_required
def create():
    """Create a new post for the current user."""
    if request.method == "POST":
        title = request.form["title"]
        body = request.form["body"]
        error = None

        if not title:
            error = "Title is required."

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                "INSERT INTO post (title, body, author_id) VALUES (?, ?, ?)",
                (title, body, g.user["id"]),
            )
            db.commit()
            return redirect(url_for("world.index"))

    return render_template("world/create.html")


@bp.route("/<int:id>/update", methods=("GET", "POST"))
@login_required
def update(id):
    """Update a post if the current user is the author."""
    post = get_post(id)

    if request.method == "POST":
        title = request.form["title"]
        body = request.form["body"]
        error = None

        if not title:
            error = "Title is required."

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                "UPDATE post SET title = ?, body = ? WHERE id = ?", (title, body, id)
            )
            db.commit()
            return redirect(url_for("blog.index"))

    return render_template("blog/update.html", post=post)


@bp.route("/<int:id>/delete", methods=("POST",))
@login_required
def delete(id):
    """Delete a post.

    Ensures that the post exists and that the logged in user is the
    author of the post.
    """
    get_post(id)
    db = get_db()
    db.execute("DELETE FROM post WHERE id = ?", (id,))
    db.commit()
    return redirect(url_for("blog.index"))
