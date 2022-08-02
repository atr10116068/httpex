import websocket
import ambil
import getlive
import json
import time
import random as rd
import requests
import sys

dat = {"result": []}
onlytrip = 0


def roomss(tkn, x):
    uriweb = "https://wjxwd01mwyo.dt01showxx02.com/App/Live/index?category_id=3&page=" + \
        str(x)
    headers = {
        "user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.171019.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36",
        "bundleidentifier": "user",
        "x-token": tkn,
        "accept-encoding": "identity",
        "x-version": "2.9.12",
        "host": "wjxwd01mwyo.dt01showxx02.com",
        "connection": "keep-alive"
    }
    f = requests.get(uriweb, headers=headers)
    lol = json.loads(f.text)
    return lol


def sen(id, x, msg):
    uri = "https://wjxwd01mwyo.dt01showxx02.com/App/Live/SendMsg"
    headers = {
        "user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.171019.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36",
        "bundleidentifier": "user",
        "x-token": x,
        "accept-encoding": "identity",
        "host": "wjxwd01mwyo.dt01showxx02.com",
        "connection": "keep-alive"
    }
    para = {"live_id": id, "content": msg}

    req = requests.get(uri, params=para, headers=headers)


token = ambil.token()[int(input("token no :"))-1]

room = getlive.roomall()

x = 1
for i in room:
    print("{}. {}".format(str(x), i["nickname"]))
    x += 1

inp = input("room nomor : ")
try:
    idroom = room[int(inp)-1]["live_id"]
    print("\nTarget Room : "+room[int(inp)-1]["nickname"])
except:
    print("\nTarget Room : all sicbo room")

datan = b"ping"
uriweb = "wss://dt001wsgew.qrdnk.cn/?token="+token

bckup = []
dat = {"tebak": True}


def lagi():
    print()
    print(f"Connected")
    try:
        import thread
    except ImportError:
        import _thread as thread

    def on_message(ws, message):
        datadadus = json.loads(message)
        for datadadu in datadadus:
            try:
                trip = False
                if datadadu["data"]["msg_body"]["game"] == "toubao_1":
                    dadd = datadadu["data"]["msg_body"]["tip"]
                    card = datadadu["data"]["msg_body"]["cards"]
                    if card[0] == card[1] and card[1] == card[2]:
                        trip = True
                    if trip == True:
                        trip = False
                        pesan = [
                            f"Yang dapet Triple jgn lupa berbagi",
                            f"Ekhem ANY TRIPLE..!!!",
                            f"Selamat yang jaga Any Triple",
                            f"Ada yang bet any triple? wkwkwk",
                            f"Cie Triple keluar wkwkw",
                        ]
                        ppsn = rd.choice(pesan)
                        print(ppsn)

                        for idnay in room:
                            sen(idnay["live_id"], token, ppsn)

                    elif onlytrip != 1:
                        pesan = [
                            f"gw sih sekarang nebak {dadd[1][:1]}{dadd[2][:1]}",
                            f"klo diliat dari pola, {dadd[1][:1]}{dadd[2][:1]} klo menurut gw",
                            f"{dadd[1][:1]}{dadd[2][:1]}",
                            f"wah klo pola ini sih {dadd[1][:1]}{dadd[2][:1]} jelas",
                            f"menurut pola gw kayaknya sih {dadd[1][:1]}{dadd[2][:1]}",
                            f"{dadd[1][:1]}{dadd[2][:1]}",
                            f"coba {dadd[1][:1]} all in",
                            f"{dadd[1][:1]} di tools gw",
                            f"tes {dadd[1][:1]}{dadd[2][:1]}",
                            f"all inn {dadd[2]} ya",
                            f"{dadd[1][:1]}{dadd[2][:1]} tipis",
                        ]
                        ppsn = rd.choice(pesan)
                        if dat["tebak"] == True:
                            while ppsn not in bckup:
                                if len(bckup) > 8:
                                    bckup.clear()
                                for i in bckup:
                                    print(i)
                                bckup.append(ppsn)

                                sen(idroom, token, ppsn)

                                rosting = rd.choice(
                                    [False, False, False, True, False])
                                print(rosting)
                                if rosting == True:
                                    time.sleep(13)
                                    sen(idroom, token, "telat mulu ah betnya")

                        dat["tebak"] = rd.choice(
                            [True, False, True, True, True])
                        print(f"next nebak adalah {dat['tebak']}")
                        if dat["tebak"] == False:
                            time.sleep(30)
                            sen(idroom, token, "skip nebak dlu gw")

            except:
                pass

    def on_error(ws, error):
        pass
        #print("error : "+str(error))

    def on_close(ws, x, y):
        for i in range(3):
            sys.stdout.write(f"Reconnect after {i} \r")
            sys.stdout.flush()
            time.sleep(1)
        lagi()

    def on_open(ws):
        def run(*args):
            ws.send(datan)
            # ws.close()
        thread.start_new_thread(run, ())

    if __name__ == "__main__":
        # websocket.enableTrace(True)
        ws = websocket.WebSocketApp(uriweb,
                                    on_open=on_open,
                                    on_message=on_message,
                                    on_error=on_error,
                                    on_close=on_close)

        ws.run_forever()


while True:
    print("\nConnected...")
    lagi()
    for i in range(5, 0, -1):
        sys.stdout.write(f"{i} sec to reconnect \r")
        sys.stdout.flush()
        time.sleep(1)
