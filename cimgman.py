import requests
import json,random
import time
import os
import sys
import ambil
from datetime import datetime


# pap baby dari bang kais  user/header/20220127/1643221226749_1772703.png
def nama(x):
    uriweb = "https://wjxwd01mwyo.dt01showxx02.com/App/User_User/Info"
    headers = {
        "user-agent": f"HS-Android Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.17{random.randint(1000,9999)}.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.{random.randint(1000,9999)}.82 Mobile Safari/537.36",
        "bundleidentifier": "user",
        "x-token": x,
        "accept-encoding": "identity",
        "host": "wjxwd01mwyo.dt01showxx02.com",
        "connection": "keep-alive"
    }
    f = requests.get(uriweb, headers=headers)
    ress = json.loads(f.text)
    print("Nickname : "+ress["result"]["nickname"])


def cimg(x, img):
    uri = "https://wjxwd01mwyo.dt01showxx02.com/App/User_User/UpdateInfo"
    headers = {
        "User-Agent": f"HS-Android Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.17{random.randint(1000,9999)}.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.{random.randint(1000,9999)}.82 Mobile Safari/537.36",
        "BundleIdentifier": "user",
        "X-Token": x,
        "Accept-Encoding": "identity",
        "X-Version": "2.10.4",
        "Content-Type": "application/x-www-form-urlencoded",
        "Host": "wjxwd01mwyo.dt01showxx02.com",
        "Connection": "Keep-Alive"
    }
    param = {
        "avatar": img
    }

    # try:
    req = requests.post(uri, data=json.dumps(param), headers=headers)
    ress = json.loads(req.text)
    return(ress)
    # except:
    #     return("Failed...")


def capat(x, appat):
    uri = "https://wjxwd01mwyo.dt01showxx02.com/App/User_User/UpdateInfo"
    headers = {
        "User-Agent": f"HS-Android Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.17{random.randint(1000,9999)}.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.{random.randint(1000,9999)}.82 Mobile Safari/537.36",
        "BundleIdentifier": "user",
        "X-Token": x,
        "Accept-Encoding": "identity",
        "X-Version": "2.10.4",
        "Content-Type": "application/x-www-form-urlencoded",
        "Host": "wjxwd01mwyo.dt01showxx02.com",
        "Connection": "Keep-Alive"
    }
    param = {
        "avatar": appat
    }

    try:
        req = requests.post(uri, data=json.dumps(param), headers=headers)
        ress = json.loads(req.text)
        print(ress)
    except:
        print("Failed...")


def topnama(x):
    uriweb = "https://wjxwd01mwyo.dt01showxx02.com/App/Rankings/GetRechargeList?time_type=month&is_last=1"
    headers = {
        "user-agent": f"HS-Android Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.17{random.randint(1000,9999)}.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.{random.randint(1000,9999)}.82 Mobile Safari/537.36",
        "bundleidentifier": "user",
        "x-token": x,
        "accept-encoding": "identity",
        "host": "wjxwd01mwyo.dt01showxx02.com",
        "connection": "keep-alive"
    }
    f = requests.get(uriweb, headers=headers)
    ress = json.loads(f.text)
    return ress["result"]


token = ambil.token()

dattop = {}
try:
    mode = int(input("token no:"))-1
    print(mode)
except:
    mode = 999

if mode == 999:
    klao = input("avatar ke {} : ".format(str(i)))
    for i in range(len(token)):
        while True:
            if len(klao) > 0 and len(klao) < 50:
                break
        dattop[i] = {"nickname": klao}
    print(str(dattop))

    for i in range(len(token)):
        try:
            print("------------------------>>>> "+str(i))
            nama(token[i])
            cna = dattop[i]["nickname"]
            print("avatar : "+cna)
            cimg(token[i], cna)
            time.sleep(1)
        except:
            print("Token Expired")
else:
    print("single mode")
    nama(token[mode])
    cna = input("avatar : ")
    print("avatar : "+cna)
    print(cimg(token[mode], cna))
