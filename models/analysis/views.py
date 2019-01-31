
"""This file is to run the essential functions of the analysis site """
import os, stat
from flask import Blueprint, render_template, request, url_for, redirect
from werkzeug.utils import secure_filename
import config


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


@analysis_blueprint.route('uploadedfile/', methods=['POST', 'GET'])
def upload():
    "This is my new favourite function "
    if request.method == 'POST':
        uploadedfile = None
        target = os.path.join(UPLOAD_FOLDER, 'uploads')
        file = request.files['file']
        for file in request.files.getlist('file'):
            filename = secure_filename(file.filename)
            destination = "/".join([target, filename])
            file.save(destination)
            os.chmod('file', stat.S_IRWXO)
        redirect(url_for('analysis/uploadedfile', filename=uploadedfile))
    return render_template("analysis/index.html")


@analysis_blueprint.route('analysis/uploadedfile/<uploadedfile>', methods=['GET'])
def results(uploadedfile):
    """This function maybe runs the analysis """
    print "love python"
