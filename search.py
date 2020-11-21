import config
import tweepy
from sendMessage import *

auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
api = tweepy.API(auth)

def search(location):
  tweets = api.search(location, count = '23')
  default = 10
  count = 0
  textTweet = []
  for tweet in tweets:
    if (tweet.user.verified == True and count <= 2 ):
      if (tweet.text not in textTweet):
        textTweet.append(tweet.text)
        count += 1
    elif(tweet.retweet_count >= default and tweet.retweeted == False):
        default = tweet.retweet_count
        if (tweet.text not in textTweet):
          textTweet.append(tweet.text)
  return textTweet

  # print(textTweet)
