from flask import Blueprint, render_template

__author__ = 'Ildiko'


inhibitor_blueprint= Blueprint('inhibitor', __name__)


@inhibitor_blueprint.route('/', methods=['GET'])
def index():
    return render_template('inhibitor/index.html')
    