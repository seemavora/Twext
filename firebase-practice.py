from firebase import Firebase

firebaseConfig = {
    "apiKey": "AIzaSyCG0VloA2BiD4Jg3aVxRCx1_iivRsJuvlQ",
    "authDomain": "userentries-f09aa.firebaseapp.com",
    "databaseURL": "https://userentries-f09aa.firebaseio.com",
    "projectId": "userentries-f09aa",
    "storageBucket": "userentries-f09aa.appspot.com",
    "messagingSenderId": "918221316416",
    "appId": "1:918221316416:web:d27ecf31f5cc4bc5f95aa5",
    "measurementId": "G-CFLWLBMTS2"
}

firebase = Firebase(firebaseConfig)

db = firebase.database()

location = ""  # FROM NANAR!
# add/update item
data = {"phoneNumber": 123456, "location": location}
db.child("users/person1").set(data)

# getitem
users = db.child("users").get().val()
for key, item in users.items():
    location = (item['location'])

print(location)

# # remove item
# db.child("users").child("person1").remove()
# db.child("users").child("person2").remove()
