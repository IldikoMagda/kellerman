import os
import psycopg2

def GetKinases():

    # Define our connection string
    conn_string = os.getenv('DB_CONNECTIONS')

    # get a connection, if a connect cannot be made an exception will be raised here
    conn = psycopg2.connect(conn_string)

    # conn.cursor will return a cursor object, you can use this cursor to perform queries
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM kinase')

    kinases = cursor.fetchall()
    conn.close()
    return kinases


def Query(query):

    # Define our connection string
    conn_string = os.getenv('DB_CONNECTION')
    print(conn_string)
    try:
        # get a connection, if a connect cannot be made an exception will be raised here
        conn = psycopg2.connect(conn_string)

        # conn.cursor will return a cursor object, you can use this cursor to perform queries
        cursor = conn.cursor()
        cursor.execute(query)

        result = cursor.fetchall()
        conn.close()
        # print("Print each row and it's columns values")
        # for row in result:
        #     print("Id = ", row[0], )
        #     print("Name = ", row[1])
        #     print("Family  = ", row[2], "\n")
        return result
    except:
        return 'An error occured while executing SQL query'
