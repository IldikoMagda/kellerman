# import flask, blueprint, render template, request, url and redirect from flask
from flask import Flask, Blueprint, render_template, request,  url_for, redirect
import sys
# import database from common file 
import common.database as db
import json

# name inhibitor blueprint route 
inhibitor_blueprint= Blueprint('inhibitor', __name__)
@inhibitor_blueprint.route('/', methods=['GET','POST'])
def index():      
    if request.method == 'POST':
        if request.form['name']:
            # give a variable for user input 
            nameFilter = request.form['name']
        return redirect(url_for('inhibitor.results', nameFilter=nameFilter))
    return render_template('inhibitor/index.html')

# create route for reuslts page that takes nameFilter as parameter 
@inhibitor_blueprint.route('/results/<nameFilter>')
def results(nameFilter):
    # try:
    # query the database for inhibitor information inhibitor table 
    query = 'SELECT * FROM public."Inhibitor_table" WHERE "INHIBITOR_NAME" = \'' + nameFilter + '\''
    data = db.Query(query)
    return render_template('inhibitor/results.html', data=data) 
    # except:
    #     return "Sorry! No information available for that kinase!"