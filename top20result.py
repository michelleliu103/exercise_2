import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import csv

conn = psycopg2.connect(database="postgres", user="postgres", password="pass", host="localhost", port="5432")
conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")

csvFile = open('top20result.csv', 'a')
csvWriter = csv.writer(csvFile)
cur = conn.cursor()
cur.execute("SELECT word, count from tweetwordcount ORDER BY count DESC LIMIT 20")
records = cur.fetchall() 
csvWriter.writerow(['Word', 'Count'])
for rec in records: 
        csvWriter.writerow([rec[0], rec[1]])
conn.commit() 
conn.close() 
csvFile.close()
