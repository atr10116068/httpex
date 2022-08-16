import websocket
import json
import time
import requests
import sys
import seting
import getlive
import ambil
import random
import pyrebase
import os
import pytz
import datetime
from tinydb import *
import translatepy as trs

dat = {
    "admin": [
        "1119943580",
        "1708242561",
        "1696182045",
        "1665699504",
        "1037219061",
        "1188860696",
        "1696985118",
        "1702716897",
        "1702616359",
        "1000361907",
        "1298487258"
    ],
    "minimumlvl": 7
}
host = ["1"]
lepel = {
    "1": 15,  # host
    "13": 2,
    "14": 3,
    "2": 4,
    "4": 5,
    "5": 6,
    "6": 7,
    "7": 8,
    "9": 9,
    "8": 10,
    "10": 11,
    "11": 12,
    "3": 13,
    "12": 14,  # admin
}
tokk = ambil.token()
persi = seting.versi()
token = tokk[int(input("token ke : "))-1]
tokenhost = ambil.tokenhost()
room = getlive.roomall()


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


def getdurasi(x1):
    now = datetime.datetime.now(pytz.timezone("Asia/Jakarta"))
    s1 = (now.strftime("%H%M"))
    ss1 = datetime.datetime.strptime(s1, "%H%M")
    # print(ss1)

    dttr = x1
    tes = datetime.datetime.strptime(dttr, '%H:%M')
    s2 = (tes.strftime("%H%M"))
    ss2 = datetime.datetime.strptime(s2, "%H%M")
    # print(ss2)

    return(ss1-ss2)


def carihos(namhost):
    datsen = {}
    try:
        dt = db.child('host').get()
        chil = []
        x = 0
        for t in dt:
            x += 1
            nama = t.val()["nickname"]
            if namhost == nama:
                chil.append(nama)
                print(f"{x}. {nama}")

        cil = chil[0]
        getrum = db.child('host').child(cil).get()
        rum = getrum.val()
        duras = getdurasi(rum["jamlive"][:5])

        datsen["status"] = True
        datsen["durasi"] = f"{duras}"[:-3]
        datsen["nama"] = rum["nickname"]
        datsen["last_time"] = rum["last_live"][:-3]
        if rum["is_live"] == 1:
            datsen["live"] = "Lagi Live"
            datsen["status"] = True
        else:
            datsen["live"] = "Lagi Off"
            datsen["status"] = False
    except:
        datsen["status"] = False

    return datsen


def jumhost():
    rgame = getlive.roomgame(
        {"idx": 1, "result": [], "rapihkanjson": [], "terfilter": []})
    rindo = getlive.roomindo(
        {"idx": 1, "result": [], "rapihkanjson": [], "terfilter": []})
    rsexy = getlive.roomsexy(
        {"idx": 1, "result": [], "rapihkanjson": [], "terfilter": []})
    dat = {
        "game": len(rgame),
        "indo": len(rindo),
        "sexy": len(rsexy),
    }
    return dat


x = 1
for i in room:
    print("{}. {}".format(str(x), i["nickname"]))
    x += 1

inp = input("room nomor : ")
idroom = room[int(inp)-1]["live_id"]
print(f'\nTarget Room : {room[int(inp)-1]["nickname"]} [{idroom}]')
os.system(f'start cmd /c python moddetectorhost.py {idroom}')
datan = b"ping"
uriweb = "wss://dt001wsgew.qrdnk.cn/?token="+token

param = {
    "upgrade": "websocket",
    "connection": "Upgrade",
    "Accept-Encoding": "gzip",
    "host": "yoogs01wltb.dt01showxx03.com",
    "user-agent": f"HS-Android Mozilla/5.0 (Linux; Android 8.1.0; SM-J730F Build/{random.randint(1000,9999)}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.{random.randint(1000,9999)}.129 Mobile Safari/537.36",
}


def sen(id, tok, tex):
    uri = "https://wjxwd01mwyo.dt01showxx02.com/App/Live/SendMsg"
    headers = {
        "user-agent": f"HS-Android Mozilla/5.0 (Linux; Android 8.1.0; SM-J730F Build/{random.randint(1000,9999)}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.{random.randint(1000,9999)}.129 Mobile Safari/537.36",
        "bundleidentifier": "user",
        "x-token": tok,
        "accept-encoding": "identity",
        "host": "wjxwd01mwyo.dt01showxx02.com",
        "connection": "keep-alive"
    }
    para = {"live_id": id, "content": tex}

    req = requests.get(uri, params=para, headers=headers)
    ress = json.loads(req.text)
    return ress


def getinfo(x):
    uriweb = "https://wjxwd01mwyo.dt01showxx02.com/App/User_User/Info"
    headers = {
        "user-agent": f"HS-Android Mozilla/5.0 (Linux; Android 8.1.0; SM-J730F Build/{random.randint(1000,9999)}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.{random.randint(1000,9999)}.129 Mobile Safari/537.36",
        "bundleidentifier": "user",
        "x-token": x,
        "accept-encoding": "identity",
        "host": "wjxwd01mwyo.dt01showxx02.com",
        "connection": "keep-alive",
    }
    stat = 0
    while stat != 200:
        f = requests.get(uriweb, headers=headers)
        stat = f.status_code
        if stat == 200:
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
        else:
            disp("Reconnect")
    return krm


def gas2(id, tok):
    uri1 = f"https://wjxwd01mwyo.dt01showxx02.com/App/Live/RealTimePeopleList?live_id={id}&page=1"
    headers = {
        "User-Agent": f"HS-Android Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.17{random.randint(1000,9999)}.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.{random.randint(1000,9999)}.82 Mobile Safari/537.36",
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


aidiku = getinfo(token)[3]


def lagi():
    import _thread as thread

    def on_message(ws, message):
        datadadu = json.loads(message)
        try:
            if datadadu[0]["action"] == "connected":
                print(f'\t\t{datadadu[0]["data"]["msg_body"]["client_id"]}')
                uriweb = "https://wjxwd01mwyo.dt01showxx02.com/App/LiveEnter/JoinGroup"
                headers = {
                    "User-Agent": f"HS-Android Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.17{random.randint(1000,9999)}.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.{random.randint(1000,9999)}.82 Mobile Safari/537.36",
                    "BundleIdentifier": "user",
                    "X-Token": token,
                    "Accept-Encoding": "identity",
                    "X-Version": persi,
                    "Host": "wjxwd01mwyo.dt01showxx02.com",
                    "Connection": "Keep-Alive"
                }
                query = f'live_id={idroom}&client_id={datadadu[0]["data"]["msg_body"]["client_id"]}&type=1'
                req = requests.get(uriweb, params=query, headers=headers)
                ress = json.loads(req.text)
                print(ress)

            if datadadu[0]["action"] == "send_msg":
                utex = datadadu[0]['data']['msg_body']['content']
                udata = {
                    "uid": datadadu[0]['data']['msg_body']['show_id'],
                    "ulvl": datadadu[0]['data']['msg_body']['vip'],
                    "uname": datadadu[0]['data']['msg_body']['nickname'],
                    "utex": utex,
                }
                db = TinyDB(f"{idroom}.json")
                tbl = Query()
                lentbl = len(db.all())
                if lentbl > 1:
                    ismod = True
                    if udata["uid"] == aidiku:
                        ismod = False
                        print("ini aidi ku")
                    for iterm in range(5):
                        sys.stdout.write(f"Scanning {iterm}    \r")
                        sys.stdout.flush()
                        if len(db.search(tbl["uid"] == udata["uid"])) == 0:
                            print("tidak ada")
                            time.sleep(1)
                            db = TinyDB(f"{idroom}.json")
                            tbl = Query()
                        else:
                            ismod = False

                    if ismod == True:
                        sen(idroom, token,
                            f"{udata['uname']} tidak terdeteksi di room")
                    print(udata["uname"])
        except Exception as e:
            print(f"Error : {e}")

    def on_error(ws, error):
        pass
        # print("error : "+str(error))

    def on_close(ws, x, y):
        for i in range(3):
            sys.stdout.write(f"Reconnect after {i} \r")
            sys.stdout.flush()
            time.sleep(1)
        print("\nReconnect")
        lagi()

    def on_open(ws):
        def run(*args):
            ws.send(datan)
            # ws.close()
        thread.start_new_thread(run, ())

    if __name__ == "__main__":
        # websocket.enableTrace(True)
        ws = websocket.WebSocketApp(uriweb,
                                    header=param,
                                    on_open=on_open,
                                    on_message=on_message,
                                    on_error=on_error,
                                    on_close=on_close)

        ws.run_forever()


lagi()
