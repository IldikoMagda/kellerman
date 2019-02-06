
"""This file is to run the essential functions of the analysis site """
import os
from flask import Blueprint, render_template, request, url_for, redirect
from werkzeug.utils import secure_filename
import config
from models.analysis import process_file
import matplotlib as mat
mat.use('agg')
import matplotlib.pyplot as plt


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
    """This function uploads the file to uploads folder """

    if request.method == 'POST':
        uploadedfile = None
        file = request.files['file']        
        # if file sent save it to upload_folder and redirect to analysis:
        for file in request.files.getlist('file'):
            uploadedfile = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_FOLDER, uploadedfile))
            return redirect(url_for('analysis.uploaded', uploadedfile=uploadedfile))
    return render_template("analysis/index.html")


@analysis_blueprint.route('uploaded/', methods=['GET', 'POST'])
def uploaded():
    """This function maybe runs the analysis """
    # take the file and analise
    result_object = process_file.actual_analysis()
    #delete the files in the upload folder
    process_file.delete_foldercontent()
    #create our precious picture 
    ourprecious = process_file.create_fancybargraph(result_object)

    return render_template("analysis/results.html",
                            tables=[result_object.to_html(classes='data', header="true")],
                            ourprecious=ourprecious)
