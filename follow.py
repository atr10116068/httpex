import requests
import seting
import json
import time
import ambil
import getlive
import random as rd


x = getlive.roomall()
for i in x:
    print(f'{i["live_id"]}:{i["nickname"]}')

live_id = input("live_id :")
show_id = input("show_id :")


def sen(x, liveid, showid):
    uri = "https://wjxwd01mwyo.dt01showxx02.com/App/Attention/Add"
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.171019.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36",
        "BundleIdentifier": "user",
        "X-Token": x,
        "Accept-Encoding": "identity",
        "X-Version": seting.versi(),
        "Content-Type": "application/x-www-form-urlencoded",
        "Host": "wjxwd01mwyo.dt01showxx02.com",
        "Connection": "Keep-Alive",
    }
    param = {"show_id": str(showid), "live_id": str(liveid)}

    try:
        req = requests.post(uri, data=json.dumps(param), headers=headers)
        ress = json.loads(req.text)
        print(ress)
        return(ress)
    except:
        print("Failed...")


def main():
    tokens = ambil.token()
    itr = "."
    for (
        token
    ) in (
        tokens
    ):  # https://wjxwd01mwyo.dt01showxx02.com/App/Live/UserInfo?show_id=&live_id=141207
        # if sen(token, live_id, show_id)["code"] == 0:
        #     time.sleep(0.1)  # random.randint(1, 7))
        # else:
        #     input(":")
        sen(token, live_id, show_id)
        time.sleep(0.8)
    exit()


main()
