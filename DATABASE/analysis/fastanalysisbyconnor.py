import time

start = time.time()

import pandas as pd 
import csv
import matplotlib as mat
import matplotlib.pyplot as plt
import psycopg2 as pg
import pandas.io.sql as psql
import multiprocessing
import numpy as np
import math

input_file = "mux.tsv"

names = []
residuelist = []
kinase = []
fclist = []

with open(input_file, "r") as data:
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

df2 = pd.DataFrame()
df2["gene"] = names
df2["residue"] = residuelist
df2["fold_change"] = fclist             
            
genename = names
location = residuelist

connection = pg.connect("dbname=d71uh4v1fd2hq user=tdsneouerzmxkj \
password=92a500cb091fe70168b32c66fa6a3d6c376d467d57fb9b663eb5d13446ecb2e6 \
host=ec2-54-75-245-94.eu-west-1.compute.amazonaws.com")

cur = connection.cursor()

result = cur.execute('SELECT "KINASE_NAME", "GENE_NAME", "RESIDUE" FROM public."Phosphosite_table" WHERE "GENE_NAME" LIKE any(%s) and "RESIDUE" LIKE any(%s)',\
            (genename, location))

df = pd.DataFrame(cur.fetchall())
df.columns = ['kinase', 'gene', 'residue']

connection.close()

result = pd.merge(df,df2, on = ('gene','residue'), how = "left")

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
    name = row[1]
    residue = row [2]
    kinase = row[0]
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
    
rdf = pd.read_csv(input_file, sep="\t")     
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

organised = final.sort_values(['z-score'], ascending = True) 

# indexing top ten z-scores

top10 = organised.iloc[0:11,:]

# putting values into a bar graph

ax = top10.plot.bar(x = "Kinase", rot=0, figsize=(7,3.5))

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

fig.savefig("topten.png")

# saves data into csv files

organised.to_csv('total_list.csv')
top10.to_csv('topten_list.csv')
            
end = time.time()

print str((end - start)/60) + " Minutes"