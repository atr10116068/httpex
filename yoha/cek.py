import ambil
import getapi
import time,sys
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
8. follow
9. cek duplikat uid
10. cek user yoha
"""
while True:
    x = input(f"{menus}-> ")
    if x == "1":#cek akun
        tkn1, tkn2,  tknall, tkn = 0, 0, 0, 0
        ftkn = input("[no] or [no-no] or enter(all): ")
        jeda=int(input("jeda : "))
        if ftkn == "":
            tknall = token
        else:
            if "-" in ftkn:
                tkn1, tkn2 = int(ftkn.split("-")[0]), int(ftkn.split("-")[1])
            else:
                tkn = int(ftkn)
        if tkn1 != 0 and tkn2 != 0 or tknall != 0:
            x = 0
            if tknall != 0:
                itrtkn = token
            else:
                itrtkn = token[tkn1-1:tkn2-1]
                x = tkn1-1
            jumkoin = 0
            for tkn in itrtkn:
                try:
                    acc = getapi.profile(tkn)
                    x += 1
                except:
                    break

                if acc != 0:
                    acc = acc["data"]
                    print(
                        f'[{x}/{len(itrtkn)}].  {c("magenta",acc["id"],0)}\t{acc["user_nicename"]} {c("cyan",acc["diamonds"],0)} {c("yellow",acc["coin"],0)} ')
                    jumkoin += int(acc["diamonds"])
                    time.sleep(jeda)
                
            print(f"jumlah Diamond +- {c('cyan',jumkoin,0)}")
        else:
            tkn1 = token[tkn-1]
            print(tkn1)
            acc = getapi.profile(tkn1)
            acc = acc["data"]
            print(
                f'{tkn}.\t{c("magenta",acc["id"],0)}\t{acc["user_nicename"]} {c("cyan",acc["diamonds"],0)} {c("yellow",acc["coin"],0)} ')

    if x == "2":#get token
        tkn = token[int(input("token no : "))-1]
        acc = getapi.profile(tkn)
        print(acc["data"]["token"])
    if x == "3":#chat
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
    if x == "4":#gift
        rdmtkn=random.choice(token)
        getidroom = getapi.getroom(rdmtkn)
        x = 1
        for idr in getidroom:
            print(f"{x}. {idr['user_nicename']}")
            x += 1
        
        idroom = getidroom[int(input("room no : "))-1]
        namahost, streamid, uid = idroom["user_nicename"], idroom["room_id"], idroom["uid"]

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
            if tknall != 0:
                itrtkn = token
            else:
                itrtkn = token[tkn1-1:tkn2-1]
            tokengift = itrtkn
            reqdata = getapi.getgift(rdmtkn)
            
            listgift = reqdata["data"]["gift_list"]
            newlistgift = sorted(listgift, key=lambda d: d['need_coin'])
            for pgift in newlistgift:
                giftid = pgift['id']
                giftname = pgift['gift_name']
                amount = pgift['need_coin']
                print(f"   [{giftid}] [{amount}]   \t{giftname}")
                
            inpp = input("Gift id : ")
            jumgip=input("jumlah : ")
            for tokengiftr in tokengift:
                print(f"Host : {namahost}")
                print(c("green", f"Diamond : {reqdata['data']['coin']}", 0))
                if inpp == "q":
                    break
                getapi.gift(tokengiftr, streamid, inpp, uid, jumgip)
    if x == "5":#getuid
        uaidi = ambil.uid()
        tkn1, tkn2,  tknall, tkn = 0, 0, 0, 0
        print(f"Jumlah UID : {len(uaidi)}")
        if input("Q to Quit : ") != "q":
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
    if x == "6":#enter room
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
    if x == "7":#jastem
        targetgip=int(input("Target Gift : "))
        jeda=float(input("jeda : "))
        tkn1, tkn2,  tknall, tkn = 0, 0, 0, 0
        ftkn = input("[no-no] or enter(all): ")
        if ftkn == "":
            tknall = token
        else:
            if "-" in ftkn:
                tkn1, tkn2 = int(ftkn.split("-")[0]), int(ftkn.split("-")[1])
            else:
                tkn = int(ftkn)
        if tkn1 != 0 and tkn2 != 0 or tknall != 0:
            x = 0
            if tknall != 0:
                itrtkn = token
            else:
                itrtkn = token[tkn1-1:tkn2-1]
                x = tkn1


            jumgift = 0
            getidroom = getapi.getroom(random.choice(token))
            xr = 1
            for idr in getidroom:
                print(f"{xr}. {idr['user_nicename']}")
                xr += 1
            idxrum=int(input("room no : "))
            idroom = getidroom[idxrum-1]["stream"]
            aidir = getidroom[idxrum-1]["uid"]

            reqdata = getapi.getgift(itrtkn[0])
            listgift = reqdata["data"]["gift_list"]
            newlistgift = sorted(listgift, key=lambda d: d['need_coin'], reverse=True)
            setop=False
            for tkn in itrtkn:
                try:
                    acc = getapi.profile(tkn)
                    x += 1
                except:
                    break
                if acc != 0:
                    acc = acc["data"]
                    #________________________________
                    rstream=idroom
                    nama=acc["user_nicename"]
                    aidi=acc["id"]
                    dm=acc["diamonds"]
                    #________________________________
                    #gip = token, stream, idgift, liveuid, num
                    for tgip in newlistgift:
                        gname= tgip["gift_name"]
                        gdm=tgip["need_coin"]
                        gid=tgip["id"]
                        if jumgift>=targetgip:
                            setop=True
                            break
                        if int(dm)>500 and int(dm)>gdm:
                            sisah=targetgip-(jumgift+gdm)
                            # print(f"kurang : {sisah}")
                            if sisah>-600:
                                try:
                                    getapi.gift(tkn,rstream,gid,aidir,"1")
                                    jumgift += int(gdm)
                                    print(f'   {x}. {c("magenta",nama,0)} [{c("cyan",dm,0)}]\tgift {c("magenta",gname,0)} [{c("red",gdm,0)}] = {c("yellow",jumgift,0)}')
                                except Exception as e:
                                    print(f"Gagal tidak masuk hitungan : {e}")
                                break
                            else:
                                print(f'   {x}. {c("magenta",nama,0)} [{c("cyan",dm,0)}]\tsaldo kurang = {c("yellow",jumgift,0)}')

                    if setop==True:
                        break
                    time.sleep(jeda)
                
            print(f"\tjumlah Gift:{c('yellow',jumgift,0)}")
    if x == "8":#follow
        mode = input("mode [no-no] : ")
        aidi = input("ID target : ")
        if "-" in mode:
            ittkn = mode
            tkn1 = int(ittkn.split("-")[0])
            tkn2 = int(ittkn.split("-")[1])
            tokenlup = token[tkn1-1:tkn2-1]
            xi=1
            for tkn in tokenlup:
                plow=getapi.follow(tkn, aidi)
                print(f'{xi}   : {c("green",plow,0)}')
                xi+=1
                time.sleep(0.6)
    if x == "9":#cek uid
        uaidi = ambil.uid()
        bck=[]
        for t in uaidi:
            if t["no"] not in bck:
                bck.append(t["no"])
            else:
                print(f'{t["no"]} ada yg sama')
    if x=="10":
        xxx=getapi.profileuser(token[0],input("id user : "))["data"]
        print(json.dumps(xxx,indent=2))
        getapi.updateuser(input("Token : "))
