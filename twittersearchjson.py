import requests
url = 'http://search.twitter.com/search.json?q=%23wholeworldlaughs'
results = requests.get(url)
jsonresults =- results.json

#for post in jsonresults['results']:
#	print post['text'].encode('utf-8')



