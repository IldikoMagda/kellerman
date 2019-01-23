""" This file is to create functions and templates to inhibitor site"""
#import flask and render template
from flask import Blueprint, render_template

__author__ = 'Ildikoishavingfunwithpython'

inhibitor_blueprint= Blueprint('inhibitor', __name__)

@inhibitor_blueprint.route('/', methods=['GET'])
def index():
    """Functions of inhibitor site  and call for template"""
    return render_template('inhibitor/index.html')
    