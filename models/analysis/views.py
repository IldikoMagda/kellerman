"""This file is to run the essential functions of the analysis site """
import os
from flask import Flask, Blueprint, render_template, request, url_for, redirect
from werkzeug.utils import secure_filename
import config

__author__ = "Ildiko"

analysis_blueprint = Blueprint('analysis', __name__) #create the blueprint to wrap up the entire code

UPLOAD_FOLDER = config.UPLOAD_FOLDER #contains abs path to uploaded file

ALLOWED_EXTENSIONS = {'tsv'} #specify the file extension allowed
def allowed_file(filename):
    """ allowed extensions to upload""" # somehow works in google chrome not in firefox....
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@analysis_blueprint.route('/', methods=('POST','GET'))
def index():
    return render_template("analysis/index.html")


@analysis_blueprint.route('uploadedfile/', methods=('POST','GET'))
def upload():
    "This is my new favourite function "
    target = os.path.join(UPLOAD_FOLDER, '/uploads')
    if not os.path.isdir(target):
        os.mkdir(target)
    file = request.files['file']
    for file in request.files.getlist('file'):
        filename = secure_filename(file.filename)
        destination = "/".join([target, filename])
        file.save(destination)
    # add your custom code to check that the uploaded file is a valid image and not a malicious file (out-of-scope for this post)
        

    return render_template('analysis/uploadedfile.html')

