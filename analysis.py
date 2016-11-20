import psycopg2
import re

import matplotlib.pyplot as plt


def histogram(words):
	count = map(lambda x: x[1], words)
	word = map(lambda x: x[0], words)
        plt.barh(range(len(count)), count, color = 'green')
	plt.yticks(range(len(count)), word)	
	plt.savefig('plot.png', format='png')

conn = psycopg2.connect(database="Tcount", user="postgres", password="pass", host="localhost", port="5432")
cur = conn.cursor()
cur.execute("select * from tweetwordcount order by count desc limit 20;")
records = cur.fetchall()

#counts = [rec[1] for rec in records]
#words = [rec[0] for rec in records]
conn.commit()
conn.close()

#words = records.map(lambda rec:(rec[1],rec[0]))
histogram(records)

#plt.figure(num=1, figsize=(8, 6))
#plt.title('Top 20 Twitter words', size=14)
#plt.xlabel('words', size=14)
#plt.ylabel('counts', size=14)
#plt.legend()
#plt.bar(range(len(words)), counts, color='green', alpha=0.4)
#plt.savefig('plot.png', format='png')
