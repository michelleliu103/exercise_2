from __future__ import absolute_import, print_function, unicode_literals

from collections import Counter
from streamparse.bolt import Bolt

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

class WordCounter(Bolt):

    def initialize(self, conf, ctx):
        self.counts = Counter()

	# Connect to the database
	conn = psycopg2.connect(database="postgres", user="postgres", password="pass", host="localhost", port="5432")

	#Create the Database
	try:
    		# CREATE DATABASE can't run inside a transaction
    		conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    		cur = conn.cursor()
    		cur.execute("CREATE DATABASE tcount")
    		cur.close()
    		conn.close()
	except:
    		print ("Could not create tcount")

	#Connecting to tcount

	conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
	conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
	#Create a Table

	cur = conn.cursor()
	cur.execute("DROP TABLE IF EXISTS tweetwordcount; \
	CREATE TABLE tweetwordcount \
       		(word TEXT PRIMARY KEY NOT NULL, \
       		count INT NOT NULL);")
	conn.commit()
	cur.close()
	conn.close()

    def process(self, tup):
        word = tup.values[0]

        # Increment the local count
        self.counts[word] += 1
        self.emit([word, self.counts[word]])

        # Log the count - just to see the topology running
        self.log('%s: %d' % (word, self.counts[word]))

	#Inserting/Selecting/Updating

	#Rather than executing a whole query at once, it is better to set up a cursor that 
	#encapsulates the query, 
	#and then read the query result a few rows at a time. One reason for doing this is
	#to avoid memory overrun when the result contains a large number of rows. 
	
	conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
	conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
	cur = conn.cursor()

	cur.execute("UPDATE tweetwordcount SET count=%s WHERE word=%s; \
	 INSERT INTO tweetwordcount (word,count) SELECT %s, 1 \
	WHERE NOT EXISTS (SELECT 1 FROM tweetwordcount WHERE word=%s)", (self.counts[word], word, word, word))
        conn.commit()
	cur.close()
	conn.close()

