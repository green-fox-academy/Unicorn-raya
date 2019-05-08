# Accidentally I got the wrong URL for a funny subreddit. It's probably "odds" and not "bots"
# Also, the URL is missing a crutial component, find out what it is and insert it too!

url = "https//www.reddit.com/r/nevertellmethebots"
url = url.replace("bots","odds")
insert_place = url.find("//")
url = url[0:insert_place] + ":" + url[insert_place:] 

print(url)

