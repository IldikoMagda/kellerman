###This file is to define routes ###


from flask import Flask 
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    """THIS IS OUR HOME PAGE""" 
    return "this is home page for now but will become our template"

##all routes will have their CSS template to handle HTML

@app.route('/kinases')
def kinases():
    """THIS IS WHERE THE SEARCH KINASES COULD BE"""
    return "template + plug-in for search in kinases"




@app.route('/kinases/<kinasesname>')
def kinases(kinasesname):
    """THIS IS WHERE THE DETAILS ABOUT THE KINASES WILL BE 
    THEY SEARCHED FOR"""

    return "what details do we want to include?"





@app.route('/upload')
def upload():
    """THIS IS WHERE THE USER CAN UPLOAD THEIR PROTEOMICS DATA"""
    return "we need a method for upload file"




@app.route('/upload/results')
def upload(results):
    """ THIS IS WHERE THEY SEE THE RESULT OF THE ANALYSIS"""
    return "we need to think what this actually will be"
