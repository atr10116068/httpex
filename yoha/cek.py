import ambil
import getapi
import time
import random
import json
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


token = ambil.token()

menus = """
1. cek akun
2. get token
3. chat
4. gift
5. get UID
6. enter room
7. jastem
"""
while True:
    x = input(f"{menus}-> ")
    if x == "1":
        tkn1, tkn2,  tknall, tkn = 0, 0, 0, 0
        ftkn = input("[no] or [no-no] or enter(all): ")
        if ftkn == "":
            tknall = token
        else:
            if "-" in ftkn:
                tkn1, tkn2 = int(ftkn.split("-")[0]), int(ftkn.split("-")[1])
            else:
                tkn = int(ftkn)
        if tkn1 != 0 and tkn2 != 0 or tknall != 0:
            x = 1
            if tknall != 0:
                itrtkn = token
            else:
                itrtkn = token[tkn1-1:tkn2-1]
                x = tkn1
            jumkoin = 0
            for tkn in itrtkn:
                try:
                    acc = getapi.profile(tkn)
                except:
                    time.sleep(20)
                    acc = getapi.profile(tkn)#percobaan ke 2

                if acc != 0:
                    acc = acc["data"]
                    print(
                        f'{x}.\t{c("magenta",acc["id"],0)}\t{acc["user_nicename"]} {c("cyan",acc["diamonds"],0)} {c("yellow",acc["coin"],0)} ')
                    jumkoin += int(acc["diamonds"])
                    time.sleep(0.5)
                
                x += 1
            print(f"jumlah Diamond +- {c('cyan',jumkoin,0)}")
        else:
            tkn1 = token[tkn-1]
            print(tkn1)
            acc = getapi.profile(tkn1)
            acc = acc["data"]
            print(
                f'{tkn}.\t{c("magenta",acc["id"],0)}\t{acc["user_nicename"]} {c("cyan",acc["diamonds"],0)} {c("yellow",acc["coin"],0)} ')

    if x == "2":
        tkn = token[int(input("token no : "))-1]
        acc = getapi.profile(tkn)
        print(acc["data"]["token"])
    if x == "3":
        mode = input("mode [no] [loop no-no] : ")
        getidroom = getapi.getroom(random.choice(token))
        x = 1
        for idr in getidroom:
            print(f"{x}. {idr['user_nicename']}")
            x += 1
        idroom = getidroom[int(input("room no : "))-1]["stream"]
        if "loop" in mode:
            ittkn = mode.replace("loop ", "")
            tkn1 = int(ittkn.split("-")[0])
            tkn2 = int(ittkn.split("-")[1])
            while True:
                quitt = False
                tokenlup = token[tkn1-1:tkn2-1]
                for tkn in tokenlup:
                    texx = input("text :")
                    if texx == "q":
                        quitt = True
                        break
                    getapi.send(tkn, idroom, texx)
                if quitt == True:
                    break
        else:
            while True:
                tkn = token[int(mode)-1]
                texx = input("text :")
                if texx == "q":
                    break
                getapi.send(tkn, idroom, texx)
    if x == "4":
        getidroom = getapi.getroom(random.choice(token))
        x = 1
        for idr in getidroom:
            print(f"{x}. {idr['user_nicename']}")
            x += 1
        idroom = getidroom[int(input("room no : "))-1]
        namahost, streamid, uid = idroom["user_nicename"], idroom["room_id"], idroom["uid"]

        tokengift = token[int(input("token no : "))-1]
        reqdata = getapi.getgift(tokengift)
        
        print(json.dumps(reqdata, indent=2))
        listgift = reqdata["data"]["gift_list"]
        newlistgift = sorted(listgift, key=lambda d: d['need_coin'])
        for pgift in newlistgift:
            giftid = pgift['id']
            giftname = pgift['gift_name']
            amount = pgift['need_coin']
            print(f"   [{giftid}] [{amount}]   \t{giftname}")
        while True:
            print(f"Host : {namahost}")
            print(c("green", f"Diamond : {reqdata['data']['coin']}", 0))
            inpp = input("Gift id : ")
            if inpp == "q":
                break
            getapi.gift(tokengift, streamid, inpp, uid, input("jumlah : "))
    if x == "5":
        uaidi = ambil.uid()
        tkn1, tkn2,  tknall, tkn = 0, 0, 0, 0
        ftkn = input("[no] or [no-no] or enter(all): ")
        if ftkn == "":
            tknall = uaidi
        else:
            if "-" in ftkn:
                tkn1, tkn2 = int(ftkn.split("-")[0]), int(ftkn.split("-")[1])
            else:
                tkn = int(ftkn)
        if tkn1 != 0 and tkn2 != 0 or tknall != 0:
            x = 1
            if tknall != 0:
                itrtkn = uaidi
            else:
                itrtkn = uaidi[tkn1-1:tkn2-1]
                x = tkn1
            for tkn in itrtkn:
                print(
                    f'{x}.\t{c("cyan",tkn["no"],0)}\t[{c("magenta",tkn["pass"],0)}]')
                time.sleep(0.1)
                x += 1
        else:
            tkn = uaidi[tkn-1]
            print(
                f'{x}.\t{c("cyan",tkn["no"],0)}\t[{c("magenta",tkn["pass"],0)}]')
    if x == "6":
        mode = input("mode [no-no] : ")
        getidroom = getapi.getroom(random.choice(token))
        x = 1
        for idr in getidroom:
            print(f"{x}. {idr['user_nicename']}")
            x += 1
        idxrum=int(input("room no : "))
        idroom = getidroom[idxrum-1]["stream"]
        aidi = getidroom[idxrum-1]["uid"]
        if "-" in mode:
            ittkn = mode
            tkn1 = int(ittkn.split("-")[0])
            tkn2 = int(ittkn.split("-")[1])
            tokenlup = token[tkn1-1:tkn2-1]
            while True:
                texx = input("e/q enter/quit :")
                if texx == "e":
                    xi=1
                    for tkn in tokenlup:
                        getapi.enter(tkn, aidi)
                        print(xi)
                        xi+=1
                        time.sleep(0.5)
                if texx == "q":
                    xi=1
                    for tkn in tokenlup:
                        getapi.kuit(tkn, aidi)
                        print(xi)
                        xi+=1
                        time.sleep(0.5)
    if x == "7":
        tkn1, tkn2,  tknall, tkn = 0, 0, 0, 0
        ftkn = input("[no] or [no-no] or enter(all): ")
        if ftkn == "":
            tknall = token
        else:
            if "-" in ftkn:
                tkn1, tkn2 = int(ftkn.split("-")[0]), int(ftkn.split("-")[1])
            else:
                tkn = int(ftkn)
        if tkn1 != 0 and tkn2 != 0 or tknall != 0:
            x = 1
            if tknall != 0:
                itrtkn = token
            else:
                itrtkn = token[tkn1-1:tkn2-1]
                x = tkn1
            
            jumkoin = 0
            reqdata = getapi.getgift(itrtkn[0])
            listgift = reqdata["data"]["gift_list"]
            newlistgift = sorted(listgift, key=lambda d: d['need_coin'])
            for tkn in itrtkn:
                try:
                    acc = getapi.profile(tkn)
                except:
                    time.sleep(20)
                    acc = getapi.profile(tkn)#percobaan ke 2

                if acc != 0:
                    acc = acc["data"]
                    aidi=acc["id"]
                    # DISINI CARI GIFT YG TERTINGGI LALU GIFT
                    print(
                        f'{x}.\t{acc["user_nicename"]} {c("cyan",acc["diamonds"],0)}')
                    jumkoin += 1
                    time.sleep(0.5)
                
                x += 1
            print(f"jumlah Diamond +- {c('cyan',jumkoin,0)}")

