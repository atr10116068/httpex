import requests
import json
import time
import getlive
import sys
import seting
import random
import random as rd
import threading


def nama(x):
    uriweb = "https://wjxwd01mwyo.dt01showxx02.com/App/User_User/Info"
    headers = {
        "User-Agent": f"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.{random.randint(100000,999999)}.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.{random.randint(1000,9999)}.120 Mobile Safari/537.36",
        "bundleidentifier": "user",
        "x-token": x,
        "accept-encoding": "identity",
        "host": "dt001piwfw.d9sph.cn",
        "connection": "keep-alive",
    }
    f = requests.get(uriweb, headers=headers)
    ress = json.loads(f.text)
    try:
        nem = ress["result"]["nickname"]
        bele = float(ress["result"]["balance"])
        return [nem, bele, 1]
    except:
        print("Token Expiret")
        return [0, 0, 0]


def sen(id, x):
    uri = "https://wjxwd01mwyo.dt01showxx02.com/App/Gift/BuyRemoteGift"
    headers = {
        "User-Agent": f"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.{random.randint(100000,999999)}.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.{random.randint(1000,9999)}.120 Mobile Safari/537.36",
        "BundleIdentifier": "user",
        "X-Token": x,
        "Accept-Encoding": "identity",
        "X-Version": seting.versi(),
        "Content-Type": "application/x-www-form-urlencoded",
        "Host": "dt001piwfw.d9sph.cn",
        "Connection": "Keep-Alive",
    }
    param = {"live_id": id, "number": "1"}

    try:
        req = requests.post(uri, data=json.dumps(param), headers=headers)
        ress = json.loads(req.text)
        print(ress)
    except:
        print("Failed...")


def main(xxx):
    room = getlive.roomall()
    x = 1
    for i in room:
        print("{}. {}".format(str(x), i["nickname"]))
        x += 1
    inp = input("room nomor : ")
    idroom = room[int(inp) - 1]["live_id"]
    print("\nTarget Room : " + room[int(inp) - 1]["nickname"])
    import ambil
    tokk = ambil.token()
    token = tokk
    # token = tokk[xxx-1:xxx]

    dat = {"token": token[0], "idroom": idroom}
    print(nama(dat["token"]))

    for i in token:
        gkl = input("y or n : ")
        if gkl == "y":
            sen(idroom, i)
        else:
            pass
    print("selesai...")


x = input("tkn no : ")
main(int(x))
