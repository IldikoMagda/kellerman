
""" This file will process the uploaded file. Take it, open it, analise it """
import os
import pickle

import pandas as pd
#import xlrd
#mport csv

import config

#the folder where you find the uploaded files
UPLOAD_FOLDER = config.UPLOAD_FOLDER


def process_file():
    """ this function will find and open the file"""
    pathjoin = os.path.join
    for file in  os.listdir(UPLOAD_FOLDER):
        mydearfile = open(pathjoin(UPLOAD_FOLDER, file))
        return mydearfile

def actual_analysis():
    """ this is where the analysis run"""

    __author__= "Connor"

    rdf = process_file()
    percentages = []
    rdf = pd.read_csv((process_file()), sep="\t")
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

    test = df2.sort_values(['percentage_difference (%)'], ascending=True)
    pickle_out = open("test", "wb")
    pickle.dump(test, pickle_out)
    pickle_out.close()

    pickle_in = open("test", "rb")
    return pickle.load(pickle_in) 

def delete_foldercontent():
    """This function might be able to delete data from our folder"""
    folder = UPLOAD_FOLDER

    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
    try:
        if os.path.isfile(file_path):
            os.unlink(file_path)
    except Exception as e_ception:
        print(e_ception)

