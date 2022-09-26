import websocket
import json
import time
import requests
import sys
import seting
import getlive
import ambil
import random
import os
from tinydb import *
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
room = getlive.roomall()

x = 1
for i in room:
    print("{}. {}".format(str(x), i["nickname"]))
    x += 1

inp = input("room nomor : ")
idroom = room[int(inp)-1]["live_id"]
print(f'\nTarget Room : {room[int(inp)-1]["nickname"]} [{idroom}]')
datan = b"ping"
uriweb = "wss://yoogs01wltb.dt01showxx03.com/?token="+token

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
            print("Reconnect")
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

piwer={}
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

            if datadadu[0]["action"] == "enter":
                udata = {
                    "uid": datadadu[0]['data']['msg_body']['show_id'],
                    "ulvl": datadadu[0]['data']['msg_body']['vip'],
                    "uname": datadadu[0]['data']['msg_body']['nickname']
                }
                piwer[udata["uid"]]=udata
                print(c("yellow",f" > masuk [{udata['uname']}]",0))

            if datadadu[0]["action"] == "send_msg":
                utex = datadadu[0]['data']['msg_body']['content']
                udata = {
                    "uid": datadadu[0]['data']['msg_body']['show_id'],
                    "ulvl": datadadu[0]['data']['msg_body']['vip'],
                    "uname": datadadu[0]['data']['msg_body']['nickname'],
                    "utex": utex,
                }
                try:
                    piwer[udata["uid"]]
                    print(c("green",f" > {udata['uname']} : {utex}",0))
                except:
                    print(c("red",f"[{udata['uname']}] : {udata['utex']}",0))
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
