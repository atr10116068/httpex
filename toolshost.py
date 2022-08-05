import requests
import seting
import os
import sys
import time
import random
import json
import getlive
import pyrebase
from colorama import Fore, Style, init
init()

persi = seting.versi()
config = {
    "apiKey": "AIzaSyDo7m9xUXkOiCVjuS6kKwkLchejkUNl5IY",
    "authDomain": "attools-cc537.firebaseapp.com",
    "databaseURL": "https://attools-cc537-default-rtdb.asia-southeast1.firebasedatabase.app/",
    "projectId": "attools-cc537",
    "storageBucket": "attools-cc537.appspot.com",
    "messagingSenderId": "181490859838",
    "appId": "1:181490859838:web:426c0a2f365cec8206f66f",
    "measurementId": "G-DY46HYTHT6"
}


firebase = pyrebase.initialize_app(config)
db = firebase.database()


gip = {}
tkn = input("token host : ")
if tkn != "":
    db.child("account").child("host").update({"token": tkn})

req = db.child('account').child('host').get()
tkn = req.val()["token"]
print(tkn)
dbuser = {
    # Admin
    "1146427296": ["green", "CHECKER BLING2 [Uler]"],
    "1000812019": ["green", "Checker02!"],
    "1011911296": ["green", "Bling2.com [Biawak]"],
    "1006906064": ["green", "Gift Bling2"],

    # Host
    "1051068531": ["red", "TRBANG BERSMA ROMAWI"],
    "1088559089": ["red", "TerbangBersamaRIMOWA"],
    "1003660226": ["blue", "Nemo [Dwi_queen]"],
    "1120206214": ["blue", "Good•BOYSS [Monokrom]"],
    "1176210414": ["blue", "Mowgliee"],
    "1109833110": ["blue", "MS•QIN [Qinquin]"],
    "1000361907": ["blue", "VOD一KA"],
    "1022223339": ["cyan", "Zaradisca"],
    "1225716607": ["cyan", "Cikman_Cuek"],
    "1022223339": ["cyan", "INDO : Zaradisca"],
    "1054237274": ["cyan", "RumahBesar [Ucok]"],
    "1000897849": ["cyan", "MobilDuaPintu [Ucok]"],
    "1208215215": ["yellow", "Save Money"],
    "1157616770": ["yellow", "sic bo forever [Jenny]"],
    "1217474222": ["yellow", "new xiee [Jenny98]"],
    "1187168610": ["yellow", "CryB@bi [zaradisca]"],
    "1000786334": ["yellow", "welcome [brown]"],
    "1378728127": ["white", "AYANGNYA MONCHROME [doinya monok]"],
    "1000833921": ["white", "tuyulnya [PODKA]"],
    "1303984570": ["white", "Baby Aurora"],
    "1109926509": ["white", "‌INDO : Melan"],
    "1361808931": ["white", "Crazyrich1 Qweenshy"],
    "1400006508": ["white", "Caramel Methys"],
    "1384497142": ["white", "Gigii"],
    "1032360190": ["white", "xiexi [RBK]"],

    # Viwer
    "1067014972": ["red", "wekawekaGONZAkatanya"],
    "1254948522": ["cyan", "RaJa TyPo [spender qin]"],
    "1223382131": ["red", "GenX"],
    "1027477350": ["red", 'hy" six [Sanji06]'],
    "1144080484": ["blue", "lonelyyy"],
    "1119943580": ["blue", "ATARO"],
    "1072820748": ["blue", "DJ_AJA"],
    "1064358125": ["blue", "A̶ʏᴀɴɢ^ɢᴇᴍᴏʏ"],
    "1015623301": ["blue", "Bank prof"],
    "1292725521": ["cyan", "▄█▀ ▅▀▅ ▀▅▀ ▅▀▅ ᴿⁱᶜ̲"],
    "1120294042": ["cyan", "♧ K 1 NG  DragoN ♧"],
    "1020681469": ["cyan", "K  E  L  L  I  N  G"],
    "1098678598": ["cyan", "MR•BOM"],
    "1216036215": ["white", "✨HARLEQUIN✨"],
    "1281083646": ["cyan", "salah - [DJ]"],
    "1124114046": ["cyan", "KANG_GURU"],
    "1185496200": ["cyan", "༺BàŗbìęBőy༻"],
    "1259631846": ["cyan", "Calon Sarjana"],
    "1003474155": ["cyan", "~Kudaponi~ᵒᵍᵗᵍ"],
    "1006183395": ["yellow", "PΣ YΛПK"],
    "1397151468": ["white", "Bang_Jingan"],
    "1283904252": ["white", "New J1nG4n"],
    "1000190406": ["white", "Gg,bj [ALEX]"],
    "1216036215": ["white", "BOOMBYSTIC"],
}
dbbuntut = {
    "1119943580": {"n": "Bang ATARO", "r": ""},
    "1000735200": {"n": "alfi", "r": ""},
    "1019005912": {"n": "Aryho", "r": ""},
}

sett = {
    "1": {"clr": "black", "lvl": "1"},
    "2": {"clr": "yellow", "lvl": "4"},
    "3": {"clr": "red", "lvl": "13"},
    "4": {"clr": "yellow", "lvl": "5"},
    "5": {"clr": "cyan", "lvl": "6"},
    "6": {"clr": "cyan", "lvl": "7"},
    "7": {"clr": "blue", "lvl": "8"},
    "8": {"clr": "red", "lvl": "10"},
    "9": {"clr": "blue", "lvl": "9"},
    "10": {"clr": "red", "lvl": "11"},
    "11": {"clr": "red", "lvl": "12"},
    "12": {"clr": "green", "lvl": "Admin"},
    "13": {"clr": "white", "lvl": "2"},
    "14": {"clr": "white", "lvl": "3"},
}


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


def jeda(o):
    for t in range(int(o)):
        sys.stdout.write(f"  Wait for {str(t)} \r")
        sys.stdout.flush()
        time.sleep(1)
    sys.stdout.write(
        f'{c("blank","==========================================",0)}')


def kirimmsg(aidi, x, zx):
    uriweb = "https://wjxwd01mwyo.dt01showxx02.com/App/Live/SendMsg"
    headers = {
        "user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.171019.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36",
        "bundleidentifier": "user",
        "x-token": x,
        "accept-encoding": "identity",
        "host": "wjxwd01mwyo.dt01showxx02.com",
        "connection": "keep-alive",
    }
    param = {"live_id": aidi, "content": zx}
    try:
        f = requests.get(uriweb, params=param, headers=headers)
        ress = json.loads(f.text)
        return ress
    except Exception as e:
        print("error : " + str(e))


def getinfo(x):
    uriweb = "https://wjxwd01mwyo.dt01showxx02.com/App/User_User/Info"
    headers = {
        "x-ws-apm-id": "155AB2F2-DB2C-4A0D-A000-CB8C655D4223-50",
        "user-agent": "Mozilla/5.0 (Linux; Android 8.10.0; Redmi 2 Plus Build/OPM1.171019.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36",
        "bundleidentifier": "anchor",
        "x-token": x,
        "x-version": persi,
        "accept-encoding": "identity",
        "host": "wjxwd01mwyo.dt01showxx02.com",
        "connection": "keep-alive",
    }
    f = requests.get(uriweb, headers=headers)
    ress = json.loads(f.text)
    print(json.dumps(ress, indent=2))
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


def gas(id, tok):
    uri = "https://wjxwd01mwyo.dt01showxx02.com/App/RedPacket/LiveRoomAdd"
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.171019.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36",
        "BundleIdentifier": "anchor",
        "X-Token": tok,
        "Accept-Encoding": "identity",
        "X-Version": persi,
        "Content-Type": "application/x-www-form-urlencoded",
        "Content-Length": "90",
        "Host": "wjxwd01mwyo.dt01showxx02.com",
        "Connection": "Keep-Alive",
    }
    param = f'live_room_id={id}&command={input("command : ")}&total_number={input("peserta : ")}&amount_type=2&issue_amount={input("coin : ")}&valid_time={input("menit : ")}'
    print(param)
    try:
        req = requests.post(uri, data=param, headers=headers)
        ress = json.loads(req.text)
        print(req.content)
        # cek keberhasilan
        # print(ress["result"]["balance"])
        return ress
    except:
        return [9, 9]


def gas2(id, tok):
    uri1 = f"https://wjxwd01mwyo.dt01showxx02.com/App/Live/RealTimePeopleList?live_id={id}&page=1"
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.171019.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36",
        "BundleIdentifier": "anchor",
        "X-Token": tok,
        "Accept-Encoding": "identitpython host/host.pyy",
        "X-Version": persi,
        "Host": "wjxwd01mwyo.dt01showxx02.com",
        "Connection": "Keep-Alive",
    }
    try:
        req1 = requests.get(uri1, headers=headers)
        ress1 = json.loads(req1.text)["result"]["list"]
        return ress1
    except:
        return [9, 9]


def cekviwer(tkn):
    room = getlive.roomall()
    x = 1
    for i in room:
        print("{}. {}".format(str(x), i["nickname"]))
        x += 1

    inp = input("room nomor : ")
    idroom = room[int(inp) - 1]["live_id"]
    namaroom = room[int(inp) - 1]["nickname"]

    while True:
        try:
            os.system("cls")
            print("\nTarget Room : " + namaroom)
            datas = gas2(idroom, tkn)
            for pp in datas:
                lvl = pp["vip"]
                aidi = pp["show_id"]
                nama = pp["nickname"]
                tex = f'    {sett[lvl]["lvl"]} "{aidi}" : ["white","{nama}"],'
                if lvl != "1":
                    print(c(sett[lvl]["clr"], tex, 0))
        except:
            print("Gagal Capture Data")
        for t in range(5, 1, -1):
            sys.stdout.write(f"{t}\r")
            sys.stdout.flush()
            time.sleep(1)


def ampau(tkn):
    room = getlive.roomall()
    x = 1
    for i in room:
        print("{}. {}".format(str(x), i["nickname"]))
        x += 1

    inp = input("room nomor : ")
    idroom = room[int(inp) - 1]["live_id"]
    namaroom = room[int(inp) - 1]["nickname"]
    print("\nTarget Room : " + namaroom)

    print(gas(idroom, tkn))

    print("selesai...")
    exit()


def find(tkn):
    while True:
        print()
        room = getlive.roomall()
        x = 1
        for i in room:
            datas = gas2(i["live_id"], tkn)
            sys.stdout.write(f"{str(x)} \r")
            sys.stdout.flush()
            namarum = i["nickname"]
            try:
                namarum = namarum.replace("INDO : ", "")
            except:
                pass

            block = 0
            for tt in datas:
                for iduser in dbuser:
                    if tt["show_id"] == iduser:
                        if block == 0:
                            print("{}".format(c("cyan", i["nickname"], 1)))
                            block = 1
                        print(
                            f'\t> {c(dbuser[iduser][0],dbuser[iduser][1],0)}')

                        if tt["show_id"] == "1254948522":
                            tkntyp = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJuYmYiOjE2NTA5NjcwMTkuNjI1Njg4LCJpYXQiOjE2NTA5NjcwMTkuNjI1Njg4LCJleHAiOjE2NTIxNzY2MTkuNjI1Njg4LCJpZCI6NDI5MzQ3Nywic2hvd19pZCI6IjE0Mjg0Njg1NjAiLCJzdGF0dXMiOjEsInR5cGUiOjIsImxldmVsIjozLCJ2aXAiOjEzLCJsYXN0X2FjdGl2ZV9kZXZpY2UiOjEsInBob25lX2lzX2JpbmRlZCI6MiwiZW1haWxfaXNfYmluZGVkIjoyfQ.6YQ09a5nXXw89QR8eIxSMsSrHI3zczTQ6MC5bNl8BjE"
                            print(kirimmsg("304203", tkntyp, namarum))
            x += 1
        jeda(10)


def active(tkn):
    print()
    room = getlive.roomall()
    x = 1
    for i in room:
        datas = gas2(i["live_id"], tkn)
        sys.stdout.write(f"{str(x)} \r")
        sys.stdout.flush()

        block = 0
        for tt in datas:
            if block == 0:
                print("\n{} {} {}".format(c("green", "====================[", 0),
                                          c("magenta", i["nickname"], 0), c("green", "]====================", 0)))
                block = 1

            tex = f'{tt["vip"]} "{tt["show_id"]}" : ["white","{tt["nickname"]}"],'
            lvl = tt["vip"]
            aidi = tt["show_id"]
            nama = tt["nickname"]
            tex = f'    {sett[lvl]["lvl"]} "{aidi}" : ["white","{nama}"],'
            if lvl != "1":
                print(c(sett[lvl]["clr"], tex, 0))
        x += 1


def buntut(tkn):
    texar = [
        "Eh ada n4m disini 🤭",
        "Dorrr...  n4m kaget ga? wkwkwk",
        "lah kok ada n4m juga",
        "cieee n4m baru dateng :v",
        "sering ke sini juga n4m?",
        "Halooooo n4m",
        "Halo n4m",
        "n4m....!!!",
        "Disini aja n4m...",
    ]
    tokensen = input("token akun typing : ")
    while True:
        print()
        room = getlive.roomall()
        x = 1
        for i in room:
            datas = gas2(i["live_id"], tkn)
            sys.stdout.write(f"{str(x)} \r")
            sys.stdout.flush()

            block = 0
            for tt in datas:
                for iduser in dbbuntut:
                    texw = random.choice(texar)
                    if tt["show_id"] == iduser:
                        if block == 0:
                            print("{}".format(c("cyan", i["nickname"], 1)))
                            block = 1
                        print(
                            f'\t> {c("red",tt["nickname"],0)}')
                        if dbbuntut[iduser]["r"] != i["nickname"]:
                            dbbuntut[iduser]["r"] = i["nickname"]

                            try:
                                tex = texw.replace(
                                    "n4m", dbbuntut[iduser]["n"])
                            except:
                                pass
                            kirimmsg(i["live_id"], tokensen, f"{tex}")
                            print(f"mengirim pesan {tex}")
            x += 1
        jeda(10)


menu = """
1. cek token
2. viwer host
3. coming soon
4. find viwer
5. scan Active viwer
6. buntutin
"""

while True:
    x = input(menu+"nomer : ")

    if x == "1":
        print(getinfo(tkn))
    elif x == "2":
        print(cekviwer(tkn))
    # elif x == "3":
    #     print(ampau(tkn))
    elif x == "4":
        find(tkn)
    elif x == "5":
        print(active(tkn))
    elif x == "6":
        while True:
            buntut(tkn)
            jeda(10)
