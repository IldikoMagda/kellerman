from flask import Flask, Blueprint, render_template, request,  url_for, redirect
import sys
import common.database as db
import json

kinase_blueprint = Blueprint('kinase', __name__)
@kinase_blueprint.route('/', methods=['GET', 'POST'])
def index():       
    if request.method == 'POST':
        if request.form['name']:
            nameFilter = request.form['name']
            nameFilter = nameFilter.upper()
        return redirect(url_for('kinase.results', nameFilter=nameFilter))
    return render_template('kinase/index.html')

@kinase_blueprint.route('/results/<nameFilter>')
def results(nameFilter):
    # try:
    if nameFilter == '':
        #query =  'SELECT * FROM public."Kinase_table" '
        #data = db.Query(query)
        data = db.Query(query)
    #query = 'SELECT * FROM test_schema.test_table WHERE kinase_n LIKE "%' + nameFilter + '%"'
    query = 'SELECT * FROM public."Kinase_table" ' # WHERE "KINASE_NAME" = "%' + nameFilter + '%"' 
  
    data = db.Query(query)
    return render_template('kinase/results.html', data=data, content_type='application/json')   
    
    
    
    
    
    #except:
     #   return render_template ('kinase/error.html')
    #    return "Sorry! No information available for that kinase!"