
""" This file will process the uploaded file... One day """

#import os
from flask import render_template
import config


DOWNLOAD_FOLDER = config.DOWNLOAD_FOLDER

def process_file(filename):
    """ this function will take a file and run analysis function on it and
    and return the results"""
    actual_analysis(filename)
    print 'results shit'
    return render_template('analysis/results.html')

def actual_analysis(filename):
    """ this is where the actual python analysis will wun"""
    #open with etc etc ...

    #return redirect(url_for('analysis.html', filename=filename))
