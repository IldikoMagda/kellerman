import os
import psycopg2

def Query(query):

    # Define our connection string
    conn_string = ("host='ec2-54-75-245-94.eu-west-1.compute.amazonaws.com' dbname='d71uh4v1fd2hq' user='tdsneouerzmxkj' password='92a500cb091fe70168b32c66fa6a3d6c376d467d57fb9b663eb5d13446ecb2e6'")

    try:
        # get a connection, if a connect cannot be made an exception will be raised here
        conn = psycopg2.connect(conn_string)

        # conn.cursor will return a cursor object, you can use this cursor to perform queries
        cur = conn.cursor()
        cur.execute(query)

        query = cur.fetchall()    # fetch query 
        conn.close()            # close connection 

        return query
    except:
        return 'An error occured while executing SQL query'


# function for inhibitor search 
def Inhibitor(inhibitor):
    #start connecition
    conn = psycopg2.connect("dbname=d71uh4v1fd2hq user=tdsneouerzmxkj password=92a500cb091fe70168b32c66fa6a3d6c376d467d57fb9b663eb5d13446ecb2e6 host=ec2-54-75-245-94.eu-west-1.compute.amazonaws.com")
 
    cur = conn.cursor()     # call cursor
    cur.execute(inhibitor)      # execute query
  
    inhibitor = cur.fetchall()
    return inhibitor
    cur.close()
    conn.close()     # close connection 

# set function for phosphotiste table 
def Phospho(phosphosite):
    #start connecition
    conn = psycopg2.connect("dbname=d71uh4v1fd2hq user=tdsneouerzmxkj password=92a500cb091fe70168b32c66fa6a3d6c376d467d57fb9b663eb5d13446ecb2e6 host=ec2-54-75-245-94.eu-west-1.compute.amazonaws.com")
 
    cur = conn.cursor()     # call cursor
    cur.execute(phosphosite)      # execute query
  
    phosphosite = cur.fetchall()
    return phosphosite
    cur.close()
    conn.close()





#def GetKinases():
    
    # Define our connection string
    #conn_string = os.getenv('DB_CONNECTIONS')

    # get a connection, if a connect cannot be made an exception will be raised here
    #conn = psycopg2.connect(conn_string)

    # conn.cursor will return a cursor object, you can use this cursor to perform queries
    #cursor = conn.cursor()
    #cursor.execute('SELECT * FROM kinase')

    #kinases = cursor.fetchall()
    #conn.close()
    #return kinase
