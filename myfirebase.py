import pyrebase

config = {
  "apiKey": "AIzaSyDAurUp8MI5ljZSfR5ytr0SI9K4aM_367o",
  "authDomain": "bikesafety-870a7.firebaseapp.com",
  "databaseURL": "https://bikesafety-870a7-default-rtdb.asia-southeast1.firebasedatabase.app",
  "projectId": "bikesafety-870a7",
  "storageBucket": "bikesafety-870a7.appspot.com",
  "messagingSenderId": "914952824248",
  "appId": "1:914952824248:web:10da734ad31d5553325b4d",
  "measurementId": "G-J09JBJZJYS"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()

myd = '1'


def setdata(data):
    global myd
    if myd != data:
        db.child("Data").child("Sleep").set(data)
        myd = data
    print("=============================================: ")
    print(data)


