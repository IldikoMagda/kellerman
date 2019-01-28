#from flask library import blueprint, render template and request methods 
from flask import Blueprint, render_template, request
import common.database as db


kinase_blueprint = Blueprint('kinase', __name__)
@kinase_blueprint.route('/', methods=['GET', 'POST'])
def index():
    kinase_name=None   
    if request.method == 'POST':
        kinase_name= request.form['name']
        query = 'SELECT kinase_id, kinase_name, family, inhibitor FROM public.kinase'
    elif request.method == 'GET':
        data = db.Query(query)
    return render_template('kinase/index.html', data=data, content_type='application/json')
