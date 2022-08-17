from textwrap import indent
import ambil,getapi,random
from colorama import Fore,Style ,init
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

token=ambil.token()

menus="""
1. cek akun
2. get token
3. chat
4. gift
"""
while True:
    x=input(f"{menus}-> ")
    if x=="1":
        jumkoin=0
        x=1
        for tkn in token:
            acc=getapi.profile(tkn)
            if acc != 0:
                acc=acc["data"]
                print(f'{x}.\t{c("magenta",acc["id"],0)}\t{acc["user_nicename"]} {c("cyan",acc["diamonds"],0)} {c("yellow",acc["coin"],0)} ')
                jumkoin+=int(acc["diamonds"])
            x+=1
            
        print(f"jumlah coin +- {c('cyan',jumkoin,0)}")
    if x=="2":
        tkn=token[int(input("token no : "))-1]
        acc=getapi.profile(tkn)
        print(acc["data"]["token"])
    if x=="3":
        mode=input("mode [no] [loop no-no] : ")
        getidroom=getapi.getroom(random.choice(token))
        x=1
        for idr in getidroom:
            print(f"{x}. {idr['user_nicename']}")
            x+=1
        idroom=getidroom[int(input("room no : "))-1]["stream"]
        if "loop" in mode:
            ittkn=mode.replace("loop ","")
            tkn1=int(ittkn.split("-")[0])
            tkn2=int(ittkn.split("-")[1])
            while True:
                quitt=False
                tokenlup=token[tkn1-1:tkn2-1]
                for tkn in tokenlup:
                    texx=input("text :")
                    if texx=="q":
                        quitt=True
                        break
                    getapi.send(tkn,idroom,texx)
                if quitt==True:
                    break
        else:
            while True:
                tkn=token[int(mode)]
                texx=input("text :")
                if texx=="q":
                    break
                getapi.send(tkn,idroom,texx)
    if x=="4":
        getidroom=getapi.getroom(random.choice(token))
        x=1
        for idr in getidroom:
            print(f"{x}. {idr['user_nicename']}")
            x+=1
        idroom=getidroom[int(input("room no : "))-1]
        namahost,streamid,uid=idroom["user_nicename"],idroom["room_id"],idroom["uid"]

        tokengift=token[int(input("token no : "))-1]
        reqdata=getapi.getgift(tokengift)
        import json
        print(json.dumps(reqdata,indent=2))
        listgift=reqdata["data"]["gift_list"]
        newlistgift = sorted(listgift, key=lambda d: d['need_coin']) 
        for pgift in newlistgift:
            giftid=pgift['id']
            giftname=pgift['gift_name']
            amount=pgift['need_coin']
            print(f"   [{giftid}] [{amount}]   \t{giftname}")
        while True:
            print(f"Host : {namahost}")
            print(c("green",f"coin : {reqdata['data']['coin']}",0))
            inpp=input("Gift id : ")
            if inpp=="q":
                break
            getapi.gift(tokengift,streamid,inpp,uid,input("jumlah : "))