from datetime import datetime
import pytz,time,requests,seting,json,ambil
from tinydb import *
import time,random
import os

# import logging
# logging.basicConfig(filename="client.log", level=logging.DEBUG)
from colorama import Fore, Style, init
init()
dat={}
print()
dbet=input("detik betting : ")
if dbet!="":
    dbet=int(dbet)
else:
    dbet=10
tanda={
    "getnum":dbet+15,
    "betting":dbet,
}

idroom=""
ty=input("id room : ")
if ty!="":
    idroom=ty

persenan=0
ty=input("persenan [0.6=60%] : ")
if ty!="":
    persenan=float(ty)
host="https://wjxwd01mwyo.dt01showxx02.com"
tokk = ambil.token()
if input("Enter to set token from db")!="":
    with open("user_token.json") as json_file:
        token = json.load(json_file)["results"][0]
else:
    token=tokk[int(input("token ke : "))-1]
print(token)
persi = seting.versi()
tz = pytz.timezone("Asia/Jakarta")
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
    uri = host+"/App/Game_Game/GetTypeInfo"
    headers = {
        "user-agent": f"HS-Android Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.17{random.randint(1000,9999)}.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.{random.randint(1000,9999)}.82 Mobile Safari/537.36",
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


def bet(x, type, num):
    rType = {
        "big": "zonghe_da",
        "small": "zonghe_xiao",
        "odd": "zonghe_dan",
        "even": "zonghe_shuang",
        "any triple": "zonghe_weitou",
    }
    uri = "https://wjxwd01mwyo.dt01showxx02.com/App/Game_Order/Create"
    headers = {
        "User-Agent": f"HS-Android Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.17{random.randint(1000,9999)}.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.{random.randint(1000,9999)}.82 Mobile Safari/537.36",
        "BundleIdentifier": "user",
        "X-Token": x,
        "Accept-Encoding": "identity",
        "X-Version": persi,
        "Content-Type": "application/x-www-form-urlencoded",
        "Content-Length": "25",
        "Host": "wjxwd01mwyo.dt01showxx02.com",
        "Connection": "Keep-Alive",
    }
    param = {
        "live_room_id": idroom,
        "game_type": "toubao_1",
        "game_sub": "zonghe;",
        "game_number": dat["gamenumber"],
        "detail": rType[type] + ":" + num + ";",
        "multiple": "1",
    }

    try:
        req = requests.post(uri, data=json.dumps(param), headers=headers)
        ress = json.loads(req.text)
        print(ress["result"]["balance"])
    except:
        print("Failed...")

def betbac(x, type, num):
    rType = {
        "player": "zhuangxian_xian",
        "banker": "zhuangxian_zhuang",
        "tie": "zhuangxian_he"
    }
    uri = "https://wjxwd01mwyo.dt01showxx02.com/App/Game_Order/Create"
    headers = {
        "User-Agent": f"HS-Android Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.17{random.randint(1000,9999)}.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.{random.randint(1000,9999)}.82 Mobile Safari/537.36",
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
        "live_room_id": idroom,
        "game_type": "baijiale_1",
        "game_sub": "zhuangxian",
        "game_number": dat["gamenumber"],
        "detail": rType[type] + ":" + num,
        "multiple": "1",
    }
    try:
        req = requests.post(uri, data=json.dumps(param), headers=headers)
        ress = json.loads(req.text)
        print(ress)
    except Exception as e:
        print(f"Failed : {e}")

mgame="""
1. Sicbo
2. Baccarat
"""
inpgame=0
ngebet=input("autobet [y/n]: ")
if ngebet=="y":
    ngebet=True
    inpgame=int(input(f"{mgame}game nomor : "))
else:
    ngebet=False
    
while True:
    try:
        os.system('cls')
        db = TinyDB("data.json")
        xs = db.all()
        xnum=10
        ress={"Big":0,"Small":0,"Odd":0,"Even":0,"Banker":0,"Player":0}
        for x in xs:
            print(f'__________[ {x["game"]} ]_________')
            for xxx in x["data"]:
                clr=""
                clrnum="green"
                num=x["data"][xxx]
                if xnum<num:
                    clrnum="red"
                    xnum=num
                else:
                    clrnum="grey"

                if "Big" in xxx:
                    clr="red"
                if "Banker" in xxx:
                    clr="red"
                if "Small" in xxx:
                    clr="blue"
                if "Player" in xxx:
                    clr="blue"
                if "Odd" in xxx:
                    clr="cyan"
                if "Even" in xxx:
                    clr="magenta"
                if "Any" in xxx:
                    clr="purple"
                ress[xxx]=num
                print(f'{c(clr,xxx,0)}:{c(clrnum,num,0)}')
        
        if inpgame==1:
            try:
                now = datetime.now(tz)
                dtk=now.strftime("%S")
                sisahw=60-int(dtk)
                xx=now.strftime(f"Sisah Waktu {sisahw}")
                print(c("magenta",'_________________________',0))
                print(xx)
                def betbrp(xx):
                    if xx>10:
                        bett=5
                    elif xx>5:
                        bett=5
                    else:
                        bett=xx
                    return bett
                if sisahw==tanda["getnum"]:
                    dat["gamenumber"]=getnum(token)
                if sisahw==tanda["betting"]:
                    print()
                    # print(ress)
                    bs,oe=["",0],["",0]
                    if int(ress["Small"])>int(ress["Big"]):
                        bs[0]="big"
                        selisihbs = int(ress["Small"])-int(ress["Big"])
                        bettbs=round(selisihbs*persenan)
                    else:
                        bs[0]="small"
                        selisihbs = int(ress["Big"])-int(ress["Small"])
                        bettbs=round(selisihbs*persenan)
                    bs[1]=betbrp(bettbs)

                    if int(ress["Odd"])>int(ress["Even"]):
                        oe[0]="even"
                        selisihoe = int(ress["Odd"])-int(ress["Even"])
                        bettoe=round(selisihoe*persenan)
                    else:
                        oe[0]="odd"
                        selisihoe = int(ress["Even"])-int(ress["Odd"])
                        bettoe=round(selisihoe*persenan)
                    oe[1]=betbrp(bettoe)
                    
                    listObj={
                        "results":{"bet":[]}
                    }

                    if bs[1]!=0:
                        # print(f"Selisih {selisihbs}[{bettbs}] Bet {bs[0]} {str(bs[1])} coin")
                        listObj["results"]["bet"].append(f"{bs[0]}{bs[1]}")
                        bet(token,bs[0],str(bs[1]))
                    if oe[1]!=0:
                        # print(f"Selisih {selisihoe}[{bettoe}] Bet {oe[0]} {str(oe[1])} coin")
                        listObj["results"]["bet"].append(f"{oe[0]}{oe[1]}")
                        bet(token,oe[0],str(oe[1]))

                    with open("betting.json", 'w') as json_file:
                        json.dump(listObj, json_file, indent=2,  separators=(',',': '))
                    # input("Press Enter to next")
                
                with open("betting.json", 'r') as json_file:
                    xbet=json.load(json_file)
                if len(xbet["results"]["bet"])!=0:
                    for ppop in xbet["results"]["bet"]:
                        print(ppop)
            except Exception as e:
                print(f"error : {e}")
                time.sleep(1)
        elif inpgame==2:
            try:
                now = datetime.now(tz)
                dtk=now.strftime("%S")
                sisahw=60-int(dtk)
                xx=now.strftime(f"Sisah Waktu {sisahw}")
                print(c("magenta",'_________________________',0))
                print(xx)
                def betbrp(xx):
                    if xx>10:
                        bett=5
                    elif xx>5:
                        bett=5
                    else:
                        bett=xx
                    return bett
                if sisahw==tanda["getnum"]:
                    dat["gamenumber"]=getnum(token)
                if sisahw==tanda["betting"]:
                    print()

                    oe=["",0]

                    if int(ress["Banker"])>int(ress["Player"]):
                        oe[0]="player"
                        selisihoe = int(ress["Banker"])-int(ress["Player"])
                        bettoe=round(selisihoe*persenan)
                    else:
                        oe[0]="banker"
                        selisihoe = int(ress["Player"])-int(ress["Banker"])
                        bettoe=round(selisihoe*persenan)
                    oe[1]=betbrp(bettoe)
                    
                    listObj={
                        "results":{"bet":[]}
                    }

                    # print(ress)
                    if oe[1]!=0:
                        print(f"Selisih {selisihoe}[{bettoe}] Bet {oe[0]} {str(oe[1])} coin")
                        listObj["results"]["bet"].append(f"{oe[0]}{oe[1]}")
                        betbac(token,oe[0],str(oe[1]))

                    with open("betting.json", 'w') as json_file:
                        json.dump(listObj, json_file, indent=2,  separators=(',',': '))
                    # input("Press Enter to next")
                
                with open("betting.json", 'r') as json_file:
                    xbet=json.load(json_file)
                if len(xbet["results"]["bet"])!=0:
                    for ppop in xbet["results"]["bet"]:
                        print(ppop)
            except Exception as e:
                print(f"error : {e}")
                time.sleep(1)
    except Exception as e:
        print(f"Error : {e}")
        ditts={"_default": {}}
        with open("data.json", "w") as outfile:
            json.dump(ditts, outfile)


    time.sleep(1)