

=======
import os
import psycopg2


def Query(query):

    # Define our connection string
    conn_string = ("host='ec2-54-75-245-94.eu-west-1.compute.amazonaws.com' dbname='d71uh4v1fd2hq' user='tdsneouerzmxkj' password='92a500cb091fe70168b32c66fa6a3d6c376d467d57fb9b663eb5d13446ecb2e6'")
    print(conn_string)
    try:
        # get a connection, if a connect cannot be made an exception will be raised here
        conn = psycopg2.connect(conn_string)

        # conn.cursor will return a cursor object, you can use this cursor to perform queries
        cur = conn.cursor()
        cur.execute(query)

        query = cur.fetchall()
        conn.close()
        # print("Print each row and it's columns values")
        # for row in result:
        #     print("Id = ", row[0], )
        #     print("Name = ", row[1])
        #     print("Family  = ", row[2], "\n")
        return query
    except:
        return 'An error occured while executing SQL query'

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
