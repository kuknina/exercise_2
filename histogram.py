import sys
from  Twittercredentials import *
import psycopg2

conn = psycopg2.connect(user="postgres", password="pass", host="localhost", port="5432")
conn.set_isolation_level(0)

#Create a Table
#The first step is to create a cursor.

cur = conn.cursor()

print (sys.argv)

a = int(sys.argv[1])
b = int(sys.argv[2])

print (a, b)

cur.execute('''SELECT word, count FROM Tweetwordcount WHERE ((count >= %i) AND (count <= %i));'''  % (a, b)  )
result = cur.fetchall()
for pair in result:
        print (pair[0], pair[1])

conn.commit()
