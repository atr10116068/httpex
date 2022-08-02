import requests
import json
import seting
import getlive
import time
import ambil
import threading


dat = {"aidi": ""}
persi = seting.versi()


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
        print("Nickname: " + ress["result"]["nickname"])
    except:
        print("token expired")


def main():
    room = getlive.roomall()
    x = 1
    for i in room:
        print("{}. {}".format(str(x), i["nickname"]))
        x += 1

    inp = input("room nomor : ")
    dat["aidi"] = room[int(inp) - 1]["live_id"]
    print("\nTarget Room : " + room[int(inp) - 1]["nickname"])

    numtkn = input("token ke ")
    dat["token"] = ambil.token()[int(numtkn) - 1]
    nama(dat["token"])

    def doreq():
        uri = "https://wjxwd01mwyo.dt01showxx02.com/App/Gift/Buy"
        headers = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.171019.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36",
            "BundleIdentifier": "user",
            "X-Token": dat["token"],
            "Accept-Encoding": "identity",
            "X-Version": persi,
            "Content-Type": "application/x-www-form-urlencoded",
            "Content-Length": "33",
            "Host": "wjxwd01mwyo.dt01showxx02.com",
            "Connection": "Keep-Alive",
        }
        param = {"live_id": dat["aidi"], "gift_id": "3", "number": "1"}
        try:
            while True:
                req = requests.post(
                    uri, data=json.dumps(param), headers=headers)
                ress = json.loads(req.text)
                if ress["code"] != 0:
                    break
                if float(ress["result"]["balance"]) < 0.10:
                    exit()
                print(ress)
                # time.sleep(0.7)
        except:
            print("error basreng")
            exit()

    while True:
        try:
            threads = []

            for i in range(10):
                t = threading.Thread(target=doreq)
                t.daemon = True
                threads.append(t)

            for i in threads:
                # time.sleep(3)
                i.start()

            for i in threads:
                i.join()
        except Exception as e:
            print(f"eror : {e}")


main()
