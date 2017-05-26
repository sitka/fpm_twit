
#Twitter API Keys are stored in a secret file
from twitter_API import consumer_key, consumer_secret, access_token, access_token_sectre
import tweepy
import csv
from textblob import TextBlob

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_sectre)


#twitter is now authenticated

api = tweepy.API(auth)


csvFile = open('FPM4.csv', 'a')
csvWriter = csv.writer(csvFile)


#this is the Twitter query

for tweet in tweepy.Cursor(api.search,
					q = "#ourvoicesarevital", 
					since = "2017-05-19",
					until = "2017-05-20",
					lang = "en").items():

#write rows to CSV file
#		analysis = TextBlob(tweet.text)
		csvWriter.writerow([tweet.user.screen_name, tweet.created_at, tweet.text.encode('utf-8'), tweet.retweet_count])
		print tweet.created_at, tweet.text, 

csvFile.close()


#for tweet in public_tweets:
#	print(tweet.text)
#	analysis = TextBlob(tweet.text)
#	print(analysis.sentiment)

#

	
