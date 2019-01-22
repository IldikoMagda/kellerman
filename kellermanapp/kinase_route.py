# define a route called 'protein' which accepts a protein name parameter
@app.route('/kinases/<kinase_name>')
def kinases(kinase_name):
   # load kinase data from TSV file into pandas dataframe with kinase name as index
	df = pd.read_csv(kinase_table_filename,sep='\t',index_col=1)
    kinase_name = kinase_name.upper()  # ensure name is in capital letters
	try:  # try to extract row for specified kinase
		row = df.loc[kinase_name]
		# if kinase is found, return some information about it
		return render_template('kinase_view.html', name=kinase_name, gene_name=row.gene_name, \
        subcelullar_location=row.subcelullar_location, image=row.Image_URL)
	except:
		# if protein is not found a key error is thrown and we end up here
		return "Sorry! We can't find any information about a kinase called %s." % kinase_name

	

	

