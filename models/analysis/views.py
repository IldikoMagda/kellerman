<<<<<<< HEAD
from flask import Blueprint, render_template


analysis_blueprint= Blueprint('analysis', __name__)
=======
"""This file is to run the functions of the analysis site """
from flask import Blueprint, render_template


analysis_blueprint = Blueprint('analysis', __name__)
>>>>>>> f5809a5f98e4871d30f3dfbc6fbd3684ac838f37


@analysis_blueprint.route('/', methods=['GET'])
def index():
<<<<<<< HEAD
=======
    """ define the routes functions  """
>>>>>>> f5809a5f98e4871d30f3dfbc6fbd3684ac838f37

    return render_template('analysis/index.html')
