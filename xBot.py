import tweepy

all_keys =  open('twitterKEYS', 'r').read().splitlines()
api_key = str("y7U0jzFq2iUYvrSJgH5n4e1cY")
api_key_secret = str("Suyr0tr6x7MfZyIZa3MLbCo53JfNeYOd0Cni6EdF4vTVxqeqWI")
access_token = str("1476936606607355911-odlEpS9HG2z9Ewdnd1Mvfu7ihdG0lq")
access_token_secret = str("dZ9mBJpgjUkeR7T3UPRl5Cyf9Yy7sgIbgnm008OyCqTOb")

authenticator = tweepy.OAuthHandler(api_key, api_key_secret)
authenticator.set_access_token(access_token, access_token_secret)

api = tweepy.API(authenticator, wait_on_rate_limit=True)

#search for stuffs on twitter
tweets = tweepy.Cursor(api.search_tweets, q="brains", lang="en").items(10)

print([tweet for tweet in tweets])

#follow a user
api.create_friendship('trvisXX')

#automated liking post
#user = api.get_user("Abjsshyest")

#tweets_user = api.user_timeline(user_id=user.id)

#for tweet in tweets_user:
#    if not tweet.favorited:
#        api.create_favorite(tweet.id)
##
#tweets_home = api.home_timeline(count=10)

#for tweets in  tweets_home:
#    if tweet.author.name.lower() != "Abjsshyest":
#        if not tweet.favorited:
#            print(f"Liking {tweet.id} ({tweet.author.name})")
#            api.create_favorite(tweet.id)


user = api.get_user(screen_name="trvisXX")
for follower in user.followers():
    print(f"{follower.name} follows {user.name}")
print(user.name)
print (user.description)

