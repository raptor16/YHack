import urllib

get_url = "https://api.instagram.com/v1/users/self/feed?access_token=1406078bbd424acc8fc8095f881aa95a"
resultI = urllib.urlopen(get_url).read()

#print resultI

text_file = open ("InstagramSelfFeedLoc.json", "w")
text_file.write (resultI)
text_file.close()

