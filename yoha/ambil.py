import pyrebase

config = {
    "apiKey": "AIzaSyATkiylea79HwAQNoJHDa5XLCK6b7kK1Ys",
    "authDomain": "bling-1b0b0.firebaseapp.com",
    "databaseURL": "https://bling-1b0b0-default-rtdb.asia-southeast1.firebasedatabase.app",
    "projectId": "bling-1b0b0",
    "storageBucket": "bling-1b0b0.appspot.com",
    "messagingSenderId": "489126684041",
    "appId": "1:489126684041:web:0f6978ddf5f9b9929bed58"
}


firebase = pyrebase.initialize_app(config)
db = firebase.database()


def token():
    tkn = db.child('yoha').child('token').get()
    acc = tkn.val()["results"]
    return acc


def uid():
    tkn = db.child('yoha').child('akun').get()
    acc = tkn.val()["results"]
    return acc
