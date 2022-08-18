import json
import time
import getapi
import pytz
import random as rdm
import sys
from datetime import datetime
import ambil

import pyrebase
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


def uid():
    uid = db.child('yoha').child('akun').get()
    acc = uid.val()["results"]
    return acc


def reset():
    acc = uid()
    token = []
    itr = 0
    for id in acc:
        itr += 1
        sys.stdout.write(f"{itr}/{len(acc)}\r")
        sys.stdout.flush()
        tkn = getapi.login(id["no"], id["pass"])
        if tkn != 0:
            try:
                token.append(tkn)
            except:
                # pass
                print(tkn)
        else:
            print("request eror")
        time.sleep(2)

    tokk = {"results": token}
    db.child("yoha").child("token").update(tokk)
    print("dah")


tes = True
jamar = []


def jam():
    tz = pytz.timezone("Asia/Jakarta")
    now = datetime.now(tz)
    jamm = now.strftime("%m/%d/%Y, %H:%M")
    minut = now.strftime("%H%M")
    if minut == "0030" and jamm not in jamar:
        jamar.append(str(jamm))
        print("•>> "+str(jamm))
        return True
    else:
        # print(""+str(jamm))
        return False


resetdong = False
tz = pytz.timezone("Asia/Jakarta")
now = datetime.now(tz)
jamm = now.strftime("%m/%d/%Y, %H:%M")
print(jamm)
while True:
    jlk = jam()
    if tes == True:
        tes = False
        jlk = True
    if jlk == False:
        pass
    else:
        tz = pytz.timezone("Asia/Jakarta")
        now = datetime.now(tz)
        klj = now.strftime("%m/%d/%Y, %H:%M")

        resetdong = False
        print("•>> Melakukan Reset Token")
        reset()
        print("•>> Selesai Reset")

    time.sleep(1)
