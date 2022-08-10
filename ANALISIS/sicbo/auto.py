import websocket
import json
import time
import sys
import requests
import getlive
import caripola
import colorama
from colorama import Fore, Style, Back

colorama.init()


datainit = {"token": "", "pola": "", "win": 0, "lose": 0, "predik": "Seimbang"}


def sen(id, tex):
    if id != "0":
        if autosen == False:
            print(tex)
            return 0
        uri = "https://dt001piwfw.d9sph.cn/App/Live/SendMsg"
        headers = {
            "user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.171019.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36",
            "bundleidentifier": "user",
            "x-token": datainit["token"],
            "accept-encoding": "identity",
            "host": "dt001piwfw.d9sph.cn",
            "connection": "keep-alive",
        }
        para = {"live_id": id, "content": tex}

        req = requests.get(uri, params=para, headers=headers)
        ress = json.loads(req.text)
        return ress
    return "silent mode"


def c(colr, tex, dim):
    try:
        w = {
            "BLACK": Fore.BLACK,
            "RED": Fore.RED,
            "GREEN": Fore.GREEN,
            "YELLOW": Fore.YELLOW,
            "BLUE": Fore.BLUE,
            "MAGENTA": Fore.MAGENTA,
            "CYAN": Fore.CYAN,
            "WHITE": Fore.WHITE,
            "RESET": Fore.RESET,
        }
        if dim == 1:
            return f"{Style.DIM}{w[colr.upper()]} {tex} {Style.RESET_ALL}"
        else:
            return f"{w[colr.upper()]} {tex} {Style.RESET_ALL}"
    except:
        return tex


def gettoken():
    with open("user_token.json") as json_file:
        tokk = json.load(json_file)

    if inpvps == "y":
        datainit["token"] = tokk["results"][len(tokk["results"]) - 1]
    else:
        datainit["token"] = tokk["results"][tknlen - 1]


inpvps = input("run on vps y/n : ")
if inpvps != "y":
    tknlen = int(input("token ke-"))
    inpr = input("connect room? y/n : ")
    if inpr.lower() == "y":

        room = []
        for x in getlive.roomgame():
            room.append(x)
        for x in getlive.roomindo():
            room.append(x)
        for x in getlive.roomsexy():
            room.append(x)
        x = 1
        for i in room:
            print("{}. {}".format(str(x), i["nickname"]))
            x += 1
        gettoken()
        inp = input("room nomor : ")
        idroom = room[int(inp) - 1]["live_id"]
        datainit["roomid"] = idroom
        namaroom = room[int(inp) - 1]["nickname"]
        print(f"\nTarget Room : {namaroom}")

        autosen = input("send msg? y/n: ")
        if autosen.lower() == "y":
            autosen = True
        else:
            autosen = False
        autosenyn = input("send win rate msg? y/n: ")
        if autosenyn.lower() == "y":
            autosenyn = True
        else:
            autosenyn = False
        sen(datainit["roomid"], "Connected...")
    else:
        datainit["roomid"] = "0"
        autosen = False
        autosenyn = False

    autob = input("auto bet? y/n: ")
    if autob.lower() == "y":
        autob = True
    else:
        autob = False
else:
    inpr = "n"
    autosen = False
    autosenyn = False
    autob = True

inppola = input("Pola : ")
datainit["pola"] = inppola

while True:
    jumlahpola = len(datainit["pola"])
    dat = {"pola": []}
    print(f'\n\t{c("magenta","===========[ TRY ]===========",0)}')
    for x in datainit["pola"]:
        if x.lower() == "b":
            dat["pola"].append("Big")
        elif x.lower() == "s":
            dat["pola"].append("Small")
        else:
            exit()

    def getnum():
        uri = "https://dt001piwfw.d9sph.cn/App/Game_Game/GetTypeInfo"
        headers = {
            "user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.171019.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36",
            "bundleidentifier": "user",
            "x-token": datainit["token"],
            "accept-encoding": "identity",
            "x-version": "2.9.13",
            "host": "dt001piwfw.d9sph.cn",
            "connection": "keep-alive",
        }
        query = {"game_type": "toubao_1"}
        req = requests.get(uri, params=query, headers=headers)
        ress = json.loads(req.text)
        try:
            return ress["result"]["current_round"]["number"]
        except:
            gettoken()
            print("get num error")

    def hist(x):
        huri = "https://dt001piwfw.d9sph.cn/App/Game_Game/HistoryDrawList"
        hhead = {
            "user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.171019.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36",
            "bundleidentifier": "user",
            "x-token": datainit["token"],
            "accept-identity": "identity",
        }
        hparam = {"game_type": "toubao_1", "page": "1"}
        hhsl = requests.get(url=huri, params=hparam, headers=hhead)
        rett = json.loads(hhsl.text)
        if (rett["code"]) == 0:
            return 0
        else:
            return 999

    def bet(type, num):
        if autob == False:
            return 0
        rType = {
            "Big": "zonghe_da",
            "Small": "zonghe_xiao",
            "Odd": "zonghe_dan",
            "Even": "zonghe_shuang",
            "Any": "zonghe_weitou",
        }
        uri = "https://dt001piwfw.d9sph.cn/App/Game_Order/Create"
        headers = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.171019.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36",
            "BundleIdentifier": "user",
            "X-Token": datainit["token"],
            "Accept-Encoding": "identity",
            "X-Version": "2.9.13",
            "Content-Type": "application/x-www-form-urlencoded",
            "Content-Length": "25",
            "Host": "dt001piwfw.d9sph.cn",
            "Connection": "Keep-Alive",
        }
        param = {
            "live_room_id": datainit["roomid"],
            "game_type": "toubao_1",
            "game_sub": "zonghe;",
            "game_number": getnum(),
            "detail": rType[type] + ":" + num + ";",
            "multiple": "1",
        }

        try:
            req = requests.post(uri, data=json.dumps(param), headers=headers)
            ress = json.loads(req.text)
            print(ress)
        except:
            print("Failed...")

    datan = b"ping"

    def lagi():
        print(f'Prediksi Win {datainit["win"]} Lose {datainit["lose"]}{chr(9)}[ATARO]')
        try:
            import thread
        except ImportError:
            import _thread as thread

        def on_message(ws, message):
            datadadu = json.loads(message)
            try:
                if (
                    datadadu["content"]["game"] == "toubao_1"
                    and "cards" in datadadu["content"]
                ):
                    dat["pola"].append(datadadu["content"]["tip"][1])
                    if datainit["predik"] != "":
                        if datainit["predik"] == datadadu["content"]["tip"][1]:
                            datainit["win"] += 1
                            print(c("green", "\t===========[ WIN ]===========\n", 0))
                        else:
                            if datainit["predik"] != "Seimbang":
                                print(c("red", "\t===========[ LOSE ]===========\n", 0))
                                datainit["lose"] += 1

                        for tim in range(10, 1, -1):
                            sys.stdout.write(f" countdown {tim}    \r")
                            sys.stdout.flush()
                            time.sleep(1)

                        if datainit["predik"] == datadadu["content"]["tip"][1]:
                            if autosenyn == True:
                                sen(
                                    datainit["roomid"],
                                    f'Prediksi Win {datainit["win"]} Lose {datainit["lose"]}{chr(9)}[ATARO]',
                                )

                    if len(dat["pola"]) > int(jumlahpola):
                        dat["pola"].pop(0)

                    pol = ""
                    for x in dat["pola"]:
                        pol += x[:1]
                    dat["polanya"] = pol  # in while data
                    datainit["pola"] = pol  # base data

                    cr = caripola.caribs(pol)

                    cr1 = caripola.caribs(pol)
                    if cr1["predik"]["Big"] > cr1["predik"]["Small"]:
                        jara = cr1["predik"]["Small"]
                        jarb = cr1["predik"]["Big"]
                    else:
                        jara = cr1["predik"]["Big"]
                        jarb = cr1["predik"]["Small"]
                    jarakpal = (jara / jarb) * 100

                    print(f'\n{cr1["pola"]} jarak: {str(jarakpal)[0:5]}% {cr}')
                    for cr3 in range(1, int(jumlahpola) - 4):
                        filt = caripola.caribs(pol[cr3:])
                        if filt["predik"]["Big"] > filt["predik"]["Small"]:
                            fjara = filt["predik"]["Small"]
                            fjarb = filt["predik"]["Big"]
                        else:
                            fjara = filt["predik"]["Big"]
                            fjarb = filt["predik"]["Small"]
                        filtjarak = (fjara / fjarb) * 100
                        if filtjarak < jarakpal:
                            if int(filtjarak) != 50:
                                if filt["predik"]["Big"] > filt["predik"]["Small"]:
                                    dispbet = "Big"
                                elif filt["predik"]["Big"] < filt["predik"]["Small"]:
                                    dispbet = "Small"
                                else:
                                    dispbet = "Sama"

                                print(
                                    f" {str(jarakpal)[0:5]}% ==> {str(filtjarak)[0:5]}% {dispbet}\t{filt}"
                                )
                                dat["polanya"] = filt["pola"]
                                cr = filt
                                if cr["predik"]["Big"] > cr["predik"]["Small"]:
                                    jara = cr["predik"]["Small"]
                                    jarb = cr["predik"]["Big"]
                                else:
                                    jara = cr["predik"]["Big"]
                                    jarb = cr["predik"]["Small"]
                                jarakpal = (jara / jarb) * 100

                    # msgtex = f'{dat["polanya"]} Bet '
                    msgtex = f""

                    if cr["predik"]["Big"] == cr["predik"]["Small"]:
                        msgtex += "⇅"
                        datainit["predik"] = "Seimbang"
                    elif cr["predik"]["Big"] > cr["predik"]["Small"]:
                        msgtex += "🤖 ⬆️Big"
                        datainit["predik"] = "Big"
                        bet("Big", "1")
                    else:
                        msgtex += "🤖 ⬇️Small"
                        datainit["predik"] = "Small"
                        bet("Small", "1")

                    sen(datainit["roomid"], msgtex)
                    print(
                        f'{cr["pola"]} jarak terbaik: {str(jarakpal)[0:5]}% {c("cyan",datainit["predik"],0)}'
                    )
            except Exception as e:
                if "game" not in str(e):
                    print(str(e))
                else:
                    pass

        def on_error(ws, error):
            pass
            # print("error : "+str(error))

        def on_close(ws, x, y):
            # for i in range(3):
            #     sys.stdout.write(f"Reconnect after {i} \r")
            #     sys.stdout.flush()
            #     time.sleep(1)
            ws.close()

        def on_open(ws):
            def run(*args):
                ws.send(datan)

            thread.start_new_thread(run, ())

        if __name__ == "__main__":
            # websocket.enableTrace(True)
            ws = websocket.WebSocketApp(
                "wss://dt001wsgew.qrdnk.cn/?token=" + datainit["token"],
                on_open=on_open,
                on_message=on_message,
                on_error=on_error,
                on_close=on_close,
            )

            ws.run_forever()

    time.sleep(0.5)
    gettoken()
    lagi()
