import config
import tweepy

auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
api = tweepy.API(auth)

tweets = api.search('pinehaven', count = '23')
default = 10
count = 0
textTweet = []
for tweet in tweets:
  if (tweet.user.verified == True and count <= 2 ):
    textTweet.append(tweet.text)
    count += 1
  elif(tweet.retweet_count >= default and tweet.retweeted == False):
      default = tweet.retweet_count
      textTweet.append(tweet.text)
print(textTweet)
