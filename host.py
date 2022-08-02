import json
from collections import OrderedDict
import datetime
import pyrebase
import pytz

config = {
    "apiKey": "AIzaSyDo7m9xUXkOiCVjuS6kKwkLchejkUNl5IY",
    "authDomain": "attools-cc537.firebaseapp.com",
    "databaseURL": "https://attools-cc537-default-rtdb.asia-southeast1.firebasedatabase.app/",
    "projectId": "attools-cc537",
    "storageBucket": "attools-cc537.appspot.com",
    "messagingSenderId": "181490859838",
    "appId": "1:181490859838:web:426c0a2f365cec8206f66f",
    "measurementId": "G-DY46HYTHT6"
}


firebase = pyrebase.initialize_app(config)
db = firebase.database()


def getdurasi(x1):
    now = datetime.datetime.now(pytz.timezone("Asia/Jakarta"))
    s1 = (now.strftime("%H%M"))
    ss1 = datetime.datetime.strptime(s1, "%H%M")
    # print(ss1)

    dttr = x1
    tes = datetime.datetime.strptime(dttr, '%H:%M')
    s2 = (tes.strftime("%H%M"))
    ss2 = datetime.datetime.strptime(s2, "%H%M")
    # print(ss2)

    return(ss1-ss2)


dt = db.child('host').get()
chil = []
x = 0
for t in dt:
    x += 1
    nama = t.val()["nickname"]
    chil.append(nama)
    print(f"{x}. {nama}")

while True:
    print()
    inp = input("room nomor : ")
    cil = chil[int(inp) - 1]
    getrum = db.child('host').child(cil).get()
    rum = getrum.val()

    duras = getdurasi(rum["jamlive"][:5])
    for tt in rum:
        print(f"\t{tt} : {rum[tt]}")
    print(f"\tDurasi : {duras}")
