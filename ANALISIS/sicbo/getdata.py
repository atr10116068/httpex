import requests
import sys
import time
import json


def record():
    dMentah = {}

    def susun():
        data = {"results": []}
        try:
            with open(f"sicbo.json", "r") as openfile:
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
                print(f"input {json_ob[x]['game_number']}")
                otput["results"].append(json_ob[x])

        # Writing to sample.json
        with open("sicbo.json", "w") as outfile:
            outfile.write(json.dumps(otput, indent=2))
        sys.stdout.write("selesai...   \r")
        sys.stdout.flush()

    with open("user_token.json") as json_file:
        tokk = json.load(json_file)
    token = tokk["results"][1]

    # constant vars
    link = "https://dt001piwfw.d9sph.cn/App/Game_Game/HistoryDrawList"  # URL goes here

    for x in range(1, 10, 1):
        sys.stdout.write(f"\tDownloading page : {x}                    \r")
        sys.stdout.flush()
        headers = {
            "user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.171019.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36",
            "bundleidentifier": "user",
            "x-token": token,
            "accept-identity": "identity",
        }

        hparam = {"game_type": "toubao_1", "page": str(x)}
        req = requests.get(url=link, params=hparam, headers=headers, timeout=100)
        reqs = json.dumps(req.json())
        reqs = json.loads(reqs)

        status = req.status_code
        req.close()
        if status == 200:
            # print(f"{threadName}: Working page : {proxy['page']}")
            try:
                # print(dtDyn["iterasi"])
                for x in reqs["result"]:
                    dMentah[x["game_number"]] = x
            except Exception as e:
                # print(f"Error : {e}")
                pass
        else:
            # print(f"{threadName}: Connection Code Status Error:{status}")
            pass
    susun()


while True:
    try:
        record()
        for piop in range(500, 1, -1):
            sys.stdout.write(f"\t{piop}                    \r")
            sys.stdout.flush()
            time.sleep(1)
    except:
        print("Error koneksi")
        for piop in range(60, 1, -1):
            sys.stdout.write(f"\t{piop}                    \r")
            sys.stdout.flush()
            time.sleep(1)

