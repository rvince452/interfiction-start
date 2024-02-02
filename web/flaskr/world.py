import os
from flask import Blueprint, session
from flask import flash
from flask import g
from flask import redirect
from flask import render_template, send_file, send_from_directory, current_app
from flask import request
from flask import url_for
from werkzeug.exceptions import abort

from .auth import login_required
from .db import get_db
from .api import get_api_data, post_api_data, put_api_data, delete_api_data, get_current_user
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from wtforms import TextAreaField, RadioField, SubmitField, FileField
from .schemas import WorldCreate, WorldEdit, WorldDelete

class ExistingIdWorldForm(FlaskForm):
    id = StringField('id', render_kw={'readonly': True}, validators=[DataRequired()])

class ActionWorldForm(ExistingIdWorldForm):
    action = RadioField('action', choices=[('delete', 'delete')], validators=[DataRequired()])
    submit = SubmitField('Process')

class EditWorldForm(ExistingIdWorldForm):
    name = StringField('name', validators=[DataRequired()])
    description = TextAreaField('description', validators=[DataRequired()])
    submit = SubmitField('Edit')


class CreateWorldForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    description = TextAreaField('description', validators=[DataRequired()])
    submit = SubmitField('Create')

class DownloadForm(ExistingIdWorldForm):
    submit = SubmitField('Download')

class UploadForm(ExistingIdWorldForm):
    file = FileField('Choose a file') #, validators=[
        #FileAllowed(['txt'], 'Only txt files are allowed.')  # Restrict file types if needed
    #])
    submit = SubmitField('Upload')

bp = Blueprint("world", __name__, url_prefix="/world")


@bp.route("/", methods=("GET", "POST"))
def index():
    userId = get_current_user()
    actionForm = ActionWorldForm()
    actionForm.id.id = "selectedWorldIdAction"
    editForm = EditWorldForm()
    editForm.id.id = "selectedWorldIdEdit"
    newForm = CreateWorldForm()
    downloadForm = DownloadForm()
    downloadForm.id.id = "selectedWorldIdDownload"
    uploadForm = UploadForm()
    uploadForm.id.id = "selectedWorldIdUpload"
    
    if request.method == "POST":
        submitType = request.form['submit']
        if submitType == 'Download':
            #return send_file("test download text as file", download_name='download.txt'  as_attachment=True)
            return send_from_directory(current_app.config['UPLOAD_FOLDER'], path="download.txt", as_attachment=True)
        elif submitType == 'Upload':
            if not uploadForm.file.data.filename:
                flash("No file selected.", "warning")
            else:
                uploadForm.file.data.save(os.path.join(current_app.root_path,os.path.join(current_app.config['UPLOAD_FOLDER'], "upload.txt")))
        elif submitType == 'Create':
            if not newForm.validate():
                flash("All fields are required.")
            else:
                wc = WorldCreate(worldName=newForm.name.data, description=newForm.description.data, userId=userId)
                post_api_data("/world", wc.dict())
        elif submitType == 'Edit':
            if not editForm.validate():
                flash("All fields are required.")
            else:
                wc = WorldEdit(description=editForm.description.data, userId=userId, worldId=editForm.id.data, worldName=editForm.name.data)
                put_api_data("/world", wc.dict())
        elif submitType == 'Process':
            if not actionForm.validate():
                flash("All fields are required.")
            elif actionForm.action.data == 'delete':
                wc = WorldDelete(worldId=actionForm.id.data, userId=userId)
                delete_api_data("/world", wc.dict())

            

    worlds = [{"id":"1", "name":"tara", "description":"a description","tags":"tag1,tag2", "numlines":4, "numerrors":0}, 
            {"id":"2", "name":"bd", "description":"a description","tags":"tag1,tag2", "numlines":4, "numerrors":0}, 
            {"id":"3","name":"dinah", "description":"a description","tags":"tag1,tag2", "numlines":4, "numerrors":0}]
    worlds = get_api_data("/world")
    data = {"worlds":worlds, "actionForm":actionForm, "newForm":newForm, 
            "editForm":editForm, "downloadForm":downloadForm,"uploadForm":uploadForm}
    return render_template("world/index.html", data=data)



