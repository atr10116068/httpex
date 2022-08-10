import requests
import sys
import time
import json
import pytz
from datetime import datetime

token = input("Masukkan Token:")


def record():
    dMentah = {}

    def cektoken():
        uriweb = "https://dt001piwfw.d9sph.cn/App/User_User/Info"
        headers = {
            "user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.171019.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36",
            "bundleidentifier": "user",
            "x-token": token,
            "accept-encoding": "identity",
            "host": "dt001piwfw.d9sph.cn",
            "connection": "keep-alive",
        }
        f = requests.get(uriweb, headers=headers)
        ress = json.loads(f.text)
        try:
            checking = ress["result"]["id"]
            return 1
        except:
            print("\nToken Expiret...!")
            return 0

    def susun():
        data = {"results": []}
        try:
            with open(f"bacarat.json", "r") as openfile:
                # Reading from json file
                data = json.load(openfile)
            ppp = data["results"]
            data = {"results": ppp}
        except Exception as e:
            print(str(e))
            exit()

        otput = {"results": []}
        mariSusun = dict(
            sorted(dMentah.items(), key=lambda item: item[1]["game_number"])
        )

        # Serializing json
        json_object = json.dumps(mariSusun, indent=2)
        json_ob = json.loads(json_object)

        for t in data["results"]:
            otput["results"].append(t)

        for x in json_ob:
            if json_ob[x] not in data["results"]:
                print(f"input {json_ob[x]['game_number']}\t\t ")
                otput["results"].append(json_ob[x])

        # Writing to sample.json
        with open("bacarat.json", "w") as outfile:
            outfile.write(json.dumps(otput, indent=2))
        sys.stdout.write("selesai...   \r")
        sys.stdout.flush()

    if cektoken() == 0:
        exit()

    # constant vars
    link = "https://dt001piwfw.d9sph.cn/App/Game_Game/HistoryDrawList"  # URL goes here

    for x in range(1, 2, 1):
        sys.stdout.write(f"\tDownloading page : {x}                    \r")
        sys.stdout.flush()
        headers = {
            "user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.171019.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36",
            "bundleidentifier": "user",
            "x-token": token,
            "accept-identity": "identity",
        }

        hparam = {"game_type": "baijiale_1", "page": str(x)}
        req = requests.get(url=link, params=hparam,
                           headers=headers, timeout=100)
        reqs = json.dumps(req.json())
        reqs = json.loads(reqs)

        status = req.status_code
        req.close()
        if status == 200:
            # print(f"{threadName}: Working page : {proxy['page']}")
            try:
                # print(dtDyn["iterasi"])
                # print(json.dumps(reqs["result"][0], indent=2))
                for x in reqs["result"]:
                    dMentah[x["game_number"]] = x
            except Exception as e:
                # print(f"Error : {e}")
                pass
        else:
            # print(f"{threadName}: Connection Code Status Error:{status}")
            pass
    susun()


dat = {"jam": "", "menit": 0}
while True:
    try:
        tz = pytz.timezone("Asia/Jakarta")
        now = datetime.now(tz)
        dat["jam"] = now.strftime("%d%b%Y-%H:%M:%S")
        menit = now.strftime("%M")
        detik = now.strftime("%S")
        sys.stdout.write(f"\trealtime : {menit}:{detik}                    \r")
        sys.stdout.flush()
        if int(menit) != dat["menit"]:
            time.sleep(5)
            dat["menit"] = int(menit)
            record()
    except Exception as e:
        print("Error : " + str(e))
        for piop in range(60, 1, -1):
            sys.stdout.write(f"\t{piop}                    \r")
            sys.stdout.flush()
            time.sleep(1)
    time.sleep(1)
