import websocket
import json
import time
import sys
import requests, random
import getlive
import caripolafull
import colorama
from colorama import Fore, Style, Back

colorama.init()

datahost = {
    "data": [
        {"nama": "INDO : ochaa", "jamlive": "23:00"},
        # {"nama": "INDO : Marseille", "jamlive": "~"},
        {"nama": "INDO : Velveta", "jamlive": "20:00/00:30"},
        {"nama": "INDO : Velveta", "jamlive": "20:00/00:30"},
        {"nama": "INDO : Ayyakecil", "jamlive": "18:00"},
        {"nama": "INDO : Sasyaa__", "jamlive": "13:00"},
    ]
}

datainit = {
    "switch": "A",
    "token": "",
    "polabs": "",
    "polaoe": "",
    "bswin": 0,
    "bslose": 0,
    "oewin": 0,
    "oelose": 0,
    "predikbs": "",
    "predikoe": "",
}


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


def getpage():
    headers = {
        "user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.171019.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36",
        "bundleidentifier": "user",
        "x-token": datainit["token"],
        "accept-identity": "identity",
    }

    hparam = {"game_type": "toubao_1", "page": "1"}
    req = requests.get(
        url="https://dt001piwfw.d9sph.cn/App/Game_Game/HistoryDrawList",
        params=hparam,
        headers=headers,
        timeout=100,
    )
    reqs = json.dumps(req.json())
    reqs = json.loads(reqs)
    return reqs


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
        datainit["token"] = tokk["results"][tknlen]


inpvps = input("run on vps y/n : ")
if inpvps != "y":
    tknlen = int(input("token ke-"))
    inpr = input("connect room? y/n : ")
    if inpr.lower() == "y":

        room = []
        # for x in getlive.roomgame():
        #     room.append(x)
        for x in getlive.roomindo():
            room.append(x)
        # for x in getlive.roomsexy():
        #     room.append(x)
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
    datainit["roomid"] = ""
    autosen = False
    autosenyn = False
    autob = True

inppolabs = ""
inppolaoe = ""

gettoken()
reqpage = getpage()
page1 = {"result": []}

# reverse dictionary
for t in range(len(reqpage["result"]) - 1, -1, -1):
    page1["result"].append(reqpage["result"][t])


for dd in page1["result"]:
    inppolabs += dd["tip"][1][:1]
for dd in page1["result"]:
    inppolaoe += dd["tip"][2][:1]
datainit["polabs"] = inppolabs
datainit["polaoe"] = inppolaoe

while True:
    dibs = datainit["polabs"]
    dioe = datainit["polaoe"]

    jumlahpola = len(datainit["polabs"])
    dat = {"polabs": [], "polaoe": []}
    print(f'\n\t{c("magenta","===========[ TRY ]===========",0)}')
    time.sleep(1)
    for x in range(len(dibs)):
        if dibs[x].lower() == "b":
            dat["polabs"].append("Big")
        elif dibs[x].lower() == "s":
            dat["polabs"].append("Small")
        else:
            exit()
        if dioe[x].lower() == "o":
            dat["polaoe"].append("Odd")
        elif dioe[x].lower() == "e":
            dat["polaoe"].append("Even")
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
                    dat["polabs"].append(datadadu["content"]["tip"][1])
                    dat["polaoe"].append(datadadu["content"]["tip"][2])

                    pickhost = random.choice(datahost["data"])
                    # sen(
                    #     datainit["roomid"],
                    #     f'Jangan lupa mampir ke {pickhost["nama"]} di jam {pickhost["jamlive"]}',
                    # )

                    # print(1)
                    switchmode = [0, 0]
                    if datainit["predikbs"] != "":
                        if (
                            datainit["predikbs"]
                            == dat["polabs"][len(dat["polabs"]) - 1]
                        ):
                            datainit["bswin"] += 1
                            print(c("green", "\t===========[ BS WIN ]===========\n", 0))
                        else:
                            if datainit["predikbs"] != "Seimbang":
                                print(
                                    c("red", "\t===========[ BS LOSE ]===========\n", 0)
                                )
                                datainit["bslose"] += 1
                                switchmode[0] = 1

                        if datainit["predikbs"] == datadadu["content"]["tip"][1]:
                            if autosenyn == True:
                                sen(
                                    datainit["roomid"],
                                    f'Big/Small Win {datainit["bswin"]} Lose {datainit["bslose"]}{chr(9)}[ATARO]',
                                )
                    if datainit["predikoe"] != "":
                        if (
                            datainit["predikoe"]
                            == dat["polaoe"][len(dat["polaoe"]) - 1]
                        ):
                            datainit["oewin"] += 1
                            print(c("green", "\t===========[ OE WIN ]===========\n", 0))
                        else:
                            if datainit["predikoe"] != "Seimbang":
                                print(
                                    c("red", "\t===========[ OE LOSE ]===========\n", 0)
                                )
                                datainit["oelose"] += 1
                                switchmode[1] = 1

                        if datainit["predikoe"] == datadadu["content"]["tip"][2]:
                            if autosenyn == True:
                                sen(
                                    datainit["roomid"],
                                    f'Odd/Even Win {datainit["oewin"]} Lose {datainit["oelose"]}{chr(9)}[ATARO]',
                                )

                    for tim in range(10, 1, -1):
                        sys.stdout.write(f" countdown {tim}    \r")
                        sys.stdout.flush()
                        time.sleep(1)

                    if switchmode[0] == 1 and switchmode[1] == 1:
                        if datainit["switch"] == "A":
                            datainit["switch"] = "B"
                        else:
                            datainit["switch"] = "A"
                    print(f'Total turn : {datainit["bswin"]+datainit["bslose"]}')
                    print(
                        f'Prediksi BS Win {datainit["bswin"]} BS Lose {datainit["bslose"]}{chr(9)}[ATARO]'
                    )
                    print(
                        f'Prediksi OE Win {datainit["oewin"]} OE Lose {datainit["oelose"]}{chr(9)}[ATARO]'
                    )

                    print(2)
                    if len(dat["polabs"]) > int(jumlahpola):
                        dat["polabs"].pop(0)
                        dat["polaoe"].pop(0)

                    polbs = ""
                    poloe = ""

                    reqpage = getpage()
                    page1 = {"result": []}

                    # reverse dict
                    for t in range(len(reqpage["result"]) - 1, -1, -1):
                        page1["result"].append(reqpage["result"][t])

                    for dd in page1["result"]:
                        polbs += dd["tip"][1][:1]
                    for dd in page1["result"]:
                        poloe += dd["tip"][2][:1]

                    # print(polbs)
                    # print(poloe)
                    # sen(datainit["roomid"], polbs)
                    # sen(datainit["roomid"], poloe)
                    print(3)
                    print()
                    cr = caripolafull.cari([polbs, poloe])
                    dat["polanya"] = cr["pola"]

                    cr1 = cr
                    print(cr1)
                    if cr1["predik"]["Big"] > cr1["predik"]["Small"]:
                        jara = cr1["predik"]["Small"]
                        jarb = cr1["predik"]["Big"]
                    else:
                        jara = cr1["predik"]["Big"]
                        jarb = cr1["predik"]["Small"]
                    jarakpalbs = (jara / jarb) * 100
                    if cr1["predik"]["Odd"] > cr1["predik"]["Even"]:
                        jara = cr1["predik"]["Even"]
                        jarb = cr1["predik"]["Odd"]
                    else:
                        jara = cr1["predik"]["Odd"]
                        jarb = cr1["predik"]["Even"]
                    jarakpaloe = (jara / jarb) * 100

                    print(f'{cr1["pola"]} jarak: {str(jarakpalbs)[0:5]}% {cr}')
                    print(f'{cr1["pola"]} jarak: {str(jarakpaloe)[0:5]}% {cr}')
                    print()
                    for cr3 in range(1, int(jumlahpola) - 5):
                        # print(polbs[cr3:] + poloe[cr3:])
                        filt = caripolafull.cari([polbs[cr3:], poloe[cr3:]])
                        dat["polanya"] = filt["pola"]
                        if filt["predik"]["Big"] > filt["predik"]["Small"]:
                            fjara = filt["predik"]["Small"]
                            fjarb = filt["predik"]["Big"]
                        else:
                            fjara = filt["predik"]["Big"]
                            fjarb = filt["predik"]["Small"]
                        if filt["predik"]["Odd"] > filt["predik"]["Even"]:
                            fjaraa = filt["predik"]["Even"]
                            fjarbb = filt["predik"]["Odd"]
                        else:
                            fjaraa = filt["predik"]["Odd"]
                            fjarbb = filt["predik"]["Even"]
                        filtjarakbs = (fjara / fjarb) * 100
                        filtjarakoe = (fjaraa / fjarbb) * 100
                        if filtjarakbs < jarakpalbs or filtjarakoe < jarakpaloe:
                            if filt["predik"]["Big"] > filt["predik"]["Small"]:
                                dispbetbs = "Big"
                            elif filt["predik"]["Big"] < filt["predik"]["Small"]:
                                dispbetbs = "Small"
                            else:
                                dispbetbs = "Sama"
                            if filt["predik"]["Odd"] > filt["predik"]["Even"]:
                                dispbetoe = "Odd"
                            elif filt["predik"]["Odd"] < filt["predik"]["Even"]:
                                dispbetoe = "Even"
                            else:
                                dispbetoe = "Sama"

                            print(
                                f" {str(jarakpalbs)[0:5]}% ==> {str(filtjarakbs)[0:5]}% {dispbetbs} {str(filtjarakoe)[0:5]}% {dispbetoe}\t{filt}"
                            )
                            cr = filt
                            if cr["predik"]["Big"] > cr["predik"]["Small"]:
                                jara = cr["predik"]["Small"]
                                jarb = cr["predik"]["Big"]
                            else:
                                jara = cr["predik"]["Big"]
                                jarb = cr["predik"]["Small"]
                            jarakpalbs = (jara / jarb) * 100
                            if cr["predik"]["Odd"] > cr["predik"]["Even"]:
                                jaraa = cr["predik"]["Even"]
                                jarbb = cr["predik"]["Odd"]
                            else:
                                jaraa = cr["predik"]["Odd"]
                                jarbb = cr["predik"]["Even"]
                            jarakpaloe = (jaraa / jarbb) * 100

                    # msgtex = f'{dat["polanya"]} Bet '
                    msgtex = f"{dat['polanya']} "

                    if datainit["switch"] == "A":
                        if cr["predik"]["Big"] == cr["predik"]["Small"]:
                            msgtex += "⇅"
                            datainit["predikbs"] = ""
                        elif cr["predik"]["Big"] > cr["predik"]["Small"]:
                            msgtex += f"Big {str(100.0-jarakpalbs)[0:5]}% "
                            # msgtex += f'Big {cr["pola"]}'
                            datainit["predikbs"] = "Big"
                            bet("Big", "2")
                        else:
                            msgtex += f"Small {str(100.0-jarakpalbs)[0:5]}% "
                            # msgtex += f'Small {cr["pola"]}'
                            datainit["predikbs"] = "Small"
                            bet("Small", "2")
                        print(
                            f'{cr["pola"]} jarak terbaik: {str(100.0-jarakpalbs)[0:5]}% {c("cyan",datainit["predikbs"],0)}'
                        )

                        if cr["predik"]["Odd"] == cr["predik"]["Even"]:
                            msgtex += "⇅"
                            datainit["predikoe"] = ""
                        elif cr["predik"]["Odd"] > cr["predik"]["Even"]:
                            msgtex += f"Odd {str(100.0-jarakpaloe)[0:5]}% "
                            # msgtex += f'Big {cr["pola"]}'
                            datainit["predikoe"] = "Odd"
                            bet("Odd", "2")
                        else:
                            msgtex += f"Even {str(100.0-jarakpaloe)[0:5]}% "
                            # msgtex += f'Small {cr["pola"]}'
                            datainit["predikoe"] = "Even"
                            bet("Even", "2")
                    else:
                        if cr["predik"]["Big"] == cr["predik"]["Small"]:
                            msgtex += "⇅"
                            datainit["predikbs"] = ""
                        elif cr["predik"]["Big"] < cr["predik"]["Small"]:
                            msgtex += f"Big {str(100.0-jarakpalbs)[0:5]}% "
                            # msgtex += f'Big {cr["pola"]}'
                            datainit["predikbs"] = "Big"
                            bet("Big", "1")
                        else:
                            msgtex += f"Small {str(100.0-jarakpalbs)[0:5]}% "
                            # msgtex += f'Small {cr["pola"]}'
                            datainit["predikbs"] = "Small"
                            bet("Small", "1")
                        print(
                            f'{cr["pola"]} jarak terbaik: {str(100.0-jarakpalbs)[0:5]}% {c("cyan",datainit["predikbs"],0)}'
                        )

                        if cr["predik"]["Odd"] == cr["predik"]["Even"]:
                            msgtex += "⇅"
                            datainit["predikoe"] = ""
                        elif cr["predik"]["Odd"] < cr["predik"]["Even"]:
                            msgtex += f"Odd {str(100.0-jarakpaloe)[0:5]}% "
                            # msgtex += f'Big {cr["pola"]}'
                            datainit["predikoe"] = "Odd"
                            bet("Odd", "1")
                        else:
                            msgtex += f"Even {str(100.0-jarakpaloe)[0:5]}% "
                            # msgtex += f'Small {cr["pola"]}'
                            datainit["predikoe"] = "Even"
                            bet("Even", "1")

                    print(
                        f'{cr["pola"]} jarak terbaik: {str(100.0-jarakpaloe)[0:5]}% {c("cyan",datainit["predikoe"],0)}'
                    )

                    print(f'Pola : {datainit["switch"]}')

                    # print(6)
                    sen(datainit["roomid"], msgtex)
                    # print(7)
            except Exception as e:
                if "game" not in str(e):
                    pass
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
