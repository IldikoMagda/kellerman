<<<<<<< HEAD
from flask import Flask, render_template
=======
"""" This file is to collect the entire app together. Define the routes and register them """

#import flask and render template
from flask import Flask, render_template
# use models directory to run blueprint functions
>>>>>>> f5809a5f98e4871d30f3dfbc6fbd3684ac838f37
from models.kinase.views import kinase_blueprint
from models.inhibitor.views import inhibitor_blueprint
from models.analysis.views import analysis_blueprint

<<<<<<< HEAD
app = Flask(__name__)
app.config.from_object('config')


@app.route("/")
def home():
    return render_template('index.html')


app.register_blueprint(kinase_blueprint, url_prefix="/kinase")
app.register_blueprint(inhibitor_blueprint, url_prefix="/inhibitor")
app.register_blueprint(analysis_blueprint, url_prefix="/analysis")
=======
APP = Flask(__name__)
APP.config.from_object('config')

@APP.route("/")
def home():

    """ Description: Home Route that renders the index template        """
    return render_template('index.html')

APP.register_blueprint(kinase_blueprint, url_prefix="/kinase")
APP.register_blueprint(inhibitor_blueprint, url_prefix="/inhibitor")
APP.register_blueprint(analysis_blueprint, url_prefix="/analysis")
>>>>>>> f5809a5f98e4871d30f3dfbc6fbd3684ac838f37
