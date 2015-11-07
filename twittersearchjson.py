import json
import requests
url = "http://api.twitter.com/1.1/search/tweets.json?q=from%3AXXX%20%23vacation&result_type=popular"
# searches for hastag vacation from user XXX
results = requests.get(url)
<<<<<<< HEAD
#jsonresults = results.json
=======
jsonresults = results.json
>>>>>>> master

with open('tweet.json', 'w') as outfile:
    json.dump(results, outfile)
#for post in jsonresults['results']:
#	print post['text'].encode('utf-8')s



text_file = open ("twitterSelfFeed.json", "w")
text_file.write (jsonresults)
text_file.close()
