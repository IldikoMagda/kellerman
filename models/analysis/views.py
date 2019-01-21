from flask import Blueprint, render_template


analysis_blueprint= Blueprint('analysis', __name__)


@analysis_blueprint.route('/', methods=['GET'])
def index():

    return render_template('analysis/index.html')
