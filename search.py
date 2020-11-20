import config
import tweepy

auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
api = tweepy.API(auth)

tweets = api.search('scu lightning complex wildfire -is:verified -is:retweet', count = '120')
for tweet in tweets:
  print(tweet.text)
