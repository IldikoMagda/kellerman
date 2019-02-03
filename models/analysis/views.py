
"""This file is to run the essential functions of the analysis site """
import os, stat
from flask import Blueprint, render_template, request, url_for, redirect
from werkzeug.utils import secure_filename
import config

#from flask_wtf import FlaskForm
#from wtforms import StringField, SubmitField
#from wtforms.validators import Required

__author__ = "Ildiko"

analysis_blueprint = Blueprint('analysis', __name__) #bluprint to wrap up the code


UPLOAD_FOLDER = config.UPLOAD_FOLDER #contains abs path to uploaded file

ALLOWED_EXTENSIONS = {'tsv'} #specify the file extension allowed
def allowed_file(filename):
    """ allowed extensions to upload""" # somehow works in google chrome not in firefox....
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@analysis_blueprint.route('/', methods=['POST', 'GET'])
def index():
    """ Main site of analysis with the form"""
    return render_template("analysis/index.html")


@analysis_blueprint.route('upload/', methods=['POST', 'GET'])
def upload():
    "This is my new favourite function "
    if request.method == 'POST':
        uploadedfile = None
        target = os.path.join(UPLOAD_FOLDER)
        #if not os.path.isdir(target):
            #os.mkdir(target, mode= 0775)
            #os.chmod('target', stat.S_IRWXO)
        file = request.files['file']
        for file in request.files.getlist('file'):
            uploadedfile = secure_filename(file.filename)
            #destination = "/".join([target, uploadedfile])
            file.save(os.path.join(UPLOAD_FOLDER, uploadedfile))
            #os.chmod('file', stat.S_IRWXO)
        redirect(url_for('analysis.uploaded', file=file))
    return render_template("analysis/uploadedfile.html")


@analysis_blueprint.route('uploaded/', methods=['GET', 'POST'])
def uploaded():
    """This function maybe runs the analysis """
    return render_template("analysis/uploadedfile.html")

