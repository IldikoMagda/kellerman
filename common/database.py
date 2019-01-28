import os
import psycopg2

def Query(query):
    # Define our connection string
    conn_string = os.getenv('DB_CONNECTION')
    # get a connection, if a connect cannot be made an exception will be raised here
    conn = psycopg2.connect('')

    # conn.cursor will return a cursor object, you can use this cursor to perform queries
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM public.kinase;')
    query = cursor.fetchall()

    cursor.close()
    conn.close()
        # print("Print each row and it's columns values")
        # for row in result:
        #     print("Id = ", row[0], )
        #     print("Name = ", row[1])
        #     print("Family  = ", row[2], "\n")
    return query
