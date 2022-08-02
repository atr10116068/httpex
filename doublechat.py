import requests
import json
import time
import getlive
import sys
import ambil
import random as rd

gip = {}


def nama(x):
    uriweb = "https://wjxwd01mwyo.dt01showxx02.com/App/User_User/Info"
    headers = {
        "user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.171019.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36",
        "bundleidentifier": "user",
        "x-token": x,
        "accept-encoding": "identity",
        "host": "wjxwd01mwyo.dt01showxx02.com",
        "connection": "keep-alive"
    }
    f = requests.get(uriweb, headers=headers)
    ress = json.loads(f.text)
    try:
        print("Nickname: "+ress["result"]["nickname"])
        return 1
    except:
        print("Token Expiret")
        return 0


def sen(id, tok, tex):
    uri = "https://wjxwd01mwyo.dt01showxx02.com/App/Live/SendMsg"
    headers = {
        "user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.171019.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36",
        "bundleidentifier": "user",
        "x-token": tok,
        "accept-encoding": "identity",
        "host": "wjxwd01mwyo.dt01showxx02.com",
        "connection": "keep-alive"
    }
    para = {"live_id": id, "content": tex}

    req = requests.get(uri, params=para, headers=headers)
    ress = json.loads(req.text)
    return ress


def main(ttt):
    room = []
    filtname = []
    for p in getlive.roomall():
        if p["nickname"] not in filtname:
            room.append(p)
    x = 1
    for i in room:
        print("{}. {}".format(str(x), i["nickname"]))
        x += 1

    inp = input("room nomor [no no]: ")
    inp = inp.split(" ")
    idroom = []
    idroom.append(room[int(inp[0])-1]["live_id"])
    idroom.append(room[int(inp[1])-1]["live_id"])
    print("\nTarget Room : "+room[int(inp[0])-1]
          ["nickname"]+"&"+room[int(inp[1])-1]["nickname"])

    token = ambil.token()[int(ttt)-1]

    while True:
        print()
        nama(token)
        tex = input(" : ")
        if tex == "q":
            break
        if tex.startswith("1"):
            sen(idroom[0], token, tex.replace("1", ""))
        elif tex.startswith("2"):
            sen(idroom[1], token, tex.replace("2", ""))
        else:
            for idny in idroom:
                sen(idny, token, tex)

    print("selesai...")


try:
    tehj = input("token no : ")
    print(tehj)
    main(tehj)
except Exception as e:
    print("app.py [token]")
    print(str(e))
