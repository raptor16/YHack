import urllib

get_url = "https://api.instagram.com/v1/users/self/media/liked?access_token=19425967.1fb234f.6b478a9fab2b49ba9ba479554199a156&max_like_id=1057979319057322008"
resultI = urllib.urlopen(get_url).read()

#print resultI

text_file = open ("InstagramMediaLikeLoc.json", "w")
text_file.write (resultI)
text_file.close()

