var firebase = require("firebase");

var firebaseConfig = {
  apiKey: "AIzaSyAezcoT2Dpgh6OO-Y0mRk4s952JIzp5Tns",
  authDomain: "twitter-tracker-6e45a.firebaseapp.com",
  databaseURL: "https://twitter-tracker-6e45a.firebaseio.com",
  projectId: "twitter-tracker-6e45a",
  storageBucket: "twitter-tracker-6e45a.appspot.com",
  messagingSenderId: "161829123701",
  appId: "1:161829123701:web:4735cefad33f69432e2a3c",
  measurementId: "G-K5471VQ1NK"
};

firebase.initializeApp(firebaseConfig);

export function write(ref, obj) {
  firebase
    .database()
    .ref(ref)
    .set(obj);
}
