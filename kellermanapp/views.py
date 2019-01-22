###This file is to define routes ###


from flask import Flask 
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    """THIS IS OUR HOME PAGE""" 
    return "this is home page for now but will become our template"

##all routes will have their CSS template to handle HTML

@app.route('/kinases')
def kinases():
    """THIS IS WHERE THE SEARCH KINASES COULD BE"""
    return "template + plug-in for search in kinases"




@app.route('/kinases/<kinasesname>')
def kinases(kinasesname):
    """THIS IS WHERE THE DETAILS ABOUT THE KINASES WILL BE 
    THEY SEARCHED FOR"""

    return "what details do we want to include?"

# define a route called 'protein' which accepts a protein name parameter
@app.route('/protein/<protein_name>')
def protein(protein_name):

	# load protein data from TSV file into pandas dataframe with protein name as index
	df = pd.read_csv(protein_table_filename,sep='\t',index_col=1)

	protein_name = protein_name.upper()  # ensure name is in capital letters

	try:  # try to extract row for specified protein
		row = df.loc[protein_name]
		# if protein is found, return some information about it
		return render_template('protein_view.html', name=protein_name, fullname=row.Full_name, \
			mass=row.Mass, function=row.GO_molecular_function, image=row.Image_URL)
	except:
		# if protein is not found a key error is thrown and we end up here
		return "We can't find any information about a protein called %s." % protein_name



@app.route('/upload')
def upload():
    """THIS IS WHERE THE USER CAN UPLOAD THEIR PROTEOMICS DATA"""
    return "we need a method for upload file"




@app.route('/upload/results')
def upload(results):
    """ THIS IS WHERE THEY SEE THE RESULT OF THE ANALYSIS"""
    return "we need to think what this actually will be"
