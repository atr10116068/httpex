import requests
import json
import time
import pytz
import seting,random
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
persi = seting.versi()


def loginid(x):
    uri = "https://wjxwd01mwyo.dt01showxx02.com/App/User_LoginRegister/Login"
    headers = {
        "User-Agent": f"HS-Android Mozilla/5.0 (Linux; Android 8.1.0; SM-J730F Build/{random.randint(1000,9999)}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.{random.randint(1000,9999)}.129 Mobile Safari/537.36",
        "BundleIdentifier": "user",
        "Accept-Encoding": "identity",
        "X-Version": persi,
        "Content-Type": "application/json; charset=UTF-8",
        "Host": "wjxwd01mwyo.dt01showxx02.com",
        "Connection": "Keep-Alive"
    }
    param = x
    # kalau mau reset v1
    # param['force_new'] = '1'
    # print(param)
    # exit()

    try:
        req = requests.post(uri, data=json.dumps(param), headers=headers)
        ress = json.loads(req.text)
        return ress
    except Exception as e:
        print("Failed : "+str(e))
        return 0


ataroinvcode = "yBooNa"
acc = ambil.uid()
print(f"\njumlah uid : {len(acc)}")
print("0 juga termasuk")
lpp=input("Enter To All")
if lpp=="":
    tkn1,tkn2=0,len(acc)
else:
    tkn1,tkn2=int(input("tkn1 : ")),int(input("tkn2 : "))
jeda=float(input("waktu jeda : "))

def reset():
    # token terakhir untuk akun inti
    token = ambil.token()
    itr = tkn1
    for id in acc[tkn1:tkn2]:
        while True:
            print(f"___________________________________[{itr}]")

            tkn = loginid(id)
            if tkn!=0:
                if tkn["code"] == 0:
                    print(tkn)
                    tknn = tkn["result"]["access_token"]
                    try:
                        token[itr]=tknn
                    except:
                        token.append(tknn)
                    itr += 1
                        
                    time.sleep(random.randint(jeda,jeda+10))
                    break
            else:
                print(f"  [{itr}]  request eror : {tkn}")
                for i in range(random.randint(jeda,jeda+10)):
                    sys.stdout.write(f"{itr}\r")
                    sys.stdout.flush()
                    time.sleep(1)
    tokk = {"results": token}

    db.child("account").child("token").update(tokk)
    print("dah")


tes = True
jamar = []


def jam():
    tz = pytz.timezone("Asia/Jakarta")
    now = datetime.now(tz)
    jamm = now.strftime("%m/%d/%Y, %H:%M")
    minut = now.strftime("%H%M")
    if minut == "0730" and jamm not in jamar:
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
