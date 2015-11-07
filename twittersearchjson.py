import json
import requests
url = 'http://search.twitter.com/search.json?q=%23wholeworldlaughs'
results = requests.get(url)
#jsonresults = results.json

with open('tweet.json', 'w') as outfile:
    json.dump(results, outfile)
#for post in jsonresults['results']:
#	print post['text'].encode('utf-8')



