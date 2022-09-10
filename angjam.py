from datetime import datetime
import requests
import threading
import json
import random
import time
import sys
import pytz
import ambil


# constant vars
claim = "https://wjxwd01mwyo.dt01showxx02.com/App/RedPacket/SystemReceive"  # URL goes here

# req proxy list
# proxreq = requests.get(
#     "https://www.proxy-list.download/api/v1/get?type=https")
# result = proxreq.text
# result = result.replace(chr(10), "").replace(chr(13), "x")
# proxies = result.split("x")
# print(proxies)

# dynamic vars
threadLock = threading.Lock()
threads = []
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
        # print(ress["msg"]) #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<   Penting
        if status == 200:
            # f"{threadName}: Working request with proxy: {proxy['proxy']}")
            if ress["msg"] not in indicat:
                # print(f'{threadName} Error : {ress["msg"]}')
                try:
                    koin = float(ress["result"]["amount"])
                    dat["tot"] += koin
                    datan["totalakun"] += 1
                    datan["totaljam"] += koin
                    # print(f'{dat["token"].index(headers["X-Token"])} dapat : {koin}')
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
    if menit == "00" and detik == "10":
        print(f"claim ter-Unlock {dat['jam']}")
        dat["claim"] = True
    else:
        sys.stdout.write(f"  {dat['jam']} \r")
        sys.stdout.flush()


def proces():
    class myThread(threading.Thread):
        def __init__(self, threadID, name, counter, proxy):
            threading.Thread.__init__(self)
            self.threadID = threadID
            self.name = name
            self.counter = counter
            self.proxy = proxy

        def run(self):
            # print("Starting " + self.name)
            spam(self.name, proxy)

    num = 0
    while len(dat["token"]) > 0:
        thread = str(num)
        num += 1
        # prox = random.choice(proxies).strip()
        x = random.choice(dat["token"])
        proxy = {
            # "proxy": {
            #     "https": prox
            # },
            "headers": {
                "user-agent": f"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.{random.randint(100000,999999)}.{random.randint(100,999)}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.{random.randint(1000,9999)}.{random.randint(100,999)} Mobile Safari/537.36",
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
        thread = myThread(thread, "Thread-" + thread, num, proxy)
        thread.start()
        time.sleep(0.1)

    # Wait for all threads to complete
    for t in threads:
        t.join()


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
            tokk = ambil.token()
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
