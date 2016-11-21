import psycopg2
import re
import sys

conn = psycopg2.connect(database="Tcount", user="postgres", password="pass", host="localhost", port="5432")
cur = conn.cursor()
if len(sys.argv)>1:
	word = sys.argv[1]
	cur.execute("SELECT count FROM Tweetwordcount WHERE word='{0}'".format(re.escape(word)))
	record = cur.fetchall()
	print("Total number of occurences of {0}: {1}".format(re.escape(word), record[0][0]))
else:
	cur.execute("SELECT word, count FROM Tweetwordcount")
	records = cur.fetchall()
	print(records)

conn.close()
	
