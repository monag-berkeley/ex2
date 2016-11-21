import psycopg2
import re
import sys

conn = psycopg2.connect(database="Tcount", user="postgres", password="pass", host="localhost", port="5432")
cur = conn.cursor()

count1 = sys.argv[1]
count2 = sys.argv[2]

if int(count1)<int(count2):
	cur.execute("SELECT word, count FROM Tweetwordcount WHERE count between {0} and {1}".format(count1, count2))
else:
	cur.execute("SELECT word, count FROM Tweetwordcount WHERE count between {0} and {1}".format(count2, count1))
records = cur.fetchall()
print(records)
