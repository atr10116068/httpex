from datetime import datetime
import requests
import json
import random
import time
import sys
import pytz
import ambil


# constant vars
claim = "https://wjxwd01mwyo.dt01showxx02.com/App/RedPacket/SystemReceive"  # URL goes here

num = 0

dat = {"jam": 0, "claim": False, "blokjam": [], "tot": 0.0}
datan = {}
# Each thread runs this function once


def spam(threadName, proxy):
    indicat = [
        "gagal",
        "The red envelope has been collected and cannot be collected again",
        "Failed to grab the red envelope",
        "The account has been logged in to other devices",
        "VIP level not up to standard, unable to receive",
    ]
    try:
        headers = proxy["headers"]
        param = {"type": "1", "live_room_id": ""}
        # req = requests.post(claim, data=json.dumps(param), headers=headers,
        #                     proxies=proxy["proxy"], timeout=100)
        req = requests.post(claim, data=json.dumps(param),
                            headers=headers, timeout=100)
        ress = json.dumps(req.json())
        ress = json.loads(ress)

        status = req.status_code
        req.close()
        # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<   Penting
        print(ress["msg"])
        if status == 200:
            # f"{threadName}: Working request with proxy: {proxy['proxy']}")
            if ress["msg"] not in indicat:
                # print(f'{threadName} Error : {ress["msg"]}')
                try:
                    koin = float(ress["result"]["amount"])
                    dat["tot"] += koin
                    datan["totalakun"] += 1
                    datan["totaljam"] += koin
                    dat["token"].pop(indexhapus)
                    print(
                        f'{dat["token"].index(headers["X-Token"])} dapat : {koin}')
                except:
                    pass
            else:
                # print(f'{threadName} Error in indicat: {ress["msg"]}')
                try:
                    indexhapus = dat["token"].index(headers["X-Token"])
                    dat["token"].pop(indexhapus)
                except:
                    pass
            sys.stdout.write(f'{len(dat["token"])}    \r')
            sys.stdout.flush()

        else:
            print(f"{threadName}: Connection Code Status Error:{status}")
    except IOError as e:
        indexhapus = dat["token"].index(headers["X-Token"])
        dat["token"].pop(indexhapus)
        print(f"{threadName}: Connection error : {e}")


try:
    if sys.argv[1] == "t":
        print("test mode")
    else:
        print("app.py t")
        exit()
    test = True
except:
    test = False


def jam():
    tz = pytz.timezone("Asia/Jakarta")
    now = datetime.now(tz)
    dat["jam"] = now.strftime("%d%b%Y-%H:%M:%S")
    menit = now.strftime("%M")
    detik = now.strftime("%S")
    if menit == "00" and detik == "01":
        print(f"claim ter-Unlock {dat['jam']}")
        dat["claim"] = True
    else:
        sys.stdout.write(f"  {dat['jam']} \r")
        sys.stdout.flush()


def proces():
    num = 0
    for x in dat["token"]:
        thread = str(num)
        num += 1
        # prox = random.choice(proxies).strip()
        proxy = {
            # "proxy": {
            #     "https": prox
            # },
            "headers": {
                "User-Agent": "HS-Android Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.171019.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4638.50 Mobile Safari/537.36",
                "BundleIdentifier": "user",
                "X-Token": x,
                "Accept-Encoding": "identity",
                "X-Version": "2.10.4",
                "Content-Type": "application/x-www-form-urlencoded",
                "Content-Length": "25",
                "Host": "wjxwd01mwyo.dt01showxx02.com",
                "Connection": "Keep-Alive",
            }
        }
        spam(thread, proxy)
        time.sleep(0.1)
        input("Tekan enter untuk lanjut ke {num}")


tz = pytz.timezone("Asia/Jakarta")
now = datetime.now(tz)
jamm = now.strftime("%m/%d/%Y, %H:%M")
print(jamm)
while True:
    try:
        if test == True:
            dat["claim"] = True
            test = False
            print("testing...")
        jam()

        if dat["claim"] == True:
            datan = {"totaljam": 0, "totalakun": 0}
            print(">claim is true")

            with open("user_token.json") as json_file:
                tokk = json.load(json_file)["results"]
            dat["token"] = tokk
            if str(dat["jam"])[0:11] not in dat["blokjam"]:
                dat["claim"] = False
                print(">lolos backup waktu")
                proces()
                print(
                    f'total coin : {dat["tot"]}\tdapat/jam : {datan["totalakun"]} akun\tcoin jam : {datan["totaljam"]}'
                )
    except Exception as e:
        print(f"Error : [{dat['jam']}] {e}")
        for x in range(1, 120):
            sys.stdout.write(f"{x}\r")
            sys.stdout.flush()
            time.sleep(1)

    time.sleep(0.1)
