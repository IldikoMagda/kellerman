<<<<<<< HEAD
from flask import Blueprint, render_template

__author__ = 'Ildiko'


inhibitor_blueprint= Blueprint('inhibitor', __name__)


@inhibitor_blueprint.route('/', methods=['GET'])
def index():
=======
""" This file is to create functions and templates to inhibitor site"""
#import flask and render template
from flask import Blueprint, render_template

__author__ = 'Ildikoishavingfunwithpython'

inhibitor_blueprint= Blueprint('inhibitor', __name__)

@inhibitor_blueprint.route('/', methods=['GET'])
def index():
    """Functions of inhibitor site  and call for template"""
>>>>>>> f5809a5f98e4871d30f3dfbc6fbd3684ac838f37
    return render_template('inhibitor/index.html')
    