
""" This file will process the uploaded file. Take it, open it, analise it """
import os

import pandas as pd
import csv
import matplotlib as mat
mat.use('agg')
import matplotlib.pyplot as plt
import psycopg2 as pg
import pandas.io.sql as psql
import numpy as np
import math
from rq import Queue
from worker import conn
q = Queue(connection=conn)

import config

#the folder where you find the uploaded files
UPLOAD_FOLDER = config.UPLOAD_FOLDER
#the folder where the results can be saved-the full csv
DOWNLOAD_FOLDER = config.DOWNLOAD_FOLDER
#folder for static files on the site, the picture
STATIC_FOLDER = config.STATIC_FOLDER


def process_file():
    """ this function will find and open the file"""
    pathjoin = os.path.join
    for file in  os.listdir(UPLOAD_FOLDER):
        mydearfile = open(pathjoin(UPLOAD_FOLDER, file))
        return mydearfile


def create_csv(dataframeobject):
    """ This function turns pandas dataframe to CSV and saves
    to DOWNLOAD_FOLDER"""
    for file in os.listdir(UPLOAD_FOLDER):
        process_file()
        file_to_csv= file.to_csv(os.path.join(DOWNLOAD_FOLDER, r'results.csv'),
                                 sep='\t', encoding='utf-8')
        return file_to_csv
        
def actual_analysis():
    """ this is where the analysis of the uploaded tsv file run"""

    __author__ = "Connor and Ildiko "
    # let's try to send this entire function to a background process


    # setting input file as a variable to be easily used across the script
    input_file =process_file()

    # connect to our database and retrieve the necessary info
    connection = pg.connect("dbname=d71uh4v1fd2hq user=tdsneouerzmxkj password=92a500cb091fe70168b32c66fa6a3d6c376d467d57fb9b663eb5d13446ecb2e6 host=ec2-54-75-245-94.eu-west-1.compute.amazonaws.com")
    dataframe = psql.read_sql('SELECT * FROM public."Phosphosite_table"', connection)
    dataframe = dataframe[["GENE_NAME", "PHOSPHORYLATION_LOC", "KINASE_NAME"]]

    counter = 0
    # lists to extract the specific information that i want
    names = []
    residuelist = []
    kinase = []
    fclist = []

    # basically cleaning the raw data to make it easier to use
    with process_file() as data:           # this might not work as double opening
        data = csv.reader(data, delimiter='\t')
        next(data, None)
        for row in data:
            counter = counter + 1
            data = row[0:6]
            name = data[0].split("(")[0]
            residue1 = data[0].split("(")[1]
            residue = residue1.split(")")[0]
            fc = data[3]
            if "_" in name: 
                name = name.split("_")[0]
            for row in dataframe.itertuples():
                namez = row[1]
                resid = row[2]
                kin = row[3]
                if namez == name:
                    if residue == resid:
                        names.append(name)
                        residuelist.append(resid)
                        kinase.append(kin)
                        fclist.append(fc)
    # putting into pandas df
    df = pd.DataFrame()
    df["Names"] = names
    df["Residue"] = residuelist
    df["Kinase"] = kinase
    df["Fold Change"] = fclist 

    # part two starts here

    log2 = []
    df = df[df != 'inf']
    df = df[df != '0']
    df = df[df != '']
    df_cleaned = df.dropna(how='all')
    df_cleaned2 = df_cleaned.dropna()
    # again, cleaning the data
    # calcualting the log2 for the substrates
    for row in df_cleaned2.itertuples():
        name = row[1]
        residue = row [2]
        kinase = row[3]
        fc = float(row[4])
        twoval = math.log(fc, 2)
        log2.append(twoval)
    # creating a new column containing the log2(fc)
    df_cleaned2["log2(fc)"] = log2

    # calculating log2(fc) specific to kinases
    total = {}

    for row in df_cleaned2.itertuples():
        name = row[1]
        residue = row [2]
        kinase = row[3]
        fc = float(row[4])
        log2fc = float(row[5])
        if kinase == kinase:
            if kinase in total:
                total[kinase].append(log2fc)
            else:
                total[kinase] = [log2fc]

    # taking the mean value
    newdict = {}

    for key, value in total.items():
        s = sum(value)/len(value)
        newdict[key] = s 

    #open file and read with pandas with delimiter
    #rdf = pd.read_csv((process_file()), delim_whitespace=True)

    rdf = pd.read_csv(input_file, sep="\t")     
    nrdf = rdf.iloc[:,0:4]
    new = nrdf.replace(0, np.nan)
    new = new.dropna(how='all')
    new = new.dropna()

    # calcuating total log2(fc) mean value for all phosphosites
    another = []

    for d in new.itertuples():
        fc = str(d[4])
        if fc != 'inf':
            fc = math.log(float(fc), 2)
            another.append(fc)
            
    p = sum(another)/len(another)

    # total number of phosphosites specific to kinases, square rooted

    m = math.sqrt(len(df_cleaned2.index))

    # mean log2(fc) of all phosphosites 

    s = np.std(another)

    # allocating the z-scores to their kinase

    score = {}

    for key, value in newdict.iteritems():
        val = ((value - p)*m)/float(s)
        score[key] = val

    # putting values into a pandas df
    kinase = []
    scores = []

    for key, value in score.iteritems():
        kinase.append(key)
        scores.append(value)
        
    final = pd.DataFrame()
    final["Kinase"] = kinase
    final["z-Score"] = scores

    # putting kinases in order from lowest to highest z-score

    organised = final.sort_values(['z-Score'], ascending = True) 

    # indexing top ten z-scores

    top10 = organised.iloc[0:11,:]

    # saves data into csv files
    organised.to_csv('total_list.csv')
    top10.to_csv('topten_list.csv')

    organised.to_csv(os.path.join(DOWNLOAD_FOLDER, r'total_list.csv'),
                                 sep='\t', encoding='utf-8')
    top10.to_csv(os.path.join(DOWNLOAD_FOLDER, r'topten_list.csv'),
                                 sep='\t', encoding='utf-8')
    return top10

def create_fancybargraph(objectfromanalysis):
    """ this function uses matplotlib to create a graphical presentation about the uploaded file"""

    __author__="Connor"    
    funny_loop = True
    #putting values into a bar graph
    job = q.enqueue_call(process_file, args=None , timeout='1h')
    results = job.result
    if results != None:
        ax = results.plot.bar(x = "Kinase", rot=0, figsize=(7,3.5))
        # adjusting figure size
        plt.subplots_adjust(bottom=0.35, left=0.35)
        # setting title
        ax.set_title('Top Ten Downregulated Kinases')
        # removing figure legend
        ax.get_legend().remove()
        # setting y-label
        ax.set_ylabel('z-score')
        # adjusting x-axis labels to be more visible
        plt.setp(ax.get_xticklabels(), rotation=30, horizontalalignment='right')
        # converts into figure
        fig = ax.get_figure()
        # saves figure

        fig.savefig(os.path.join((STATIC_FOLDER), 'top_ten.png'))
        fig.savefig(os.path.join((DOWNLOAD_FOLDER),'top_ten.png'))
        ourprecious = 'top_ten.png'
        funny_loop == False
        return ourprecious
    else: 
        funny_loop == True

def delete_foldercontent():
    """This function might be able to delete data from our upload folder"""
    folder = UPLOAD_FOLDER

    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
    try:
        if os.path.isfile(file_path):
            os.unlink(file_path)

        
    except Exception as e_ception:
        print(e_ception)
