import psycopg2
import sys
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


conn = psycopg2.connect(database="postgres", user="postgres", password="pass", host="localhost", port="5432")
conn2 = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")

if len(sys.argv) == 2:
	my_input = sys.argv[1].split(',')
	k1 = my_input[0]
	k2 = my_input[1]
	if k1 > k2:
		print ('Error: k1 must be smaller than k2')
	else:
		cur = conn2.cursor()
		cur.execute("SELECT word, count FROM tweetwordcount WHERE count >= %s AND count <= %s \
		ORDER BY count DESC", [k1, k2])
	records = cur.fetchall()
	for rec in records:
		print ('%s: %s' % (rec[0], rec[1]))
	conn.close()
else:
	print (sys.argv)
	print ('Error')


