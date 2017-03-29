import psycopg2
import sys
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


conn = psycopg2.connect(database="postgres", user="postgres", password="pass", host="localhost", port="5432")
conn2 = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")

if len(sys.argv) == 2:
	cur = conn2.cursor()
	cur.execute("SELECT word, count from tweetwordcount where word=%s", [sys.argv[1]])

	records = cur.fetchall()
	for rec in records:
		print ('Total number of occurrences of "%s": %s' % (rec[0], rec[1]))
	conn.close()
elif len(sys.argv) == 1:
	cur = conn2.cursor()
	cur.execute("SELECT word, count from tweetwordcount ORDER BY word")
	records = cur.fetchall()
	statement='';
	for rec in records:
		print ('(%s, %s), ' % (rec[0], rec[1]))
		#statement = statement + "(%s, %s), " % (rec[0], rec[1])
	#print statement
else:
	print ('Error')

