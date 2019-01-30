from flask import Flask, render_template
from models.kinase.views import kinase_blueprint
from models.inhibitor.views import inhibitor_blueprint
from models.analysis.views import analysis_blueprint


APP = Flask(__name__)
APP.config.from_object('config')

@APP.route("/")
def index():

    """ Description: Home Route that renders the index template        """
    return render_template('index.html')

APP.register_blueprint(kinase_blueprint, url_prefix="/kinase")
APP.register_blueprint(inhibitor_blueprint, url_prefix="/inhibitor")
APP.register_blueprint(analysis_blueprint, url_prefix="/analysis")
