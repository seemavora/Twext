import config
import tweepy
from twilio.rest import Client

auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
api = tweepy.API(auth)


def sendMessage(tweet):
    account_sid = config.twilio_sid
    auth_token = config.twilio_auth_token
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
            body=tweet,
            from_=config.from_phone_number,
            to=config.to_phone_number
        )
    return "Message sent with id{}".format(message.sid)



# tweets = api.search('wildfire', count=10)
# tweet = tweets[0]
# sid = send_message(tweet.text)
# print(sid)
