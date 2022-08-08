import requests
import json
import time
import getlive
import seting
import pytz
import ambil
import sys
from datetime import datetime

persi = seting.versi()
dat = {"jam": 0, "claim": False, "blokjam": [], "counting": 0,
       "countTarget": int(input("Target count :"))}
betamount = int(input("bet Amount : "))


def jam():
    tz = pytz.timezone("Asia/Jakarta")
    now = datetime.now(tz)
    dat["jam"] = now.strftime("%d%b%Y-%H:%M:%S")
    detik = now.strftime("%S")
    if detik == "10":
        print(f"claim ter-Unlock {dat['jam']}")
        dat["claim"] = True
    else:
        sys.stdout.write(f"  {dat['jam']}  count:{dat['counting']}\r")
        sys.stdout.flush()

    if dat['counting'] > dat['countTarget']:
        exit()


def getnum(x):
    uri = "https://wjxwd01mwyo.dt01showxx02.com/App/Game_Game/GetTypeInfo"
    headers = {
        "user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.171019.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36",
        "bundleidentifier": "user",
        "x-token": x,
        "accept-encoding": "identity",
        "x-version": persi,
        "host": "wjxwd01mwyo.dt01showxx02.com",
        "connection": "keep-alive",
    }
    query = {"game_type": "baijiale_1"}
    req = requests.get(uri, params=query, headers=headers)
    ress = json.loads(req.text)
    try:
        return ress["result"]["current_round"]["number"]
    except:
        print("return error")


def bet(x, type, num):
    gamenum=getnum(x)
    print(gamenum)
    rType = {
        "player": "zhuangxian_xian",
        "banker": "zhuangxian_zhuang",
        "tie": "zhuangxian_he"
    }
    uri = "https://wjxwd01mwyo.dt01showxx02.com/App/Game_Order/Create"
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.171019.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36",
        "BundleIdentifier": "user",
        "X-Token": x,
        "Accept-Encoding": "identity",
        "X-Version": persi,
        "Content-Type": "application/x-www-form-urlencoded",
        "Content-Length": "123",
        "Host": "wjxwd01mwyo.dt01showxx02.com",
        "Connection": "Keep-Alive",
    }
    param = {
        "live_room_id": "",
        "game_type": "baijiale_1",
        "game_sub": "zhuangxian",
        "game_number": gamenum,
        "detail": rType[type] + ":" + num,
        "multiple": "1",
    }
    try:
        req = requests.post(uri, data=json.dumps(param), headers=headers)
        ress = json.loads(req.text)
        dat["counting"] += betamount
        print(ress)
    except Exception as e:
        print(f"Failed : {e}")


token = ambil.token()
nomer = input("Token no :")
betnya = input("betnya :")
tz = pytz.timezone("Asia/Jakarta")
now = datetime.now(tz)
jamm = now.strftime("%m/%d/%Y, %H:%M")
print(f"\t\tstart in [ {jamm} ]")
while True:
    try:
        jam()

        if dat["claim"] == True:
            datan = {"totaljam": 0, "totalakun": 0}
            print(">claim is true")
            tokk = ambil.token()
            dat["token"] = tokk
            if str(dat["jam"])[0:11] not in dat["blokjam"]:
                dat["claim"] = False
                print(">lolos backup waktu")

                tkn = token[int(nomer)-1]
                bet(tkn, betnya, str(betamount))
                print()
                time.sleep(2)
    except Exception as e:
        print(f"Error : [{dat['jam']}] {e}")
        for x in range(1, 120):
            sys.stdout.write(f"{x}\r")
            sys.stdout.flush()
            time.sleep(1)

    time.sleep(0.1)
