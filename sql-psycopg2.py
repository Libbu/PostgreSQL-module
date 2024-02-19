import psycopg2

#connect to "chinook" database
connection = psycopg2.connect(database = "chinook")

#build a cursor object (similar to set, list or array(js)) of the database
cursor = connection.cursor()

#Query 1 - select all records from the "artist" table
cursor.execute('SELECT * FROM "artist"')

# fetch the results (mulitple)
results =  cursor.fetchall()

#fetch the result (single)
#results = cursor.fetchone()

#close the connection
connection.close()

#print results

for result in results:
    print(result)