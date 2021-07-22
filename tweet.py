import tweepy
import time
from keys import *

print("PI Bot live")

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)


def getDate():
	epochSeconds = time.time()
	currentTime = time.localtime(epochSeconds)
	return str(currentTime.tm_mon) + "/" + str(currentTime.tm_mday) + "/" + str(currentTime.tm_year)
def getHour():
	epochSeconds = time.time()
	currentTime = time.localtime(epochSeconds)
	return str(currentTime.tm_hour)
def getMin():
	epochSeconds = time.time()
	currentTime = time.localtime(epochSeconds)
	return str(currentTime.tm_min)


def tweetevery314(timeofday):
	if timeofday == "pm":
		api.update_status("Good Afternoon! It's PI time !!!! \n\n" + getDate())
		api.send_direct_message(3254499216,"Pi has been tweeted")
		print("tweeted!")
		time.sleep(60)
	elif timeofday == "am":
		api.update_status("Good Morning ! It's PI time !\n\n" + getDate())
		api.send_direct_message(3254499216,"Pi has been tweeted")
		print("tweeted!")
		time.sleep(60)
	else:
		return 

while True:
	try: 
		if getHour() == "3":
			if getMin() == "14":
				tweetevery314("am")
		elif getHour() == "15" :
			if getMin() == "14":
				tweetevery314("pm")
		print(getHour() + " : " + getMin())	
		time.sleep(15)	
	except:
		time.sleep(60)