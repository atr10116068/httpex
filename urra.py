import requests
import json
import random
import time
import getlive
import threading
import ambil
import sys
import random as rd

gip = {}


def masok(aidi, x, zx):
    uriweb = "https://wjxwd01mwyo.dt01showxx02.com/App/Live/SendMsg"
    headers = {
        "user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.171019.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36",
        "bundleidentifier": "user",
        "x-token": x,
        "accept-encoding": "identity",
        "host": "wjxwd01mwyo.dt01showxx02.com",
        "connection": "keep-alive",
    }
    param = {"live_id": aidi, "content": zx}
    try:
        f = requests.get(uriweb, params=param, headers=headers)
        ress = json.loads(f.text)
        return ress
    except Exception as e:
        print("error : " + str(e))


def nama(x):
    uriweb = "https://wjxwd01mwyo.dt01showxx02.com/App/User_User/Info"
    headers = {
        "user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.171019.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36",
        "bundleidentifier": "user",
        "x-token": x,
        "accept-encoding": "identity",
        "host": "wjxwd01mwyo.dt01showxx02.com",
        "connection": "keep-alive",
    }
    f = requests.get(uriweb, headers=headers)
    ress = json.loads(f.text)
    try:
        # print("Nickname: "+str(ress["result"]))
        pass
    except:
        print("error")


def main():
    room = getlive.roomall()
    x = 1
    for i in room:
        print("{}. {}".format(str(x), i["nickname"]))
        x += 1

    inp = input("room nomor : ")
    idroom = room[int(inp) - 1]["live_id"]
    print("\nTarget Room : " + room[int(inp) - 1]["nickname"])

    token = ambil.token()

    def doreq():
        masok(idroom, random.choice(token), dat["text"])

    while True:
        dat = {"text": input("text : "), "total": input("jum akun : ")}
        threads = []
        for i in range(int(dat["total"])):
            t = threading.Thread(target=doreq)
            t.daemon = True
            threads.append(t)
        for i in range(int(dat["total"])):
            threads[i].start()
        for i in range(int(dat["total"])):
            threads[i].join()


main()
