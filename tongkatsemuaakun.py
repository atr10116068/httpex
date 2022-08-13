import requests
import json
import seting
import time
import getlive
import ambil
import random
import sys
import random as rd
import colorama
from colorama import Fore, Style, Back

colorama.init()
gip = {}
dat = {"totalgip": 0.0}
persi = seting.versi()

host = "https://wjxwd01mwyo.dt01showxx02.com/"


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
    uri = host+"App/Gift/Buy"
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.171019.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36",
        "BundleIdentifier": "user",
        "X-Token": x,
        "Accept-Encoding": "identity",
        "X-Version": persi,
        "Content-Type": "application/x-www-form-urlencoded",
        "Content-Length": "33",
        "Host": "dt001piwfw.d9sph.cn",
        "Connection": "Keep-Alive",
    }
    param = {"live_id": id, "gift_id": gif, "number": "1"}

    try:
        req = requests.post(uri, data=json.dumps(param), headers=headers)
        ress = json.loads(req.text)
        print(f'sisah di akun : {ress}')
    except Exception as e:
        print("Failed... :"+str(e))


def sentxt(id, tok, tex):
    uri = host + "App/Live/SendMsg"
    headers = {
        "user-agent": "HS-Android Mozilla/5.0 (Linux; Android 8.5.0; Redmi 2 Plus Build/OPM1.171019.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4638.50 Mobile Safari/537.36",
        "bundleidentifier": "user",
        "x-token": tok,
        "accept-encoding": "identity",
        "x-version": persi,
        "connection": "keep-alive",
    }
    para = {"live_id": id, "content": tex}

    req = requests.get(uri, params=para, headers=headers)
    ress = json.loads(req.text)
    return ress


def main(ttt):
    room = getlive.roomall()
    x = 1
    for i in room:
        print("{}. {}".format(str(x), i["nickname"]))
        x += 1

    inp = input("room nomor : ")
    idroom = room[int(inp) - 1]["live_id"]
    print("\nTarget Room : " + room[int(inp) - 1]["nickname"])

    token = ambil.token()[0:100]

    if ttt != "cok":
        token = [token[int(ttt) - 1]]

    for i in token:
        sen(idroom, "3", i)
        # sentxt(idroom, i, "numpang lewat")
        time.sleep(0.1)#random.randint(7, 15))

    print("selesai...")


try:
    tehj = sys.argv[1]
    print(tehj)
    main(tehj)
except:
    main("cok")
