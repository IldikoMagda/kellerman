import os
import psycopg2

def GetKinases():

    # Define our connection string
    conn_string = os.getenv('DB_CONNECTIONS')

    # get a connection, if a connect cannot be made an exception will be raised here
    conn = psycopg2.connect(conn_string)

    # conn.cursor will return a cursor object, you can use this cursor to perform queries
    cursor = conn.cursor()
    results = cursor.execute('SELECT * FROM kinase')
    results = cursor.fetchall()
    conn.close()
    return results
except:
    return 'An error occured while executing SQL query'


