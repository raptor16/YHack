import urllib

get_url = "https://api.instagram.com/v1/users/self/feed?access_token=19425967.1fb234f.6b478a9fab2b49ba9ba479554199a156&max_id=1112658542408961440_38671474"
resultI = urllib.urlopen(get_url).read()

#print resultI

text_file = open ("InstagramSelfFeedLoc.json", "w")
text_file.write (resultI)
text_file.close()

