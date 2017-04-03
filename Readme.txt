MIDS W205 Exercise 2 - Michelle Liu

Step-by-step instructions on how to run the application:

1. This codebase assumes that it is being run on the correct AMI, with all the proper applications downloaded. 
(postgres, python, along with all the libraries, and streamparse specified in the Architecture.pdf)

2. Please follow direction as outlined in the assignment page to get the Twitter access token:

2.1. Once you have the four tokens, please input your Consumer Key, Consumer Secret, Access Token, and Access Token Secret in the /tweetwordcount/src/spouts/tweets.py 

3. Start the Storm application by typing the command "sparse run -t 60" in tweetwordcount folder. 
This will run Streamparse for 60 seconds. The emitted words and their respective word counts will be save into the table "tweetwordcount" under the Database "tcount"

4. Submit queries encoded in Python serving script to pull out the data from the database

4.1. finalresults.py without an argument returns all the words in the stream, and their total count of occurences, sorted alphabetically, one word per line. With a single word as an argument argument, it will print out the total number of word occurrences in the stream. 
For example, "python finalresults.py hello" will print out "Total number of occurences of “hello”: 10"

4.2. histogram.py gets two integers k1,k2 and returns all the words that their total number of occurrences in the stream that is greater than or equal to k1 and less than or equal to k2.
For example, "python histogram.py 3,8" will return all words with occurances greater than or equal to 3 but less than or equal to k2. 

4.3 top20result.py outputs a csv file titled "top20result.csv" with the top 20 words in the database and their respective counts. 
