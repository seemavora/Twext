from fireAPI import *
from search import *
from sendMessage import *
from fireAPI import *

resultList = listsManager()
location = resultList[1] 

def warningMessage():
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
  return warning

def tweetMessage():
  tweets = search(location + ' wildfire ')
  numTweets = len(tweets)
  finalMessage = ''
  for x in range (numTweets):
    tweetText= str(x+1) + '. ' + str(tweets[x]) +'\n'
    finalMessage = finalMessage + tweetText
  finalMessage = 'Here is what Twitter has to say: \n'+ finalMessage
  # print(finalMessage)
  return finalMessage

  # print(warning)
sendMessage(warningMessage())
sendMessage(tweetMessage())