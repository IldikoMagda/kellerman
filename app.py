from flask import Flask, render_template
from models.kinase.views import kinase_blueprint
from models.inhibitor.views import inhibitor_blueprint
from models.analysis.views import analysis_blueprint

app = Flask(__name__)
app.config.from_object('config')


@app.route("/")
def home():
    return render_template('index.html')


app.register_blueprint(kinase_blueprint, url_prefix="/kinase")
app.register_blueprint(inhibitor_blueprint, url_prefix="/inhibitor")
app.register_blueprint(analysis_blueprint, url_prefix="/analysis")