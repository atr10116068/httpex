import ambil
import requests
import seting
import json,random
import time
import getlive
import sys
persi = seting.versi()
xxx, yyy = 0, 0


print("token[x:y]")
try:
    xxx, yyy = int(input("x : ")), int(input("y : "))
except:
    xxx, yyy = 0, 99
    print("all token added")

dat = {"roomid": "0","audit":0}

if input("enter to skip audit target") == "":
    pass
else:
    dat["audit"] = int(input("Audit : "))


def getnum(x):
    uri = "https://wjxwd01mwyo.dt01showxx02.com/App/Game_Game/GetTypeInfo"
    headers = {
        "user-agent": f"Mozilla/5.0 (iPhone11,2; U; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/602.{random.randint(0,255)}.{random.randint(0,255)} (KHTML, like Gecko) Version/9.0 Mobile/{random.randint(11,99)}E{random.randint(111,999)} Safari/602.1",
        "bundleidentifier": "user",
        "x-token": x,
        "accept-encoding": "identity",
        "x-version": persi,
        "host": "wjxwd01mwyo.dt01showxx02.com",
        "connection": "keep-alive",
    }
    query = {"game_type": "toubao_1"}
    req = requests.get(uri, params=query, headers=headers)
    ress = json.loads(req.text)
    try:
        return ress["result"]["current_round"]["number"]
    except:
        print("return error")


# tripel
# live_room_id=160807&game_type=toubao_1&game_sub=zonghe&game_number=202110260818&detail=zonghe_weitou%3A1%3B&multiple=1


def bet(x, type, num,proxs):
    rType = {
        "big": "zonghe_da",
        "small": "zonghe_xiao",
        "odd": "zonghe_dan",
        "even": "zonghe_shuang",
        "any triple": "zonghe_weitou",
    }
    uri = "https://wjxwd01mwyo.dt01showxx02.com/App/Game_Order/Create"
    headers = {
        "User-Agent": f"Mozilla/5.0 (iPhone11,2; U; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/602.{random.randint(0,255)}.{random.randint(0,255)} (KHTML, like Gecko) Version/9.0 Mobile/{random.randint(11,99)}E{random.randint(111,999)} Safari/602.1",
        "BundleIdentifier": "user",
        "X-Token": x,
        "Accept-Encoding": "identity",
        "X-Version": persi,
        "Content-Type": "application/x-www-form-urlencoded",
        "Content-Length": "25",
        "Host": "wjxwd01mwyo.dt01showxx02.com",
        "Connection": "Keep-Alive",
    }
    prox={"https":proxs}
    param = {
        "live_room_id": dat["roomid"],
        "game_type": "toubao_1",
        "game_sub": "zonghe",
        "game_number": getnum(x),
        "detail": rType[type] + ":" + num + ";",
        "multiple": "1",
    }

    req = requests.post(uri, data=json.dumps(param), headers=headers,proxies=prox)
    try:
        ress = json.loads(req.text)
        print(ress)
    except:
        print(f"Failed : {req.text}")


menu = """\t\t[ MENU ]
1.big  2.small  3.odd  4.even 5.any
token-jumlah-bet"""
hehe = ["big", "small", "odd", "even", "any triple"]

token = ambil.token()[xxx:yyy]


dat["room"] = []

# for pp in getlive.roomsexy():
#     dat["room"].append(pp)

for ppp in getlive.roomall():
    dat["room"].append(ppp)

# for p in getlive.roomgame():
#     dat["room"].append(p)
room = dat["room"]

x = 1
for i in room:
    print("{}. {}".format(str(x), i["nickname"]))
    x += 1
inp = input("room nomor : ")
dat["roomid"] = room[int(inp) - 1]["live_id"]
print("\nTarget Room : " + room[int(inp) - 1]["nickname"])

proxx=input("proxy : ")
while True:
    print(menu)
    print(f'Audit : {dat["audit"]}')
    predic = input("prediksi : ")
    if "all" not in predic:
        try:
            idxtoken = int(predic.split("-")[0]) - 1
            num = predic.split("-")[1]
            type = int(predic.split("-")[2])-1
            dat["audit"] -= int(num)
            tkn = token[idxtoken]
            bet(tkn, hehe[type], num,proxx)
        except:
            pass
    else:
        print("ALL IN...")
        type = int(predic.split("-")[2])-1
        num = predic.split("-")[1]
        for tkn in token:
            bet(tkn, hehe[type], num,proxx)
        pass
