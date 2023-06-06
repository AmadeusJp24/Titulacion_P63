import twitter

consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

#@Yinsito24

api = twitter.Api(consumer_key=consumer_key,
                  consumer_secret=consumer_secret,
                  access_token_key=access_token,
                  access_token_secret=access_token_secret)

contadores = api.GetFollowerIDs()
print(contadores)
#users = twitter.api.Api.GetFriends()

#print([u.screen_name for u in users])