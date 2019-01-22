"""This file is to run the functions of the analysis site """
from flask import Blueprint, render_template


analysis_blueprint = Blueprint('analysis', __name__)


@analysis_blueprint.route('/', methods=['GET'])
def index():
    """ define the routes functions  """

    return render_template('analysis/index.html')
