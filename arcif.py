import json
import seting
import requests
import sys
import ambil
import time


force36 = True
dat = {"itr": 1}
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
        return 1
    except:
        print("Token Expiret")
        return 0


def getlist(x):
    uriweb = "https://wjxwd01mwyo.dt01showxx02.com/App/Achievement_AchievementApi/List"
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

    return ress


def reciv(x, tipe, level):
    uri = "https://wjxwd01mwyo.dt01showxx02.com/App/Achievement_AchievementApi/Receive"
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.171019.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36",
        "BundleIdentifier": "user",
        "X-Token": x,
        "Accept-Encoding": "identity",
        "X-Version": persi,
        "Content-Type": "application/x-www-form-urlencoded",
        "Content-Length": "14",
        "Host": "wjxwd01mwyo.dt01showxx02.com",
        "Connection": "Keep-Alive",
    }
    # print(f"tipe {tipe}\nlevel {level}")
    param = {"type": int(tipe), "level": int(level)}
    # param="type=3&level=1"

    try:
        req = requests.post(uri, data=json.dumps(param), headers=headers)
        ress = json.loads(req.text)
        return ress
    except:
        return "Failed..."


def cek(tkn):
    data = getlist(tkn)
    for i in data["result"]["data"]:
        print()
        print(i)
        for ii in data["result"]["data"][i]:
            type = ii["type"]
            receive = ii["is_receive"]
            if receive == 1:
                # print(f"type : {type}\ntutup")
                pass
            else:
                print(f"type : {type}\n{ii}")


def klaim(tkn, lvl):
    nama(tkn)
    lis = getlist(tkn)

    lisny = ["basic", "live", "game"]

    if force36 == True:
        for i in range(1, len(token), 1):
            cek = reciv(tkn, i, int(lvl))
            print(f'{dat["itr"]}. {cek["msg"]}')
            time.sleep(0.01)
    else:
        for typ in lisny:
            # print(typ)
            for id in lis["result"]["data"][typ]:
                cek = reciv(tkn, id["type"], int(lvl))
                print(cek)
                time.sleep(0.01)


token = ambil.token()

moddd1 = """\tmode
c=cek
r=recive
:"""
moddd2 = """\ttoken
1
1-5
all
:"""
moddd3 = """\tlevel
1
2
3
:"""

try:
    modd = input(moddd1)
    lvl = input(moddd3)
except:
    exit()

inp = input(moddd2)

if "-" in inp:
    aw, ak = int(inp.split("-")[0])-1, int(inp.split("-")[1])
    tkn = token[aw:ak]
    if modd == "c":
        try:
            dat['itr'] = aw-1
            for i in tkn:
                dat['itr'] += 1
                print(f"c> {dat['itr']}")
                cek(i)
                time.sleep(5)
        except Exception as e:
            print(f"error cek : {e}")
    elif modd == "r":
        try:
            dat['itr'] = aw-1
            for i in tkn:
                dat['itr'] += 1
                print(0.1)
                print(f"r> {dat['itr']}")
                print(0.1)
                klop = klaim(i, lvl)
                print(0.1)
                time.sleep(0.1)
        except Exception as e:
            print(f"error claim : {e}")
elif inp == "all":
    tkn = token
    # print(tkn)
    if modd == "c":
        try:
            for i in range(len(tkn)):
                print(f"c> {i}")
                tkn = token[i]
                cek(tkn)
                time.sleep(5)
        except Exception as e:
            print(f"error cek : {e}")
    elif modd == "r":
        try:
            for i in range(len(tkn)):
                for lvl in range(1, int(lvl)+1):
                    print(f"r> {i}  {lvl}")
                    tkn = token[i]
                    klop = klaim(tkn, lvl)
                    dat["itr"] += 1
                    time.sleep(1)
        except Exception as e:
            print(f"error claim : {e}")
else:
    print("single mode")
    tkn = token[int(inp)-1: int(inp)]
    print(str(tkn))
    print("manual")
    if modd == "c":
        cek(tkn[0])
    elif modd == "r":
        klaim(tkn[0], lvl)


# "device_id=Android_Redmi5Plus_com.dt011usera.ghjb_41DCE986BE35441ED40A4D547134D932&sign=6913926bce02da7f85b184aea7de79d5&invite_code=&force_new=2&registration_id=&appsflyer_id=1643814409838-7176889219393781526",
#     "device_id=Android_Redmi5Plus_com.dt011usera.ghjb_607129F3D4A1FA5FCB4C1C8D9F2AC3BE&sign=43183e440c5d172a2284f0a425a29c6f&invite_code=&force_new=2&registration_id=&appsflyer_id=1643369576010-5859483671572764918",
