import collections.abc
#hyper needs the four following aliases to be done manually.
collections.Iterable = collections.abc.Iterable
collections.Mapping = collections.abc.Mapping
collections.MutableSet = collections.abc.MutableSet
collections.MutableMapping = collections.abc.MutableMapping
#Now import hyper
from hyper.contrib import HTTP20Adapter
import requests
s = requests.Session()
s.mount('https://http2bin.org', HTTP20Adapter())

import json
import time
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
with open("data.json") as json_file:
    data = json.load(json_file)["results"]
persi=data["versi"]

head={
  "host":"api.yoha.pro",
  "content-type":"application/json; charset=utf-8",
  "user-agent":f"okhttp/5.0.0-alpha.2 {rdm.randint(1111,9999)}"
}

def login(no,passw):
    head["accept"]="application/json"
    head["accept-encoding"]="gzip"
    param={
        "user_login":no,
        "user_pass":passw,
        "user_email":"",
        "source":"",
        "v":persi,
        "ip":f'180.252.129.{rdm.randint(1,255)}',
        "l":"in",
    }
    uri=f'{data["host"]}api/auth/login'
    r = s.post(uri,params=param,headers=head)
    if r.status_code==200:
        ress=json.loads(r.text)
        try:
            token=f'Bearer {ress["data"]["access_token"]}'
            return token
        except:
            print(f'gagal : {r.text}')
            return 0
    else:
        print(f"gagal status code : {r.text}")
        return 0



def uid():
    uid = db.child('yoha').child('akun').get()
    acc = uid.val()["results"]
    return acc
def reset():
    acc=uid()
    token = []
    itr = 0
    for id in acc:
        itr += 1
        sys.stdout.write(f"{itr}\r")
        sys.stdout.flush()
        tkn = login(id["no"],id["pass"])
        if tkn != 0:
            try:
                token.append(tkn)
            except:
                # pass
                print(tkn)
        else:
            print("request eror")

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
