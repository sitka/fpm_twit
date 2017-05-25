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


#this will list the target user's list of followers

pers1 = "jeffcharrison"
pers2 = "lizzielashark"


while True:
    try:


        for user in tweepy.Cursor(api.followers, screen_name = pers1).items(2):
				print user.screen_name
				csvWriter.writerow([pers1, user.screen_name])


		for user in tweepy.Cursor(api.followers, screen_name = pers2).items(2):
				print user.screen_name
				csvWriter.writerow([pers2, user.screen_name])

    except tweepy.TweepError:
    	print "error handeling1"
        time.sleep(60 * 15)
        continue


    except StopIteration:
        break



 




#write rows to CSV file
#		analysis = TextBlob(tweet.text)
