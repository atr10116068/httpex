import requests
import json
import sys
import time
import getlive
import seting
import random


def nama(x):
    uriweb = "https://wjxwd01mwyo.dt01showxx02.com/App/User_User/Info"
    headers = {
        "User-Agent": f"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.{random.randint(100000,999999)}.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.{random.randint(1000,9999)}.120 Mobile Safari/537.36",
        "bundleidentifier": "user",
        "x-token": x,
        "accept-encoding": "identity",
        "host": "dt001piwfw.d9sph.cn",
        "connection": "keep-alive",
    }
    f = requests.get(uriweb, headers=headers)
    try:
        ress = json.loads(f.text)
        nem = ress["result"]["nickname"]
        bele = float(ress["result"]["balance"])
        return [nem, bele, 1]
    except:
        print("Token Expiret")
        return [0, 0, 0]


def sen(dat,itrx):
    uri = "https://wjxwd01mwyo.dt01showxx02.com/App/Gift/BuyRemoteGift"
    headers = {
        "User-Agent": f"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.{random.randint(100000,999999)}.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.{random.randint(1000,9999)}.120 Mobile Safari/537.36",
        "BundleIdentifier": "user",
        "X-Token": dat["token"][itrx],
        "Accept-Encoding": "identity",
        "X-Version": seting.versi(),
        "Content-Type": "application/x-www-form-urlencoded",
        "Host": "wjxwd01mwyo.dt01showxx02.com",
        "Connection": "Keep-Alive",
    }
    param = {"live_id": dat["idroom"], "number": "1"}

    req = requests.post(uri, data=json.dumps(param), headers=headers)
    try:
        ress = json.loads(req.text)
        print(ress)
    except:
        print(f"Error : {req.text}")


room = getlive.roomall()

tkn1,tkn2=int(input("tkn1:")),int(input("tkn2:"))
dat = {"token": [], "idroom": ""}
import ambil
tokk = ambil.token()
token = tokk
itr=tkn1
for tyk in token[tkn1:tkn2]:
    cef=nama(tyk)
    itr+=1
    if cef[1]>2:
        dat["token"].append(tyk)
        print(f"{itr}. {cef}")
    else:
        sys.stdout.write(f"{itr}. {cef}\r")
        sys.stdout.flush()
    time.sleep(4)
x = 1
for i in room:
    print("{}. {}".format(str(x), i["nickname"]))
    x += 1
inp = input("room nomor : ")
idroom = room[int(inp) - 1]["live_id"]
dat["idroom"]=idroom
print("\nTarget Room : " + room[int(inp) - 1]["nickname"])
# token = tokk[xxx-1:xxx]



while True:
    itrr=0
    gk = input("q to exit: ")
    if gk=="q":
        break
    for tknn in range(len(dat["token"])):
        gkl = input(f"{itrr}/{len(dat['token'])}. y or n : ")
        if gkl == "y":
            sen(dat,itrr)
        elif gkl == "q":
            break
        else:
            pass
        itrr+=1
    print("selesai...")


