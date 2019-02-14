
""" This file will process the uploaded file. Take it, open it, analise it """
import os
import csv
import pandas as pd
import psycopg2 as pg
import config
import matplotlib as mat
mat.use('agg')
import matplotlib.pyplot as plt

import numpy as np
import math


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
    """ This function turns a file to CSV and saves
    to DOWNLOAD_FOLDER"""
    for file in os.listdir(UPLOAD_FOLDER):
        process_file()
        file_to_csv= file.to_csv(os.path.join(DOWNLOAD_FOLDER, r'results.csv'),
                                 sep='\t', encoding='utf-8')
        return file_to_csv
        
def actual_analysis():
    """ this is where the analysis of the uploaded tsv file run"""

    __author__ = "Connor and Ildiko "
    
    pathjoin = os.path.join
    # lists to extract the specific information that i want
    names = []
    residuelist = []
    kinase = []
    fclist = []

    for file in  os.listdir(UPLOAD_FOLDER):
        data = open(pathjoin(UPLOAD_FOLDER, file), 'r')
        data = csv.reader(data, delimiter='\t')
        next(data, None)
        for row in data:
            data = row[0:6]
        if "(" in data[0]:
            name = data[0].split("(")[0]
            residue1 = data[0].split("(")[1]
            residue = residue1.split(")")[0]
            fc = data[3]
        else:
            pass
        if "_" in name:
            name = name.split("_")[0]
        if residue != "None":
            if residue != "inf":
                names.append(name)
                residuelist.append(residue)
                fclist.append(fc)

        # putting into pandas df
        df2 = pd.DataFrame()
        df2 = pd.DataFrame(columns=['gene', 'residue', 'fold_change'])
        df2["gene"] = names
        df2["residue"] = residuelist
        df2["fold_change"] = fclist

        genename = names
        location = residuelist

        conn_string = ("host='ec2-54-75-245-94.eu-west-1.compute.amazonaws.com' dbname='d71uh4v1fd2hq' user='tdsneouerzmxkj' password='92a500cb091fe70168b32c66fa6a3d6c376d467d57fb9b663eb5d13446ecb2e6'")
        conn = pg.connect(conn_string)
        cur = conn.cursor()
        query =('SELECT "KINASE_NAME", "GENE_NAME", "RESIDUE" FROM public."Phosphosite_table" WHERE "GENE_NAME" LIKE any(%s) and "RESIDUE" LIKE any(%s)',\
                str((genename, location)))

        df = pd.read_sql(query, con= pg.connect(conn_string), params={'name':'value'})
        conn.close()
        result = pd.merge(df, df2, left_on=('gene','residue'))
        result['fold_change'].dropna()
        d = result.replace("inf", np.nan)
        e = d.replace("0", np.nan)
        f = e.replace("", np.nan)
        new = f.dropna(how='all')
        df3 = new.dropna()
        log2 = []
        for row in df3.itertuples():
            name = row[1]
            residue = row [2]
            kinase = row[3]
            fc = float(row[4])
            twoval = math.log(fc, 2)
            log2.append(twoval)

        df3["log2(fc)"] = log2

        total = {}
        for row in df3.itertuples():
            name = row[2]
            residue = row [3]
            kinase = row[1]
            fc = float(row[4])
            log2fc = float(row[5])
            if kinase == kinase:
                if kinase in total:
                    total[kinase].append(log2fc)
                else:
                    total[kinase] = [log2fc]

        newdict = {}
        for key, value in total.iteritems():
            s = sum(value)/len(value)
            newdict[key] = s

        rdf = pd.read_csv(data, sep="\t")    
        nrdf = rdf.iloc[:,0:4]
        new = nrdf.replace(0, np.nan)
        new = new.dropna(how='all')
        new = new.dropna()

        another = []

        for d in new.itertuples():
            fc = str(d[4])
            if fc != 'inf':
                fc = math.log(float(fc), 2)
                another.append(fc)
                
        p = sum(another)/len(another)

        m = math.sqrt(len(df3.index))

        s = np.std(another)

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
        final["z-score"] = scores

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

    ax = objectfromanalysis.plot.bar(x= "Kinase", rot=0, figsize=(7,3.5))
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

    return ourprecious

def delete_foldercontent():
    """This function might be able to delete data from our upload folder"""
    folder = UPLOAD_FOLDER  # delete folder content, later can be more general for all the folders
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
    try:
        if os.path.isfile(file_path):
            os.unlink(file_path)
    except Exception as e_ception:
        print(e_ception)
