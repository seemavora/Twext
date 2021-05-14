## Project Demo
https://youtu.be/BdzOdhu_89Q 

## Inspiration
In 2020, California faced the worst fires in its history in the midst of a pandemic. During this stressful situation, reliable and quick information was hard to come by and the source many relied on was Twitter. Tweets made by the local fire departments and onsite witnesses were relayed to the public in a faster and more accurate manner in comparison to other sources. As a result of the overwhelming amount of information received through Twitter, users were also faced with the issue of sorting through the tweets they found most reliable, especially when the time was of the essence.

## What It Does
Twext takes a user's location and phone number to personalize their communication experience. By signing up for Twext, the user automatically registers for natural disaster and safety updates. Meaning, in case of an emergency, the user will be provided a description of what is happening along with a small list of curated tweets relaying information pertaining to this issue. In addition, the user can opt in to sign up for other Twext communication features such as events where the user will get information and the top Tweets regarding an event of their choice.

For this hackathon, we focused on a natural disaster safety feature, where based on one's location, Twext will continuously check for fires in a set radius from the user's location. In the case of a fire, the user will immediately receive information regarding the fire.
 
## How We Built It
There are three components of this product: the frontend, backend, and database.

_The Frontend_

The frontend utilizes the React.js library along with CSS to create a static homepage where the users can enter personal information like their location and phone number.

_The Backend_

This flows into the backend, where we use several different technologies and languages depending on the services Twext provides. One of them was using Flask to perform HTTP POST requests to connect inbound SMS texts to Twilio. In addition, we used the Tweepy API and Breezometer API to gather information about wildfires and subsequently generate a list of reliable tweets. Lastly, we also implemented a useful feature of auto-completing the user’s location using the google-maps-api.

_The Database_

For the database, we chose to use Firebase. Here, we created a table of user entries containing each individual user’s exact location latitude, longitude, and phone number. This data was fed into the various APIs mentioned above to gather data to be later displayed!

## Challenges We Ran Into
We, as a team, always welcome challenges as we believe it pushes us to our limits, helping us create some of the best projects. During the Codechella hackathon, some of the challenges we faced were learning completely new languages/technology, being able to quickly adapt to changes in plans, and getting all the pieces of the puzzle to work. The biggest challenge we ran into was finding a way to analyze all the data of the tweets we had queried and implementing an algorithm such that we showed the user only the top, most reputable tweets. 

## Accomplishments That We're Proud Of
Throughout this development experience, we are extremely proud to have endured the challenges and learned the necessary technologies to build this application. We were able to adapt to changes in plans and worked cohesively as a team. Only a year prior, we were mostly freshmen and completely clueless as to how to build a program or use Github. The thought of building an entire application in a matter of three days would have seemed daunting to us only a year ago. This experience has really demonstrated our progress, how far we have come in our technical skills, and our ability to truly make it in this field.

## What We Learned
Prior to this experience, the majority of our team had no experience working with APIs nor did we know how to connect the backend technology with the frontend. This whole experience has truly encompassed our abilities and technical skills, as we incorporated what we know as well as newly learned techniques.
 
## What's Next for Twext 
Currently, we have the implementation for the user to query the text bot for information solely about wildfires. We wish to further the application by adding the same structure of information for other purposes, such as safety information, events in the area, etc. Safety features that we would implement include the number of casualties, missing persons, and active shooters. Events would include concerts and festivals in the near vicinity as well as restaurant openings. Overall, we wish to expand the functionality of Twext to make searching for information easier for Twitter users. Down the line, we would like to implement machine learning algorithms for the sorting of the tweets to be automated. 

