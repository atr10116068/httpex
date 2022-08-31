import ambil
import getapi
import time
import sys
import webbrowser
import random
import json
import pytz
import requests
from datetime import datetime
from colorama import Fore, Style, init
from tinydb import *
init()

tini = TinyDB("adminbot.json")
ataro = TinyDB("ataroid.json")
db = Query()


def oweb(url):
    webbrowser.register('chrome',
                        None,
                        webbrowser.BackgroundBrowser("C:\\Users\\User\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe"))
    webbrowser.get('chrome').open_new(url)


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
gumawok = {'id': 55, 'type': 1, 'mark': 4, 'swf': 'svga/IsRsDvDOnqctBs0trLlWazQbe4ZEdGI6L6F.svga', 'gift_name': 'gumawok',
           'need_coin': 100, 'gift_icon': 'image/8MksAJFIU7PXbI76ydUs3iGglP6YTWHvpBI.png', 'swf_time': '0.00', 'activity_tag': ''}
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
11. receive reward
12. top up
13. msg All
14. search agency
15. chatbot
16. set random profile
"""
while True:
    x = input(f"{menus}-> ")
    if x == "1":  # cek akun
        jeda = float(input("jeda : "))
        ftkn = input("[no] or [no-no] or enter(all): ")
        jumkoin = 0
        x = 0
        if ftkn == "":
            itrtkn = token
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
        elif "-" in ftkn:
            tkn1, tkn2 = int(ftkn.split("-")[0]), int(ftkn.split("-")[1])
            itrtkn = token[tkn1-1:tkn2]
            x = tkn1-1
            for tkn in itrtkn:
                try:
                    acc = getapi.profile(tkn)
                    x += 1
                except:
                    break

                if acc != 0:
                    acc = acc["data"]
                    warnalvl = "white"
                    if acc["vip_level"] < 1:
                        warnalvl = "yellow"
                    elif acc["vip_level"] < 2:
                        warnalvl = "blue"
                    elif acc["vip_level"] < 3:
                        warnalvl = "magenta"
                    elif acc["vip_level"] < 4:
                        warnalvl = "green"
                    else:
                        warnalvl = "red"
                    print(
                        f'[{x}/{len(itrtkn)+tkn1-1}].  {c(warnalvl,acc["id"],0)}\t{acc["user_nicename"]} {c("cyan",acc["diamonds"],0)} {c("yellow",acc["coin"],0)} ')
                    jumkoin += int(acc["diamonds"])
                    time.sleep(jeda)
        else:
            tkn1 = token[int(ftkn)-1]
            print(tkn1)
            acc = getapi.profile(tkn1)
            acc = acc["data"]
            print(
                f'{ftkn}.\t{c("magenta",acc["id"],0)}\t{acc["user_nicename"]} {c("cyan",acc["diamonds"],0)} {c("yellow",acc["coin"],0)} ')

        print(f"jumlah Diamond +- {c('cyan',jumkoin,0)}")
    if x == "2":  # get token
        tkn = token[int(input("token no : "))-1]
        acc = getapi.profile(tkn)
        print(acc["data"]["token"])
    if x == "3":  # chat
        mode = input("mode [no] [no-no] : ")
        getidroom = getapi.getroom(random.choice(token))
        x = 1
        for idr in getidroom:
            print(f"{x}. {idr['user_nicename']}")
            x += 1
        idroom = getidroom[int(input("room no : "))-1]["stream"]
        if "-" in mode:
            ittkn = mode
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
    if x == "4":  # gift
        rdmtkn = random.choice(token)
        getidroom = getapi.getroom(rdmtkn)
        x = 1
        for idr in getidroom:
            print(f"{x}. {idr['user_nicename']}")
            x += 1

        idroom = getidroom[int(input("room no : "))-1]
        namahost, streamid, uid = idroom["user_nicename"], idroom["room_id"], idroom["uid"]

        tkn1, tkn2, jeda = 0, 0, 10
        ftkn = input("[no] or [no-no] or enter(all): ")
        if ftkn == "":
            tokengift = token
        elif "-" in ftkn:
            tkn1, tkn2 = int(ftkn.split("-")[0]), int(ftkn.split("-")[1])
            jeda = float(input("jeda : "))
            tokengift = token[tkn1-1:tkn2-1]
        else:
            tokengift = token[int(ftkn)-1:int(ftkn)]

        reqdata = getapi.getgift(rdmtkn)
        listgift = reqdata["data"]["gift_list"]
        listgift.append(gumawok)
        newlistgift = sorted(listgift, key=lambda d: d['need_coin'])
        for pgift in newlistgift:
            giftid = pgift['id']
            giftname = pgift['gift_name']
            amount = pgift['need_coin']
            print(f"   [{giftid}] [{amount}]   \t{giftname}")
        while True:
            inpp = input("Gift id : ")
            if inpp == "q":
                break
            else:
                jumgip = input("jumlah : ")
                for tokengiftr in tokengift:
                    print(f"Host : {namahost}")
                    if inpp == "q":
                        break
                    getapi.enter(tokengiftr, uid)
                    time.sleep(1)
                    getapi.gift(tokengiftr, streamid, inpp, uid, jumgip)
                    time.sleep(jeda)
    if x == "5":  # getuid
        uaidi = ambil.uid()
        tkn1, tkn2,  tknall, tkn = 0, 0, 0, 0
        print(f"Jumlah UID : {len(uaidi)}")
        if input("Q to Quit : ") != "q":
            ftkn = input("[no] or [no-no] or enter(all): ")
            if ftkn == "":
                tknall = uaidi
            else:
                if "-" in ftkn:
                    tkn1, tkn2 = int(ftkn.split(
                        "-")[0]), int(ftkn.split("-")[1])
                else:
                    tkn = int(ftkn)
            if tkn1 != 0 and tkn2 != 0 or tknall != 0:
                x = 1
                if tknall != 0:
                    itrtkn = uaidi
                else:
                    itrtkn = uaidi[tkn1-1:tkn2]
                    x = tkn1
                disp = ""
                for tkn in itrtkn:
                    disp += (
                        f'{x}.\t{c("cyan",tkn["no"],0)}\t[{c("magenta",tkn["pass"],0)}]\n')
                    x += 1
                print(disp)
            else:
                tkn = uaidi[tkn-1]
                print(
                    f'{x}.\t{c("cyan",tkn["no"],0)}\t[{c("magenta",tkn["pass"],0)}]')
    if x == "6":  # enter room
        mode = input("mode [no-no] : ")
        getidroom = getapi.getroom(random.choice(token))
        x = 1
        for idr in getidroom:
            print(f"{x}. {idr['user_nicename']}")
            x += 1
        idxrum = int(input("room no : "))
        idroom = getidroom[idxrum-1]["stream"]
        aidi = getidroom[idxrum-1]["uid"]
        if "-" in mode:
            jeda = float(input("jeda : "))
            ittkn = mode
            tkn1 = int(ittkn.split("-")[0])
            tkn2 = int(ittkn.split("-")[1])
            tokenlup = token[tkn1-1:tkn2-1]
            while True:
                texx = input("e/ex enter/exit :")
                if texx == "q":
                    break
                if texx == "e":
                    xi = 1
                    for tkn in tokenlup:
                        getapi.enter(tkn, aidi)
                        print(xi)
                        xi += 1
                        time.sleep(jeda)
                if texx == "ex":
                    xi = 1
                    for tkn in tokenlup:
                        getapi.kuit(tkn, aidi)
                        print(xi)
                        xi += 1
                        time.sleep(jeda)
    if x == "7":  # jastem
        targetgip = int(input("Target Gift : "))
        inpjed = input("jeda : ")
        if inpjed == "":
            jeda = float(1.0)
        else:
            jeda = float(inpjed)
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
            idxrum = int(input("room no : "))
            print("\n\n\n\n\n\n\n\t\t\t\t[ JASTEM ATARO ]\n")
            idroom = getidroom[idxrum-1]["stream"]
            aidir = getidroom[idxrum-1]["uid"]

            reqdata = getapi.getgift(itrtkn[0])
            listgift = reqdata["data"]["gift_list"]
            newlistgift = sorted(
                listgift, key=lambda d: d['need_coin'], reverse=True)
            setop = False
            for tkn in itrtkn:
                try:
                    acc = getapi.profile(tkn)
                    x += 1
                except:
                    break
                if acc != 0:
                    acc = acc["data"]
                    # ________________________________
                    rstream = idroom
                    nama = acc["user_nicename"]
                    while len(nama) < 15:
                        nama += " "
                    aidi = acc["id"]
                    dm = acc["diamonds"]
                    # ________________________________
                    #gip = token, stream, idgift, liveuid, num
                    for tgip in newlistgift:
                        gname = tgip["gift_name"]
                        while len(gname) < 24:
                            gname += " "
                        gdm = tgip["need_coin"]
                        gid = tgip["id"]
                        if jumgift >= targetgip:
                            setop = True
                            break
                        # jika dm gk kosong dan dibawah 100K
                        if int(dm) > 2501 and int(dm) > gdm and int(dm) < 550000:
                            # random biar ga sama
                            for acakin in range(1, random.randint(2, 15)):
                                getapi.gift(tkn, rstream, "55", aidir, "1")
                                jumgift += 100
                                time.sleep(2)
                            sisah = targetgip-(jumgift+gdm)
                            # print(f"kurang : {sisah}")
                            try:
                                if sisah > -600:  # jika sisahnya gak kebanyakan
                                    try:
                                        getapi.enter(tkn, aidir)
                                        time.sleep(1)
                                        getapi.follow(tkn, aidir)
                                        time.sleep(1)
                                        getapi.gift(
                                            tkn, rstream, gid, aidir, "1")
                                        jumgift += int(gdm)
                                        # print(f'       {c("cyan",nama,0)}[{c("magenta",dm,0)}]\tgift {c("cyan",gname,0)}[{c("green",gdm,0)}]\t{c("yellow",jumgift,0)}')
                                        print(
                                            f'       {c("cyan",nama,0)}\tgift {c("cyan",gname,0)}[{c("green",gdm,0)}]\t{c("yellow",jumgift,0)}')
                                    except Exception as e:
                                        print(
                                            f"Gagal tidak masuk hitungan : {e}")
                                    time.sleep(jeda)
                                    break
                                else:
                                    # print(f'   {x}. {c("magenta",nama,0)} [{c("cyan",dm,0)}]\tsaldo kurang = {c("yellow",jumgift,0)}')
                                    pass  # skip gift gede
                            except Exception as e:
                                print(e)
                                break
                    if setop == True:
                        break

            print(f"\tjumlah Gift:{c('yellow',jumgift,0)}\n\n\n\n\n")
    if x == "8":  # follow
        mode = input("mode [no-no] : ")
        aidi = input("ID target : ")
        if "-" in mode:
            try:
                ittkn = mode
                tkn1 = int(ittkn.split("-")[0])
                tkn2 = int(ittkn.split("-")[1])
                tokenlup = token[tkn1-1:tkn2-1]
                xi = 1
                for tkn in tokenlup:
                    plow = getapi.follow(tkn, aidi)
                    print(f'{xi}   : {c("green",plow,0)}')
                    xi += 1
                    time.sleep(2)
            except Exception as e:
                print(f"Error : {e}")
    if x == "9":  # cek uid
        uaidi = ambil.uid()
        bck = []
        for t in uaidi:
            if t["no"] not in bck:
                bck.append(t["no"])
            else:
                print(f'{t["no"]} ada yg sama')
    if x == "10":
        xxx = getapi.profileuser(token[0], input("id user : "))["data"]
        print(json.dumps(xxx, indent=2))

        itk = input("Token (enter to skip): ")
        if len(itk) != 0:
            print(getapi.updateuser(token[int(itk)-1]))
    if x == "11":  # receive follow
        mode = input("[no-no] : ")
        if "-" in mode:
            ittkn = mode
            tkn1 = int(ittkn.split("-")[0])
            tkn2 = int(ittkn.split("-")[1])
            tokenlup = token[tkn1-1:tkn2-1]
            for tkn in tokenlup:
                plow = getapi.rewardlist(tkn)["data"]
                for piop in plow:
                    print(f'{c("blue",piop,0)}')
                    for piop2 in plow[piop]:
                        # print(f'{c("green",json.dumps(piop2,indent=2),0)}')
                        if piop2["info"]["complete_status"] == 1:  # terbuka
                            if piop2["info"]["status"] == 1:  # belum claim
                                # print(f'{c("green",json.dumps(piop2,indent=2),0)}')
                                print(
                                    f'{c("yellow",piop2["info"]["en_name"],0)}')
                                for idxtask in piop2["task"]:
                                    kuda = getapi.rewardclaim(
                                        tkn, idxtask["task_record_id"])
                                    print(kuda)
                                    if kuda["code"] == 200:
                                        print(
                                            f"\tClaim : {c('green',kuda['status'],0)}")
                        else:
                            # print(json.dumps(piop2,indent=2))
                            print(piop2["info"]["en_name"])

                time.sleep(2)
    if x == "12":
        mode = input("Token ke :")
        tkn = token[int(mode)-1]
        print(getapi.tu(tkn))
    if x == "13":
        mode = input("Token ke :")
        tkn = token[int(mode)-1]
        texx = input("text :")
        if texx == "q":
            break

        getidroom = getapi.getroom(tkn)
        for idrt in getidroom:
            idroom = idrt["stream"]
            getapi.send(tkn, idroom, texx)
            time.sleep(1)
        print(getapi.tu(tkn))
    if x == "14":
        tkn = token[random.randint(10, 100)]
        agc = input("agency :")
        if agc == "q":
            break

        getidroom = getapi.getroom(tkn)
        print(f"\n\n\n")
        for idrt in getidroom:
            idroom = idrt["uid"]
            nams = idrt["user_nicename"]
            if agc in nams.lower():
                print(f'   [{c("green",idroom,0)}]\t{c("cyan",nams,0)}')
        print(f"\n\n\n")
    if x == "15":  # chat
        mode = "5"
        tkn = token[int(mode)-1]
        getidroom = getapi.getroom(tkn)
        x = 1
        for idr in getidroom:
            print(f"{x}. {idr['user_nicename']}")
            x += 1
        pilop = int(input("room no : "))
        idroom = getidroom[pilop-1]["stream"]
        roomuid = getidroom[pilop-1]["uid"]
        bck = []
        simionoff = False
        while True:
            popo = getapi.getmsg(tkn, idroom)
            if popo["code"] == 200:
                for itrpop in popo["data"]["list"]:
                    tz = pytz.timezone("Asia/Jakarta")
                    now = datetime.now(tz)
                    waktu = now.strftime("%H%M")
                    datac = {
                        "uid": itrpop["uid"],
                        "nama": itrpop["nick"],
                        "vip": itrpop["vip"],
                        "chat": itrpop["content"],
                        "waktu": waktu,
                    }
                    uid, nama, vip, chat, waktu = datac["uid"], datac[
                        "nama"], datac["vip"], datac["chat"], datac["waktu"]

                    if itrpop["is_robot"] == 0:  # bukan robot

                        for jeda in range(1, 5):
                            tmbh = str(int(waktu)+jeda)
                            if len(tmbh) == 3:
                                tmbh = f"0{tmbh}"
                            datacc = {
                                "uid": itrpop["uid"],
                                "nama": itrpop["nick"],
                                "vip": itrpop["vip"],
                                "chat": itrpop["content"],
                                "waktu": tmbh,
                            }
                            bck.append(datacc)

                        dilarang = ["kamu ga boleh ya sayang ya",
                                    "apasih... aku ga kenal kamu",
                                    "cuma adminku yg boleh ya kak",
                                    "ih gak mau, gak suka..."]
                        if datac not in bck:
                            print(f' [{waktu}][{uid}]\t{nama}\t{chat}')
                            bck.append(datac)
                            if chat.lower() == "simi":
                                if tini.contains(db.uid == uid):
                                    cet = ["ada apa miminku?",
                                           f"apa sayangku {nama}"]
                                    getapi.send(
                                        tkn, idroom, random.choice(cet))
                                else:
                                    cet = ["apa si manggil manggil", "ada apa babi",
                                           "manggil sekali lagi aku jitak nih", "bodo amat , ga keliatan"]
                                    getapi.send(
                                        tkn, idroom, random.choice(cet))
                                print(f"simi-> {chat}")
                            if chat.lower() == "help":
                                if tini.contains(db.uid == uid):
                                    cet = """
help
simi [on/off]
.add admin [id]
.del admin [id]
.agency [nama]
.gift [nomer] [id]"""
                                    getapi.send(
                                        tkn, idroom, cet)
                                else:
                                    getapi.send(
                                        tkn, idroom, random.choice(dilarang))
                                print(f"help-> {chat}")

                            if chat.startswith("simi gift "):
                                if ataro.contains(db.uid == uid):
                                    namagenc = chat.replace("simi gift ", "")
                                    tokengiftbot = namagenc.split(" ")[0]
                                    idgiftbot = namagenc.split(" ")[1]
                                    getapi.gift(token[int(tokengiftbot)-1], idroom,
                                                idgiftbot, roomuid, "1")
                                else:
                                    getapi.send(
                                        tkn, idroom, random.choice(dilarang))
                                print(f"gift-> {chat}")
                            elif chat.startswith("simi "):
                                if tini.contains(db.uid == uid):
                                    switer = chat.replace("simi ", "")
                                    if uid != "2550918":  # simi
                                        if switer.lower() == "on":
                                            simionoff = True
                                            getapi.send(
                                                tkn, idroom, "Sudah on")
                                            break
                                        elif switer.lower() == "off":
                                            simionoff = False
                                            getapi.send(
                                                tkn, idroom, "Sudah off")
                                else:
                                    getapi.send(
                                        tkn, idroom, random.choice(dilarang))

                            if chat.startswith(".add admin "):
                                if tini.contains(db.uid == uid):
                                    uidmin = chat.replace(".add admin ", "")
                                    if tini.contains(db.uid == int(uidmin)):
                                        getapi.send(tkn, idroom, "Sudah ada")
                                    else:
                                        tini.insert({"uid":  int(uidmin)})
                                        getapi.send(
                                            tkn, idroom, "Sudah ditambah")
                                else:
                                    getapi.send(
                                        tkn, idroom, random.choice(dilarang))
                                print(f"add-> {chat}")
                            elif chat.startswith(".del admin "):
                                if tini.contains(db.uid == uid):
                                    uidmin = chat.replace(".del admin ", "")
                                    if tini.contains(db.uid == int(uidmin)):
                                        tini.remove(
                                            where('uid') == int(uidmin))
                                        getapi.send(
                                            tkn, idroom, "Sudah dihapus")
                                    else:
                                        getapi.send(tkn, idroom, "Tidak ada")
                                else:
                                    getapi.send(
                                        tkn, idroom, random.choice(dilarang))
                                print(f"delete-> {chat}")
                            elif chat.startswith(".agency "):
                                if tini.contains(db.uid == uid):
                                    namagenc = chat.replace(".agency ", "")
                                    getidroombot = getapi.getroom(tkn)
                                    laip = []
                                    for poiu in getidroombot:
                                        if namagenc.lower() in poiu['user_nicename'].lower():
                                            laip.append(poiu['user_nicename'])
                                    if len(laip) > 6:
                                        getapi.send(
                                            tkn, idroom, "Lebih dari 6")
                                    else:
                                        disp = ""
                                        for pouiy in laip:
                                            disp += f"\n{pouiy}"
                                        getapi.send(tkn, idroom, disp)
                                else:
                                    getapi.send(
                                        tkn, idroom, random.choice(dilarang))
                                print(f"agency-> {chat}")
                            if simionoff == True:
                                # EA ayaa
                                if uid != 2550918 and chat.startswith(".") == False:
                                    try:
                                        smi = getapi.simi(chat)["success"]
                                        if smi == "Aku tidak mengerti apa yang kamu katakan.Tolong ajari aku.":
                                            pass
                                        else:
                                            getapi.send(tkn, idroom, smi)
                                        print(f"3-> {chat}")
                                    except Exception as e:
                                        print(f"   Error : {e}")
                sys.stdout.write(
                    "--------------------------------------------->  \r")
                sys.stdout.flush()
                # for t in bck:
                #     print(t)
                for tm in range(2, 0, -1):
                    sys.stdout.write(f"   {tm}   \r")
                    sys.stdout.flush()
                    time.sleep(1)
    if x == "16":
        tkn1, tkn2, jeda = 0, 0, 10
        ftkn = input("[no] or [no-no]: ")
        if "-" in ftkn:
            tkn1, tkn2 = int(ftkn.split("-")[0]), int(ftkn.split("-")[1])
            jeda = float(input("jeda : "))
            tokengift = token[tkn1-1:tkn2-1]
        else:
            tokengift = token[int(ftkn)-1:int(ftkn)]

        for tkn in tokengift:
            xxs = getapi.updaterandom(tkn)
            print(xxs)

#  𓌸 𓌹 𓌺(◣_◢)𓌸 𓌹 𓌺
