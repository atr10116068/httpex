import requests
import json,random
import time
import getlive
import seting
import ambil
import sys

xxx, yyy = 1, 33
persi = seting.versi()

try:
    xxx, yyy = int(input("token awal : ")), int(input("token ahir : "))
except:
    xxx, yyy = 0, 133
    print("all token added")

dat = {"roomid": "0"}


def getnum(x):
    uri = "https://wjxwd01mwyo.dt01showxx02.com/App/Game_Game/GetTypeInfo"
    headers = {
        "user-agent": f"HS-Android Mozilla/5.0 (Linux; Android 8.1.0; SM-J730F Build/{random.randint(1000,9999)}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.{random.randint(1000,9999)}.129 Mobile Safari/537.36",
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


# tripel
# live_room_id=160807&game_type=toubao_1&game_sub=zonghe&game_number=202110260818&detail=zonghe_weitou%3A1%3B&multiple=1


def bet(x, type, num,proxs):
    rType = {
        "player": "zhuangxian_xian",
        "banker": "zhuangxian_zhuang",
        "tie": "zhuangxian_he"
    }
    uri = "https://wjxwd01mwyo.dt01showxx02.com/App/Game_Order/Create"
    headers = {
        "User-Agent": f"HS-Android Mozilla/5.0 (Linux; Android 8.1.0; SM-J730F Build/{random.randint(1000,9999)}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.{random.randint(1000,9999)}.129 Mobile Safari/537.36",
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
        "live_room_id": dat["roomid"],
        "game_type": "baijiale_1",
        "game_sub": "zhuangxian",
        "game_number": getnum(x),
        "detail": rType[type] + ":" + num,
        "multiple": "1",
    }
    prox={"https":proxs}
    try:
        req = requests.post(uri, data=json.dumps(param), headers=headers,proxies=prox)
        ress = json.loads(req.text)
        print(ress)
    except Exception as e:
        print(f"Failed : {e}")


menu = """\t\t[ MENU ]
1.player 2.banker 3.tie
bet-jumlah-token"""
hehe = ["player", "banker", "tie"]


# token = ambil.token()[xxx:yyy]
token = ambil.token()


room = getlive.roomall()
room.append({"nickname": "lobby", "live_id": ""})
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
    predic = input("prediksi : ")
    if "all" not in predic:
        try:
            type = int(predic.split("-")[0]) - 1
            num = predic.split("-")[1]
            tkn = token[int(predic.split("-")[2])-1]
            bet(tkn, hehe[type], num,proxx)
        except:
            pass
    else:
        print("ALL IN...")
        type = int(predic.split("-")[0]) - 1
        num = predic.split("-")[1]
        for tkn in token:
            bet(tkn, hehe[type], num,proxx)
        pass
