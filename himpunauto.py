import httpx
import json
import time
import seting
import random
import sys,pytz
from datetime import datetime
import ambil
from colorama import Fore, Style, init
init()


dat = {"roomid": "0", "pake": [], "ganjilgenap": 2}
persi = seting.versi()

def tunggu(x):
    tz = pytz.timezone("Asia/Jakarta")
    print()
    while True:
        now = datetime.now(tz)
        jamm = now.strftime("%H:%M:%S")
        sys.stdout.write(f"  {jamm}/{x}   \r")
        sys.stdout.flush()
        detik = now.strftime("%S")
        if int(detik)==int(x):
            break
        time.sleep(0.5)
    

def c(colr, tex, dim):
    try:
        w = {
            "RED": Fore.RED,
            "GREEN": Fore.GREEN,
            "YELLOW": Fore.YELLOW,
            "BLUE": Fore.BLUE,
            "MAGENTA": Fore.MAGENTA,
            "CYAN": Fore.CYAN,

            "BLACK": Fore.BLACK,
            "WHITE": Fore.WHITE,
            "RESET": Fore.RESET,
        }
        if dim == 1:
            return f"{Style.DIM}{w[colr.upper()]}{tex}{Style.RESET_ALL}"
        else:
            return f"{w[colr.upper()]}{tex}{Style.RESET_ALL}"
    except:
        return tex


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
    query = {"game_type": "baijiale_1"}
    req = httpx.get(uri, params=query, headers=headers)
    ress = json.loads(req.text)
    try:
        return ress["result"]["current_round"]["number"]
    except:
        print("return error")


# tripel
# live_room_id=160807&game_type=toubao_1&game_sub=zonghe&game_number=202110260818&detail=zonghe_weitou%3A1%3B&multiple=1


def bet(x, type, num, gamevers):
    rType = {
        "player": "zhuangxian_xian",
        "banker": "zhuangxian_zhuang",
        "tie": "zhuangxian_he"
    }
    uri = "https://wjxwd01mwyo.dt01showxx02.com/App/Game_Order/Create"
    headers = {
        "User-Agent": f"Mozilla/5.0 (iPhone11,2; U; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/602.{random.randint(0,255)}.{random.randint(0,255)} (KHTML, like Gecko) Version/9.0 Mobile/{random.randint(11,99)}E{random.randint(111,999)} Safari/602.1",
        "BundleIdentifier": "user",
        "X-Token": x,
        "Accept-Encoding": "identity",
        "X-Version": persi,
        "Content-Type": "application/x-www-form-urlencoded",
        "Host": "wjxwd01mwyo.dt01showxx02.com",
        "Connection": "Keep-Alive",
    }
    param = {
        "live_room_id": dat["roomid"],
        "game_type": "baijiale_1",
        "game_sub": "zhuangxian",
        "game_number": gamevers,
        "detail": rType[type] + ":" + num,
        "multiple": "1",
    }

    req = httpx.post(uri, data=json.dumps(param), headers=headers)
    try:
        ress = json.loads(req.text)
        return(ress)
    except:
        print("Failed...")


def getinfo(x):
    uriweb = "https://wjxwd01mwyo.dt01showxx02.com/App/User_User/Info"
    headers = {
        "user-agent": f"Mozilla/5.0 (iPhone11,2; U; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/602.{random.randint(0,255)}.{random.randint(0,255)} (KHTML, like Gecko) Version/9.0 Mobile/{random.randint(11,99)}E{random.randint(111,999)} Safari/602.1",
        "bundleidentifier": "user",
        "x-token": x,
        "accept-encoding": "identity",
        "host": "wjxwd01mwyo.dt01showxx02.com",
        "connection": "keep-alive",
    }
    f = httpx.get(uriweb, headers=headers)
    try:
        ress = json.loads(f.text)
        krm = [
            ress["result"]["nickname"],
            ress["result"]["balance"],
            ress["result"]["vip_name"],
            ress["result"]["id"],
        ]
        return krm
    except:
        krm = [
            "expiret",
            0.0,
            "expiret",
            "expiret",
        ]
        return krm


tokens = []

print("0 termasuk token[x:y]")
try:
    aa, bb = int(input("x : ")), int(input("y : "))
except:
    aa, bb = 0, 150


jedascan=float(input("jeda scan : "))
token = ambil.token()[aa:bb]
print("filtering...")
ikl = 1
for i in token:
    ceking = getinfo(i)
    if float(ceking[1]) >= 1.0:
        tokens.append(i)
    sys.stdout.write(f"\t {ikl} -> {len(tokens)}\r")
    sys.stdout.flush()
    ikl += 1
    time.sleep(jedascan)

print()
# room = getlive.roomall()
# room.append({"nickname": "lobby", "live_id": ""})

# x = 1
# for i in room:
#     print("{}. {}".format(str(x), i["nickname"]))
#     x += 1
# inp = input("room nomor : ")
# dat["roomid"] = room[int(inp) - 1]["live_id"]
# print("\nTarget Room : " + room[int(inp) - 1]["nickname"])
dat["roomid"]=0

def pilter():
    dat["pake"].clear()
    iff = 0
    xkecil=999999

    for t in tokens:
        ceking = getinfo(t)
        ceking.append(t)
        # print(f"{ceking[1]} {ceking[0]}")

        if float(ceking[1]) >= 1.0:
            gngn = "Ganjil"
            gngnkey = "Ganjil"
            # print(
            #     f'coinnya = [{int(str(ceking[1].split(".")[0]))}]  {int(str(ceking[1].split(".")[0]))%2==0}')

            if int(str(ceking[1].split(".")[0])) % 2 == 0:  # genap
                gngn = "Genap"
            if dat["ganjilgenap"] == 1:
                gngnkey = "Genap"

            if gngnkey == "Genap" and gngn == "Genap":
                dat["pake"].append(ceking[4])
                print(f"Add [{ceking[1]}] \t{ceking[0]} {gngn} -> {gngnkey}")
                if int(ceking[1].split(".")[0]) < xkecil:
                    xkecil=int(ceking[1].split(".")[0])
            if gngnkey == "Ganjil" and gngn == "Ganjil":
                dat["pake"].append(ceking[4])
                print(f"Add [{ceking[1]}] \t{ceking[0]} {gngn} -> {gngnkey}")
                if int(ceking[1].split(".")[0]) < xkecil:
                    xkecil=int(ceking[1].split(".")[0])
        else:
            tokens.pop(tokens.index(t))
            # print(f"jumlah token : {len(tokens)}")

        iff += 1
        sys.stdout.write(f"Scanning... {iff} \r")
        sys.stdout.flush()
        time.sleep(jedascan)
    return xkecil


hehe = ["player", "banker"]

while True:
    tunggu(15)
    # input("SCAN")
    if dat["ganjilgenap"] == 2:
        dat["ganjilgenap"] = 1
    else:
        dat["ganjilgenap"] = 2
    xkecil=pilter()
    itrr = len(dat["pake"])
    print(f"<<<<<<<<<<<<<  {itrr} tokens Selected")
    if itrr == 1 or itrr == 0:
        if dat["ganjilgenap"] == 2:
            dat["ganjilgenap"] = 1
        else:
            dat["ganjilgenap"] = 2
        xkecil=pilter()
        itrr = len(dat["pake"])
        print(f"<<<<<<<<<<<<<  {itrr} tokens Selected")
    if itrr % 2 != 0:
        dat["pake"].pop(0)

    itrr = len(dat["pake"])
    print(f">>>>>>>>>>>>> {itrr} akun Betting")
    if itrr==0:exit()

    #cari nilai terkecil
    print(f"terkecil = {xkecil}")
    tunggu(random.randint(46,50))
    # input("BET")
    bett = str(xkecil)
    if itrr != 0:
        gamevers = getnum(dat["pake"][0])

        # print(json.dumps(dat["pake"], indent=2))
        jp, jb = [], []

        gasbet = {}
        for pola in range(itrr):
            if pola % 2 == 0:
                type = 0
            else:
                type = 1
            tkn = dat["pake"][pola]
            # untuk bet all in semuanya
            # bet(tkn, hehe[type], dataakun[itr][1].split('.')[0])
            # print(hehe[type], bett, gamevers)
            if hehe[type] == "banker":
                dataa = {
                    "num": pola,
                    "tipe": hehe[type],
                    "tkn": tkn,
                    "jum": bett,
                    "verr": gamevers,
                    "warna": "red"
                }
                gasbet[pola] = (dataa)
            else:
                dataa = {
                    "num": pola,
                    "tipe": hehe[type],
                    "tkn": tkn,
                    "jum": bett,
                    "verr": gamevers,
                    "warna": "blue"
                }
                gasbet[pola] = (dataa)

        lennya = len(gasbet)-1
        dahpick = []
        while len(gasbet) != 0:
            # print(">>>>>>>>>>  "+str(len(gasbet)))
            while True:
                badak = random.randint(0, lennya)
                if badak not in dahpick:
                    dahpick.append(badak)
                    break

            dbt = gasbet[badak]
            # print()
            bettlol = bet(dbt["tkn"], dbt["tipe"], dbt["jum"], dbt["verr"])
            # bettlol = {'msg': 'ok', 'code': 0, 'result': {'balance': dbt["jum"]}}
            try:
                if dbt["tipe"] == "player":
                    jp.append(
                        int("1"+str(bettlol["result"]["balance"].replace(".", ""))))
                else:
                    jb.append(
                        int("1"+str(bettlol["result"]["balance"].replace(".", ""))))
            except:
                jp.append("000")

            print(c(dbt["warna"], f"{str(badak)} >> {str(bettlol)}", 0))
            if bettlol["code"] == 1:
                if "empty" in bettlol["msg"]:
                    if dat["ganjilgenap"] == 2:
                        dat["ganjilgenap"] = 1
                    else:
                        dat["ganjilgenap"] = 2
                break

            del gasbet[badak]
            time.sleep(0.3)

        try:
            apop = str(min(jb))
            apop = apop[1::]
            apop = (f"{apop[:1]}.{apop[1:5]}")
            bpop = str(min(jp))
            bpop = bpop[1::]
            bpop = (f"{bpop[:1]}.{bpop[1:5]}")

            print(c("blue", f"\tif player : {apop}", 0))
            print(c("red", f"\tif banker : {bpop}", 0))
        except:
            pass
