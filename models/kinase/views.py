# import flask, blueprint, render template, request, url and redirect from flask
from flask import Flask, Blueprint, render_template, request,  url_for, redirect
# import database from common database 
import common.database as db

# name kinase blueprint
kinase_blueprint = Blueprint('kinase', __name__)

# make search box using request form
@kinase_blueprint.route('/', methods=['GET', 'POST'])
def index():       
    if request.method == 'POST':
        if request.form['name']:
            # make user input a variable named nameFilter
            nameFilter = request.form['name']
            # turn kinase name into uppercase 
            nameFilter = nameFilter.upper()
        # redirect to results page
        return redirect(url_for('kinase.results', nameFilter=str(nameFilter)))
    return render_template('kinase/index.html')

# make a results route that takes nameFilter as parameter 
@kinase_blueprint.route('/results/<nameFilter>')
def results(nameFilter):
    #try:
 
    # set kinase query 
    query =  'SELECT * FROM public."Kinase_table" WHERE "KINASE_NAME" = \'' + nameFilter + '\''
    # gather data from database 
    data = db.Query(query)
    # set query for inhibitor nae 
    inhibitor = 'SELECT "INHIBITOR_NAME" FROM public."KiInh_relation_table" WHERE "KINASE_NAME" = \'' + nameFilter + '\''
    data2 = db.Inhibitor(inhibitor)
    # set query for phosphosites 
    phosphosite = 'SELECT * FROM public."Phosphosite_table" WHERE "KINASE_NAME" = \'' + nameFilter + '\''
    data3 = db.Phospho(phosphosite)

    return render_template('kinase/results.html', data=data, data2=data2, data3=data3) 

    # except:
    #     return render_template ('kinase/error.html')

