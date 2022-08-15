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

import json
import random as rdm

with open("data.json") as json_file:
    data = json.load(json_file)["results"]
persi=data["versi"]


head={
  "host":"api.yoha.pro",
  "content-type":"application/json; charset=utf-8",
  "user-agent":f"okhttp/5.0.0-alpha.2 {rdm.randint(1111,9999)}"
}


def profile(token):
    head["authorization"]=token
    uri=f'{data["host"]}api/auth/me?v={persi}&ip=180.{rdm.randint(1,255)}.{rdm.randint(1,255)}.{rdm.randint(1,255)}&l=in'
    r = s.get(uri,headers=head)
    if r.status_code==200:
        ress=(json.loads(r.text))
        for akun in ress["data"]:
            # print(f"{akun} : {ress['data'][akun]}")
            return ress
        else:
            print(f"gagal : {ress['message']}")
            return 0

def claim(token,days):
    head["authorization"]=token
    aipi=f'180.{rdm.randint(1,255)}.{rdm.randint(1,255)}.{rdm.randint(1,255)}'
    param1={
        "v":persi,
        "ip":aipi,
        "l":"in"
    }
    #entry
    uri=f'{data["host"]}api/activity/entry?v={persi}&v={persi}&ip=180.{rdm.randint(1,255)}.{rdm.randint(1,255)}.{aipi}&l=in'
    r = s.get(uri,headers=head)
    if r.status_code==200:
        ress=(json.loads(r.text))
        print(f"Entry : {ress['status']}")
    #registerActv
    uri=f'{data["host"]}api/registerActivity/receiveAward?v={persi}&v={persi}&ip=180.{rdm.randint(1,255)}.{rdm.randint(1,255)}.{aipi}&l=in'
    r = s.post(uri,params=param1,headers=head)
    if r.status_code==200:
        ress=(json.loads(r.text))
        print(f"Receive : {ress['status']}")
    #Auth
    uri=f'{data["host"]}api/auth/me?v={persi}&v={persi}&ip=180.{rdm.randint(1,255)}.{rdm.randint(1,255)}.{aipi}&l=in'
    r = s.get(uri,headers=head)
    if r.status_code==200:
        ress=(json.loads(r.text))
        if ress['status'] != "error":
            print(f"Auth : [{ress['data']['coin']}] {ress['data']['user_nicename']}")
    #claim
    uri=f'{data["host"]}api/signs/store?day={days}&sign_id={days}&v={persi}&v={persi}&ip=180.{rdm.randint(1,255)}.{rdm.randint(1,255)}.{aipi}&l=in'
    r = s.post(uri,headers=head)
    if r.status_code==200:
        ress=(json.loads(r.text))
        print(f"Claim : {ress}")


def randcode():
    avail=["q","w","e","r","t","y","u","i","o","p","1","2","3","4","5","6","7","8","9","0","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"]
    tex=""
    for t in range(34):
        tex+=rdm.choice(avail)
    return tex
    
def sendcode(nomer):
    head["accept"]="application/json"
    head["accept-encoding"]="gzip"
    param={
        "mobile":nomer,
        "tag":"register",
        "v":persi,
        "ip":f'180.252.{rdm.randint(1,255)}.{rdm.randint(1,255)}',
        "l":"in",
    }
    uri=f'{data["host"]}api/sms/verify-code'
    r = s.post(uri,params=param,headers=head)
    if r.status_code==200:
        ress=json.loads(r.text)
        try:
            return ress
        except:
            print(f'gagal : {r.text}')
    else:
        print(f"gagal status code : {r.text}")

def register(nomer,password):
    head["accept"]="application/json"
    head["accept-encoding"]="gzip"
    param={
        "user_login":nomer,
        "user_pass":password,
        "user_pass2":password,
        "source":"android",
        "referral_code":"INoQDdUI2W4TZZDd",
        "channel_code":"2",
        "unique_code":f"{rdm.randint(100000,999999)}7{rdm.randint(100000,999999)}-{rdm.randint(100000,999999)}0{rdm.randint(100000,999999)}{rdm.randint(100000,999999)}",
        "code":input("code : "),
        "pasteboard":"",
        "device_code":randcode(),
        "guest_code":"",
        "v":persi,
        "ip":f'180.252.{rdm.randint(1,255)}.{rdm.randint(1,255)}',
        "l":"in",
    }
    uri=f'{data["host"]}api/auth/register'
    r = s.post(uri,params=param,headers=head)
    if r.status_code==200:
        ress=json.loads(r.text)
        try:
            dbb = {"results": []}
            nuall={"no":nomer,"pass":password}
            dbb["results"].append(nuall)
            db.child("yoha").child("akun").update(dbb)
            return ress
        except:
            print(f'gagal : {r.text}')
    else:
        print(f"gagal status code : {r.text}")

def getroom(token):
    head["authorization"]=token
    head["host"]="tech04.yoha.pro"
    aipi=f'180.{rdm.randint(1,255)}.{rdm.randint(1,255)}.{rdm.randint(1,255)}'
    param1={
        "v":persi,
        "ip":aipi,
        "l":"in"
    }
    uri=f'{data["api"]}live/list?type=0&page=1&per_page=100&last_ids=&v={persi}&ip=180.252.129.{rdm.randint(1,255)}&l=in'
    try:
        r = s.post(uri,params=param1,headers=head,timeout=5)
        if r.status_code==200:
            ressx=(json.loads(r.text))
            ress=[]
            for dtr in ressx["data"]["list"]:
                vuid= dtr["uid"]
                if vuid not in ress:
                    ress.append(dtr)
            return ress
        print(f"{r.text}")
    except Exception as error:
        print(error)
    return 0

def send(token,streamid,tex):
    head["authorization"]=token
    head["host"]="tech04.yoha.pro"
    aipi=f'180.{rdm.randint(1,255)}.{rdm.randint(1,255)}.{rdm.randint(1,255)}'
    param1={
        "stream":streamid,
        "content":tex,
        "v":persi,
        "ip":aipi,
        "l":"in"
    }
    uri=f'{data["api"]}live/sendMsg'
    try:
        r = s.post(uri,data=json.dumps(param1),headers=head,timeout=5)
        if r.status_code==200:
            ressx=(json.loads(r.text))
            return ressx
        print(f"{r.text}")
    except Exception as error:
        print(error)
    return 0
