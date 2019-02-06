
""" This file will process the uploaded file. Take it, open it, analise it """
import os

import pandas as pd
from pandas import DataFrame
import matplotlib as mat
mat.use('agg')
import matplotlib.pyplot as plt

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
        file_to_csv= file.to_csv(os.path.join(DOWNLOAD_FOLDER,r'results.csv'),
                                 sep='\t', encoding='utf-8')
        return file_to_csv
        
def actual_analysis():
    """ this is where the analysis of the uploaded tsv file run"""

    __author__ = "Connor"

    percentages = []

    #open file and read with pandas with delimiter
    rdf = pd.read_csv((process_file()), delim_whitespace=True)
    df = rdf.dropna(how="all", axis=1)
    df1 = df.loc[(df!=0).any(1)]

    df1.columns = ["Substrate", "control_conc_mean", "treated_conc_mean",
                   "fold_change", "p-value", "controlCV", "treatedCV"]

    for index, row in df1.iterrows():
        control = float(row["control_conc_mean"])
        treated = float(row["treated_conc_mean"])
        first = control - treated
        if control != float(0):
            first = float(control - treated)
            second = float(first/control)
            third = second*100
            percentages.append(float(third))
        if control == float(0):
            if treated > 0:
                control = 0.0000000000001
                first = float(control - treated)
                second = float(first/control)
                third = second*100
            percentages.append(float(0))

    df1["percentage_difference (%)"] = percentages

    df2 = df1[['Substrate', 'control_conc_mean', 'treated_conc_mean',
               'fold_change', 'p-value', 'percentage_difference (%)', 'controlCV', 'treatedCV']]

    sort = df2.sort_values(['percentage_difference (%)'], ascending=True)
    test = sort.iloc[0:10:]
    return test

def create_fancybargraph(objectfromanalysis):
    """ this function uses matplotlib to create a graphical presentation about the uploaded file"""

    __author__="Connor"    
    inter = objectfromanalysis[['Substrate','percentage_difference (%)']]
    new = inter.iloc[0:10, :]

    ax = new.plot.bar(x='Substrate', y='percentage_difference (%)', rot=0)
    ax.set_title('Top Ten Downregulated Kinases')

    ax.get_legend().remove()
    ax.set_ylabel('percentage_difference (%)')

    plt.setp(ax.get_xticklabels(), rotation=30, horizontalalignment='right')

    my_file = ax.get_figure()
    my_file.savefig(os.path.join((STATIC_FOLDER), 'my_file.png'))
    ourprecious = 'my_file.png'
    return ourprecious

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
