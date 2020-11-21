from fireAPI import *
from search import *
from sendMessage import *

location = 'Reno'
if not resultList[4]:
  warning = ('Warning!! ' + (str(resultList[0])).upper() + ' wildfire named ' 
  + str(resultList[1]) + 'discovered around ' 
  + str(distanceList[3]) 
  + 'km away from your location and no information has been found regarding the containment.')
else:
  warning = ('Warning ' + str(resultList[0]) + ' wildfire named ' 
  + str(resultList[1]) + 'discovered ' 
  + ' around ' + str(distanceList[3]) 
  + 'km away from your location and it is ' 
  + str(resultList[4]) + ' % contained')

tweets = search(location + ' wildfire ')
numTweets = len(tweets)
finalMessage = ''
for x in range (numTweets):
  tweetText= str(x+1) + '. ' + str(tweets[x]) +'\n'
  finalMessage = finalMessage + tweetText
finalMessage = 'Here is what Twitter has to say: \n'+ finalMessage
# print(finalMessage)
send_reg_message(warning)
send_tweet_message(finalMessage)

# print(warning)