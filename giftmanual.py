import requests
import seting
import json
import time
import getlive
import ambil
import sys
import random as rd
import colorama
from colorama import Fore, Style, Back

colorama.init()
gip = {}
dat = {"totalgip": 0.0}


def c(colr, tex, dim):
    try:
        w = {
            "BLACK": Fore.BLACK,
            "RED": Fore.RED,
            "GREEN": Fore.GREEN,
            "YELLOW": Fore.YELLOW,
            "BLUE": Fore.BLUE,
            "MAGENTA": Fore.MAGENTA,
            "CYAN": Fore.CYAN,
            "WHITE": Fore.WHITE,
            "RESET": Fore.RESET,
        }
        if dim == 1:
            return f"{Style.DIM}{w[colr.upper()]} {tex} {Style.RESET_ALL}"
        else:
            return f"{w[colr.upper()]} {tex} {Style.RESET_ALL}"
    except:
        return tex


def sen(id, gif, x):
    uri = "https://wjxwd01mwyo.dt01showxx02.com/App/Gift/Buy"
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.171019.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36",
        "BundleIdentifier": "user",
        "X-Token": x,
        "Accept-Encoding": "identity",
        "X-Version": seting.versi(),
        "Content-Type": "application/x-www-form-urlencoded",
        "Content-Length": "33",
        "Host": "wjxwd01mwyo.dt01showxx02.com",
        "Connection": "Keep-Alive",
    }
    param = {"live_id": id, "gift_id": gif, "number": "1"}

    try:
        for i in gip["result"]:
            if i["id"] == gif:
                print(f'Send... {i["name"]} [{i["price"]}] coin')
                dat["totalgip"] += float(i["price"])
        req = requests.post(uri, data=json.dumps(param), headers=headers)
        ress = json.loads(req.text)
        print(f'sisah di akun : {ress["result"]["balance"]}')
    except:
        print("Failed... request")


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
        nem = ress["result"]["nickname"]
        bele = float(ress["result"]["balance"])
        return [nem, bele, 1]
    except:
        print("Token Expiret")
        return [0, 0, 0]


def getgift(x):
    uriweb = "https://wjxwd01mwyo.dt01showxx02.com/App/Gift/List"
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
    gip["result"] = ress["result"]


def main(ttt):
    room = getlive.roomall()
    x = 1
    for i in room:
        print("{}. {}".format(str(x), i["nickname"]))
        x += 1

    inp = input("room nomor : ")
    idroom = room[int(inp) - 1]["live_id"]
    print("\nTarget Room : " + room[int(inp) - 1]["nickname"])

    token = ambil.token()

    if ttt != "cok":
        token = [token[int(ttt) - 1]]

    for i in token:
        if len(gip) == 0:
            getgift(i)
        while True:
            print(c("MAGENTA", f'\nTotal gift : {dat["totalgip"]}', 0))
            getinf = nama(i)
            if getinf[2] == 1:
                print(f'Nickname: {getinf[0]}')
                if getinf[1] < 0.0:
                    break
                print(f"Balance : {getinf[1]}")
                typegift = input("gift id: ")
                if typegift == "q":
                    break
                sen(idroom, typegift, i)

    print("selesai...")


try:
    tehj = input("token no : ")
    print(tehj)
    main(tehj)
except:
    main("cok")
