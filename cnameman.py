import requests
import json
import time
import ambil
import seting,random
import os
import sys
from datetime import datetime

persi = seting.versi()


def nama(x):
    print(x)
    uriweb = "https://wjxwd01mwyo.dt01showxx02.com/App/User_User/Info"
    headers = {
        "user-agent": f"HS-Android Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.17{random.randint(1000,9999)}.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.{random.randint(1000,9999)}.82 Mobile Safari/537.36",
        "bundleidentifier": "user",
        "x-token": x,
        "accept-encoding": "identity",
        "host": "wjxwd01mwyo.dt01showxx02.com",
        "connection": "keep-alive",
    }
    f = requests.get(uriweb, headers=headers)
    ress = json.loads(f.text)
    print(json.dumps(ress, indent=2))
    print("Nickname : " + str(ress["result"]["nickname"]))


def cnama(x, nama):
    uri = "https://wjxwd01mwyo.dt01showxx02.com/App/User_User/UpdateInfo"
    headers = {
        "User-Agent": f"HS-Android Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.17{random.randint(1000,9999)}.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.{random.randint(1000,9999)}.82 Mobile Safari/537.36",
        "BundleIdentifier": "user",
        "X-Token": x,
        "Accept-Encoding": "identity",
        "X-Version": persi,
        "Content-Type": "application/x-www-form-urlencoded",
        "Host": "wjxwd01mwyo.dt01showxx02.com",
        "Connection": "Keep-Alive",
    }
    param = {"nickname": nama}

    try:
        req = requests.post(uri, data=json.dumps(param), headers=headers)
        ress = json.loads(req.text)
        print(ress)
    except:
        print("Failed...")


def capat(x, appat):
    uri = "https://wjxwd01mwyo.dt01showxx02.com/App/User_User/UpdateInfo"
    headers = {
        "User-Agent": f"HS-Android Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.17{random.randint(1000,9999)}.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.{random.randint(1000,9999)}.82 Mobile Safari/537.36",
        "BundleIdentifier": "user",
        "X-Token": x,
        "Accept-Encoding": "identity",
        "X-Version": persi,
        "Content-Type": "application/x-www-form-urlencoded",
        "Host": "wjxwd01mwyo.dt01showxx02.com",
        "Connection": "Keep-Alive",
    }
    param = {"avatar": appat}

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
        "connection": "keep-alive",
    }
    f = requests.get(uriweb, headers=headers)
    ress = json.loads(f.text)
    return ress["result"]


token = ambil.token()

dattop = {}
try:
    mode = int(input("token tdk ada 0: "))-1
except:
    mode = 999

if mode == 999:
    for i in range(len(token)):
        while True:
            klao = input("Nama ke {} : ".format(str(i)))
            if len(klao) > 0 and len(klao) < 25:
                break
        dattop[i] = {"nickname": klao}
    print(str(dattop))

    for i in range(len(token)):
        try:
            print("------------------------>>>> " + str(i))
            nama(token[i])
            cna = dattop[i]["nickname"]
            print("nickbaru : " + cna + str(i))
            cnama(token[i], cna + str(i))
            time.sleep(1)
        except:
            print("Token Expired")
else:
    a = "\u200f"
    b = "ᅠ"
    nama(token[mode])
    cna = input("New Nickname : ")
    # cna += a
    print(f"nickbaru : {cna} {len(cna)}")
    cnama(token[mode], cna)
input()
