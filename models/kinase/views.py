from flask import Flask, render_template, url_for, redirect
import pandas as pd

# import libraries needed create and process forms
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required

# create a flask application object
app = Flask(__name__)
# we need to set a secret key attribute for secure forms
app.config['SECRET_KEY'] = 'change this unsecure key'

# tell code where to find kinase information
kinase_table_filename = 'kinase_table.tsv'

# create a class to define the form
class QueryForm(FlaskForm):
	kinase_name = StringField('Enter a valid UniProt kinase name:', validators=[Required()])
	submit = SubmitField('Submit')

# define a route called 'kinase' which accepts a kinase name parameter
@app.route('/kinases/<kinase_name>',  methods=['GET','POST'])
def kinases(kinase_name):
	form = QueryForm()  # create form to pass to template
	kinase_name = None
	if form.validate_on_submit():
		kinase_name = form.kinase_name.data
		print('\n\n\n'+kinase_name+'\n\n\n')
		return redirect(url_for('kinase', kinase_name = kinase_name))
	return render_template('kinase.index.html', form=form, kinase_name=kinase_name)

   # load kinase data from TSV file into pandas dataframe with kinase name as index
	df = pd.read_csv(kinase_table_filename,sep='\t',index_col=1)
	kinase_name = kinase_name.upper()  # ensure name is in capital letters
	try: # try to extract row for specified kinase
		row = df.loc[kinase_name]
		# if kinase is found, return some information about it
		return render_template('kinase.index.html', name=kinase_name, gene_name=row.gene_name, \
        subcelullar_location=row.subcelullar_location, image=row.Image_URL)
	except:
		# if kinase is not found a key error is thrown and we end up here
		return "Sorry! We can't find any information about a kinase called %s." % kinase_name


	

