#Twitter API Keys are stored in a secret file
from twitter_API import consumer_key, consumer_secret, access_token, access_token_sectre
import tweepy
import csv
import time

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_sectre)


#twitter is now authenticated


api = tweepy.API(auth)


#This loads up CSV file to write data to

csvFile = open('followers.csv', 'a')
csvWriter = csv.writer(csvFile)



pers1 = "jeffcharrison"
pers2 = "lizzielashark"


#this will list the target user's list of followers

#followlist = ["jeffcharrison"]

#for user in tweepy.Cursor(api.followers, screen_name= pers1).items(10):
#	for account in tweepy.Cursor(api.followers).items(1):
#		time.sleep(1)
#		print user.screen_name
#		csvWriter.writerow(user.screen_name)		
		

for user in tweepy.Cursor(api.followers, screen_name = pers2).items():
	print user.screen_name
	csvWriter.writerow([pers2, user.screen_name])




#list1 = ['jeffcharrison', 'Bradsedal']

#print list1
 




#write rows to CSV file
#		analysis = TextBlob(tweet.text)
#	csvWriter.writerow([tweet.created_at, tweet.user.screen_name])



