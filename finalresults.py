#Connecting to a database
#Note: If the database does not exist, then this command will create the database

import sys
from Twittercredentials import *
import psycopg2

conn = psycopg2.connect(user="postgres", password="pass", host="localhost", port="5432")
conn.set_isolation_level(0)

#Create a Table
#The first step is to create a cursor.

cur = conn.cursor()
#cur.execute('''DROP DATABASE Tcount''')

#cur.execute('''CREATE DATABASE Tcount''')
#cur.execute('''DROP TABLE Tweetcount''')

#cur.execute('''CREATE TABLE Tweetwordcount
#       (word TEXT PRIMARY KEY     NOT NULL,
#       count INT     NOT NULL);''')

if len(sys.argv)< 2:
        cur.execute('''SELECT * FROM Tweetwordcount;''')
        cur.fetchall()
else:
        w = sys.argv[1]
        cur.execute('''SELECT * FROM Tweetwordcount WHERE word = '%s';''' %w)
        result = cur.fetchall()
        print ("Total number of occurences of: '%s' " % result)

conn.commit()
#conn.close()
