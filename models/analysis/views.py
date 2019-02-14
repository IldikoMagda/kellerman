
"""This file is to run the essential functions of the analysis site """
import os

import zipfile
from flask import Blueprint, render_template, request, url_for, redirect, send_file
from werkzeug.utils import secure_filename
import config
from models.analysis import process_file
import matplotlib as mat
mat.use('agg')

__author__ = "Ildiko"

analysis_blueprint = Blueprint('analysis', __name__) #bluprint to wrap up the code

#contains abs path to uploaded file
UPLOAD_FOLDER = config.UPLOAD_FOLDER
#the folder where the results can be saved-the full csv
DOWNLOAD_FOLDER = config.DOWNLOAD_FOLDER

ALLOWED_EXTENSIONS = {'tsv'} #specify the file extension allowed
def allowed_file(filename):
        """ allowed extensions to upload"""
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@analysis_blueprint.route('/', methods=['POST', 'GET'])
def index():
    """ Main site of analysis with the form"""
    return render_template("analysis/index.html")

@analysis_blueprint.route('upload/', methods=['POST', 'GET'])
def upload():
    """This function uploads the file to the uploads folder """
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
    """This function runs the analysis and returns the results """
    result_object = process_file.actual_analysis() #all file processing function runs from process_file.py
    ourprecious = process_file.create_fancybargraph(result_object) # graphical representation of the results 
    return render_template("analysis/results.html",
                           tables=[result_object.to_html(classes='data', header="true")],
                           ourprecious=ourprecious)
 
@analysis_blueprint.route('/dowload_all', methods=['GET', 'POST'])
def download_all():
    """This is the function which dowloads the results for the user"""

    zipf = zipfile.ZipFile('Results.zip','w', zipfile.ZIP_DEFLATED) #create zipfile with all related result files
    for root, dirs, files in os.walk('downloads/'):
        for file in files:
            zipf.write('downloads/'+file)
    zipf.close()
    return send_file('Results.zip',
                     mimetype='zip',
                     attachment_filename='Results.zip',
                     as_attachment=True)
