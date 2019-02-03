from flask import Flask, Blueprint, render_template, request,  url_for, redirect
import sys
import common.database as db
import json

inhibitor_blueprint= Blueprint('inhibitor', __name__)
@inhibitor_blueprint.route('/', methods=['GET','POST'])
def index():      
    if request.method == 'POST':
        if request.form['name']:
            nameFilter = request.form['name']
        return redirect(url_for('inhibitor.results', nameFilter=nameFilter))
    return render_template('inhibitor/index.html')

## Do we want to search inhibitor by inhibitor name?
## Or do we want by kinase name to retrieve corresponding inhibitor infamition?

@inhibitor_blueprint.route('/results/<nameFilter>')
def results(nameFilter):
    # try:
    query = 'SELECT * FROM public."Inhibitor_table" WHERE "INHIBITOR_NAME" = ' + nameFilter + ' ; '
    data = db.Query(query)
    return render_template('inhibitor/results.html', data=data) 
    # except:
    #     return "Sorry! No information available for that kinase!"