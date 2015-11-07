import requests
url = "http://api.twitter.com/1.1/search/tweets.json?q=from%3AXXX%20%23vacation&result_type=popular"
# searches for hastag vacation from user XXX
results = requests.get(url)
jsonresults = results.json

#for post in jsonresults['results']:
#	print post['text'].encode('utf-8')s



text_file = open ("twitterSelfFeed.json", "w")
text_file.write (jsonresults)
text_file.close()
