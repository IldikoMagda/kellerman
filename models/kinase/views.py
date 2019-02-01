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
        return redirect(url_for('kinase.results', nameFilter=nameFilter))
    return render_template('kinase/index.html')

@kinase_blueprint.route('/results/<nameFilter>')
def results(nameFilter):
    # try:
    query = 'SELECT * FROM public."Kinase_table" WHERE "KINASE_NAME" = ' + nameFilter + ' ; '
    data = db.Query(query)
    return render_template('kinase/results.html', data=data)   
    # except:
    #     return "Sorry! No information available for that kinase!"