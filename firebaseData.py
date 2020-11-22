from firebase import Firebase

firebaseConfig = {
    "apiKey": "AIzaSyAezcoT2Dpgh6OO-Y0mRk4s952JIzp5Tns",
    "authDomain": "twitter-tracker-6e45a.firebaseapp.com",
    "databaseURL": "https://twitter-tracker-6e45a.firebaseio.com",
    "projectId": "twitter-tracker-6e45a",
    "storageBucket": "twitter-tracker-6e45a.appspot.com",
    "messagingSenderId": "161829123701",
    "appId": "1:161829123701:web:4735cefad33f69432e2a3c",
    "measurementId": "G-K5471VQ1NK"
}

firebase = Firebase(firebaseConfig)

db = firebase.database()

result = []

def getEntry():
   user = db.child('users').get().val()
   for key, item in user.items():
       result.append(item)
   return result

# print(getEntry())

