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
    #query = db.Query(query)
    #if nameFilter in query:
        # set kinase query 
    query =  'SELECT * FROM public."Kinase_table" WHERE "CAP_KINASE_NAME" LIKE \'' "%" + nameFilter +  "%" '\''
    # gather data from database 
    data = db.Query(query)
    # set query for inhibitor nae 
    inhibitor = 'SELECT "INHIBITOR_NAME" FROM public."KiInh_relation_table" WHERE "KINASE_NAME" LIKE \'' "%" + nameFilter +  "%" '\''
    data2 = db.Inhibitor(inhibitor)
    # set query for phosphosites on target genes
    phosphosite = 'SELECT * FROM public."Phosphosite_table" WHERE "KINASE_NAME" LIKE \''"%" + nameFilter +  "%" '\''
    data3 = db.Phospho(phosphosite)
    # set query for phosphosites on selected kinase
    phosphosite = 'SELECT * FROM public."Phosphosite_table" WHERE "GENE_NAME" LIKE \''"%" + nameFilter +  "%" '\''
    data4 = db.Phospho(phosphosite)
    return render_template('kinase/results.html', data=data, data2=data2, data3=data3, data4=data4) 
    #except:
      #  return render_template ('kinase/error.html')

@kinase_blueprint.route('/inhib_info/')
def inhib_info():
    query = 'SELECT * FROM public."Inhibitor_table"  WHERE "INHIBITOR_NAME" LIKE \'' "%" + data2 +  "%" '\''
    data = db.Query(query)
    return render_template('inhibitor/results.html', data=data) 