from pymongo import MongoClient
import pprint

client = MongoClient ("mongodb://localhost:27017")
db = client.twitter

def tweetbynameandvacation():
	result = db.tweets.aggregate([
				{ "$group" : { "-id" : "$user.screen_name", 
								"_id" : {"entities.hashtags.vacation"}}}])
	return result

if __name__ == '__main__':
	result = tweetbynameandvacation()
	pprint.pprint(result)
<<<<<<< HEAD
	
=======
<<<<<<< HEAD
>>>>>>> 3686d3e4d29f991ba7e2ba5ccd34926509805b34
=======
>>>>>>> 0bf78c293ff4b6dbf50d053d0980e862f17e710c
>>>>>>> 01ddd9bfa7fc5f50ecab3ce14fc46d3020a5d8a3
