from datetime import datetime
import pytz,time,httpx,json
from tinydb import *
import time,random
import os,sys
from tinydb import *

db = TinyDB("database.json")
sett = db.table('setting')
q = Query()

# import logging
# logging.basicConfig(filename="client.log", level=logging.DEBUG)
from colorama import Fore, Style, init
init()

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

dat={}
print()
 
host="https://wjxwd01mwyo.dt01showxx02.com"

with open(f"user_token.json", 'r') as json_file:
    xtokens=json.load(json_file)["results"]


while True:
    try:
        idek=int(sett.search(q.profile == 'tkn')[0]["val"])
        if idek !=0:
            print(idek)
            token=xtokens[idek]
            break
        else:
            sys.stdout.write(f"{c('red','isi token yang mana yg mau dipake di profile',0)}  \r")
            sys.stdout.flush()
            time.sleep(1)
    except:
        sys.stdout.write(f"{c('red','isi token yang mana yg mau dipake di profile',0)}  \r")
        sys.stdout.flush()
        time.sleep(1)

tz = pytz.timezone("Asia/Jakarta")
now = datetime.now(tz)
idtoken=str(now.strftime("%Y%M%S"))
awaldata={
  "results": {"bet":[]}
  }
with open(f"betting{idtoken}.json", 'w') as json_file:
    json.dump(awaldata, json_file, indent=2,  separators=(',',': '))
    
persi = sys.argv[1]

def getnum(x):
    uri = host+"/App/Game_Game/GetTypeInfo"
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
    req = httpx.get(uri, params=query, headers=headers)
    ress = json.loads(req.text)
    try:
        print(ress)
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
        "live_room_id": idroom,
        "game_type": "toubao_1",
        "game_sub": "zonghe;",
        "game_number": dat["gamenumber"],
        "detail": rType[type] + ":" + num + ";",
        "multiple": "1",
    }

    try:
        req = httpx.post(uri, data=json.dumps(param), headers=headers)
        ress = json.loads(req.text)
        print(ress)
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
        "live_room_id": idroom,
        "game_type": "baijiale_1",
        "game_sub": "zhuangxian",
        "game_number": dat["gamenumber"],
        "detail": rType[type] + ":" + num,
        "multiple": "1",
    }
    try:
        req = httpx.post(uri, data=json.dumps(param), headers=headers)
        ress = json.loads(req.text)
        print(ress)
    except Exception as e:
        print(f"Failed : {e}")

def getinfo(x):
    uriweb = "https://wjxwd01mwyo.dt01showxx02.com/App/User_User/Info"
    headers = {
        "user-agent": f"HS-Android Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.17{random.randint(1000,9999)}.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.{random.randint(1000,9999)}.82 Mobile Safari/537.36",
        "bundleidentifier": "user",
        "x-token": x,
        "accept-encoding": "identity",
        "host": "wjxwd01mwyo.dt01showxx02.com",
        "connection": "keep-alive",
    }
    f = httpx.get(uriweb, headers=headers)
    ress = json.loads(f.text)
    try:
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



mgame="""
1. Sicbo
2. Baccarat
"""
inpgame=0
ngebet="y"#input("autobet [y/n]: ")
if ngebet=="y":
    ngebet=True
    inpgame=1#int(input(f"{mgame}game nomor : "))
else:
    ngebet=False

audit=0
while True:
    try:
        os.system('cls')
        db = TinyDB("database.json")
        sett = db.table('setting')
        dbrec = TinyDB("rec.json")
        dbselisih = dbrec.table('data')

        tabel=chr(126)+chr(126)+chr(32)+chr(65)+chr(84)+chr(65)+chr(82)+chr(79)+chr(32)+chr(126)+chr(126)
        q = Query()
        pola=sett.search(q.profile == 'pola')[0]["val"]
        if pola=="terbesar":
            disppol=c("green","↑↑↑↑↑↑↑↑",0)
            polll=1
        else:
            polll=0
            disppol=c("red","↓↓↓↓↓↓↓↓",0)
        print(f'\t{c("cyan",tabel,0)}')
        
        idek=int(sett.search(q.profile == 'tkn')[0]["val"])
        token=xtokens[idek]
        print(getinfo(token))
        time.sleep(20)
        idroom=sett.search(q.profile == 'roomid')[0]["val"]
        maxbet=int(sett.search(q.profile == 'maxbet')[0]["val"])
        dbet=int(sett.search(q.profile == 'detik')[0]["val"])
        persenan=float(sett.search(q.profile == 'persenan')[0]["val"])
        batasany=int(sett.search(q.profile == 'batas any')[0]["val"])
        tanda={
            "getnum":dbet+10,
            "betting":dbet,
        }

        print(c("green",f"{disppol}[ Audit : {audit} ]{disppol}",0))
        db = TinyDB("data.json")
        xs = db.all()
        xnum=10
        ress={"Big":0,"Small":0,"Odd":0,"Even":0,"Any":0,"Banker":0,"Player":0}
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
                    if xx<maxbet:
                        bett=xx
                    else:
                        bett=maxbet
                    return bett
                if sisahw==tanda["getnum"]:
                    dat["gamenumber"]=getnum(token)
                    time.sleep(1)
                if sisahw==tanda["betting"]:
                    print()
                    # print(ress)
                    bs,oe=["",0],["",0]
                    if int(ress["Small"])>int(ress["Big"]):
                        if polll==0:
                            bs[0]="big"
                        else:
                            bs[0]="small"
                        selisihbs = int(ress["Small"])-int(ress["Big"])
                        bettbs=round(selisihbs*persenan)
                    else:
                        if polll==0:
                            bs[0]="small"
                        else:
                            bs[0]="big"
                        selisihbs = int(ress["Big"])-int(ress["Small"])
                        bettbs=round(selisihbs*persenan)
                    bs[1]=betbrp(bettbs)

                    if int(ress["Odd"])>int(ress["Even"]):
                        if polll==0:
                            oe[0]="even"
                        else:
                            oe[0]="odd"
                        selisihoe = int(ress["Odd"])-int(ress["Even"])
                        bettoe=round(selisihoe*persenan)
                    else:
                        if polll==0:
                            oe[0]="odd"
                        else:
                            oe[0]="even"
                        selisihoe = int(ress["Even"])-int(ress["Odd"])
                        bettoe=round(selisihoe*persenan)
                    oe[1]=betbrp(bettoe)
                    
                    dbselisih.insert_multiple([{
                        'gamenum': dat["gamenumber"],
                        'big': int(ress["Big"]),
                        'small': int(ress["Small"]),
                        'odd': int(ress["Odd"]),
                        'even': int(ress["Even"]),
                        'any': int(ress["Any"]),
                        'selisihbs':selisihbs,
                        'selisihoe':selisihoe,
                        'pola':polll,
                        }])

                    listObj={
                        "results":{"bet":[]}
                    }

                    if bs[1]!=0:
                        print(f"Selisih {selisihbs}[{bettbs}] Bet {bs[0]} {str(bs[1])} coin")
                        listObj["results"]["bet"].append(f"{bs[0]}{bs[1]}")
                        bet(token,bs[0],str(bs[1]))
                        audit+=int(bs[1])
                    if oe[1]!=0:
                        print(f"Selisih {selisihoe}[{bettoe}] Bet {oe[0]} {str(oe[1])} coin")
                        listObj["results"]["bet"].append(f"{oe[0]}{oe[1]}")
                        bet(token,oe[0],str(oe[1]))
                        audit+=int(oe[1])
                    if int(ress["Any"])<batasany:
                        print(c("red","   ANY..!",0))
                        bet(token,"any triple","1")
                        audit+=1

                    with open(f"betting{idtoken}.json", 'w') as json_file:
                        json.dump(listObj, json_file, indent=2,  separators=(',',': '))
                    # input("Press Enter to next")
                    print()
                    for jedaa in range(10):
                        sys.stdout.write(f"\t{jedaa}   \r")
                        sys.stdout.flush()
                        time.sleep(1)
                
                with open(f"betting{idtoken}.json", 'r') as json_file:
                    xbet=json.load(json_file)
                print(c("green","\tLast Bet",0))
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
                    if xx<maxbet:
                        bett=xx
                    else:
                        bett=maxbet
                    return bett
                if sisahw==tanda["getnum"]:
                    dat["gamenumber"]=getnum(token)
                    time.sleep(1)
                if sisahw==tanda["betting"]:
                    print()

                    oe=["",0]

                    if int(ress["Banker"])>int(ress["Player"]):
                        if polll==0:
                            oe[0]="player"
                        else:
                            oe[0]="banker"
                        selisihoe = int(ress["Banker"])-int(ress["Player"])
                        bettoe=round(selisihoe*persenan)
                    else:
                        if polll==0:
                            oe[0]="banker"
                        else:
                            oe[0]="player"
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

                    with open(f"betting{idtoken}.json", 'w') as json_file:
                        json.dump(listObj, json_file, indent=2,  separators=(',',': '))
                    # input("Press Enter to next")
                
                with open(f"betting{idtoken}.json", 'r') as json_file:
                    xbet=json.load(json_file)
                print(c("green","\tLast Bet",0))
                if len(xbet["results"]["bet"])!=0:
                    for ppop in xbet["results"]["bet"]:
                        print(ppop)
            except Exception as e:
                print(f"error : {e}")
                time.sleep(1)
        print(c("green","__________________________",0))
        print(f"token    : {idek}")
        print(f"persenan : {persenan}")
        print(f"maxbet   : {maxbet}")
        print(f"idroom   : {idroom}")
    except Exception as e:
        print(f"Error : {e}")
        ditts={"_default": {}}
        with open("data.json", "w") as outfile:
            json.dump(ditts, outfile)
        


    time.sleep(0.3)