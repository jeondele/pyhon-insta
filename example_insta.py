from instagram.client import InstagramAPI

access_token = "a260613cb8cf4ea894a70bd653453295"
client_secret = "fa908800ef484dcfb4b77e2de72923f7 "
api = InstagramAPI(access_token=access_token, client_secret=client_secret)
recent_media, next_ = api.user_recent_media(user_id="adele", count=10)
for media in recent_media:
   print (media.caption.text)
