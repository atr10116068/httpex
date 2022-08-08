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
import pytz
import datetime
import translatepy as trs

dat = {
    "admin": [
        "1119943580",
        "1696182045",
        "1665699504",
        "1037219061",
    ],
    "minimumlvl": 7
}
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
token = tokk[20]
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


x = 1
for i in room:
    print("{}. {}".format(str(x), i["nickname"]))
    x += 1

inp = input("room nomor : ")
idroom = room[int(inp)-1]["live_id"]
print("\nTarget Room : "+room[int(inp)-1]["nickname"])

datan = b"ping"
uriweb = "wss://dt001wsgew.qrdnk.cn/?token="+token

param = {
    "upgrade": "websocket",
    "connection": "Upgrade",
    "Accept-Encoding": "gzip",
    "host": "yoogs01wltb.dt01showxx03.com",
    "user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.171019.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36",
}


def sen(id, tok, tex):
    uri = "https://wjxwd01mwyo.dt01showxx02.com/App/Live/SendMsg"
    headers = {
        "user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.171019.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36",
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


def trans(udata):
    try:
        udata["utex"] = udata["utex"].replace("tr ", "")
        desx = udata["utex"].split(" ")[0]
        se0 = udata["utex"].split(" ")
        del se0[0]
        texxx = ""
        for tp in se0:
            texxx += f'{tp} '

        # print(f"texx : {texx}")
        # print(f"desx : {desx}")
        # print(f"texxx : {texxx}")
        hasi = trs.tpy(texxx, desx)
        # <<<< ['入力しようとしています', 'Nyūryoku shiyou to shite imasu'] >>>>>>
        sen(idroom, token, hasi[1])
    except Exception as e:
        print(f"Error : {e}")


def carihost(udata):
    try:
        udata["utex"] = udata["utex"].replace("cari ", "")
        print(udata)
        hostny = udata["utex"]
        rekhost = carihos(hostny)

        # print(f"texx : {texx}")
        # print(f"desx : {desx}")
        # print(f"texxx : {texxx}")
        if rekhost["status"] == True:
            sen(idroom, token, f"Sekarang dia lagi on")
            sen(idroom, token, f"Durasinya {rekhost['durasi']}")
            sen(idroom, token, f"Terahir live {rekhost['last_time']}")
        elif rekhost["status"] == False:
            print(rekhost)
            sen(idroom, token, f"sekarang dia lagi off")
            sen(idroom, token, f"Terahir live {rekhost['last_time']}")
        else:
            sen(idroom, token, f"Acil bingung...")
            sen(idroom, token, "masuk")
    except Exception as e:
        print(f"Error : {e}")


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


def cariviwer(udata):
    udata["utex"] = udata["utex"].replace("cariakun ", "")
    viwerny = udata["utex"]
    roomxx = getlive.roomall()
    nemu = False
    for iii in roomxx:
        idroomss = iii["live_id"]
        namaroom = iii["nickname"]
        try:
            datas = gas2(idroomss, tokenhost)
            for pp in datas:
                nama = pp["nickname"]
                if nama == viwerny:
                    nemu = {0: nama, 1: namaroom}
        except:
            print("Gagal Capture Data")
    if nemu != False:
        sen(idroom, token, f"{nemu[0]} di {nemu[1]}")
    else:
        sen(idroom, token, f"Ga nemu bang")


def clvl(udata):
    try:
        udata["utex"] = udata["utex"].replace("changelvl ", "")
        dat["minimumlvl"] = int(udata["utex"])
        sen(idroom, token, f"Sudah di sett ke {udata['utex']}")
    except Exception as e:
        print(f"Error : {e}")


gid = []
imb = ["karena", "ketika", "saat", "dan", "melihat", "mendengar"]
game = {}


def lagi():
    import _thread as thread

    def on_message(ws, message):
        datadadu = json.loads(message)
        try:
            if datadadu[0]["action"] == "connected":
                print(f'\t\t{datadadu[0]["data"]["msg_body"]["client_id"]}')
                uriweb = "https://wjxwd01mwyo.dt01showxx02.com/App/LiveEnter/JoinGroup"
                headers = {
                    "User-Agent": "HS-Android Mozilla/5.0 (Linux; Android 8.1.0; Pixel C Build/OPM1.171019.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36",
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

                if udata['utex'].lower() in ["cil", "acil"]:
                    bawel = [
                        "apa sih... bawel",
                        "apaan?",
                        "oiiiii",
                        "kenapa?",
                        "gw disini...",
                        "ada apa?...",
                    ]
                    tex = random.choice(bawel)
                    sen(idroom, token, tex)
                try:
                    if utex.startswith("."):
                        texx = utex.replace(".", "")
                        udata["utex"] = texx
                        if udata['utex'] == "reset":
                            if udata["uid"] in dat["admin"]:
                                game.clear()
                                gid.clear()
                            else:
                                tex = "Hanya adminku yang boleh"
                                sen(idroom, token, tex)
                        if udata['utex'] == "cek":
                            tex = f"{len(gid)} akun ikutan"
                            sen(idroom, token, tex)
                        if udata['utex'] == "main":
                            if udata["uid"] in dat["admin"]:
                                for tex in ["ketik .add [nama]-[kerja]-[nama]-[kerja]", 'contoh .add budi-terkejut-alex-uncep']:
                                    sen(idroom, token, tex)

                        elif udata['utex'] == "acak":
                            if udata["uid"] in dat["admin"]:
                                print(gid)
                                print(game)
                                disp = f"{game[random.choice(gid)][0]} {game[random.choice(gid)][1]} {random.choice(imb)} {game[random.choice(gid)][2]} {game[random.choice(gid)][3]}"
                                sen(idroom, token, disp)
                            else:
                                tex = "Hanya adminku yang boleh"
                                sen(idroom, token, tex)

                        elif udata['utex'].startswith("add "):
                            dgame = texx.replace("add ", "")
                            dgames = dgame.split("-")
                            if len(dgames) == 4:
                                game[udata["uid"]] = dgames
                                if udata["uid"] not in gid:
                                    gid.append(udata["uid"])
                                tex = "Sudah ditambah"
                                sen(idroom, token, tex)
                            else:
                                tex = "contoh nama-ekspresi-nama-ekspresi"
                                sen(idroom, token, tex)
                                tex = "contoh budi-terkejut-rudi-tertawa"
                                sen(idroom, token, tex)
                except Exception as e:
                    print(e)

                if utex.startswith("cil "):
                    texx = utex.replace("cil ", "")
                    udata["utex"] = texx
                    try:
                        if lepel[udata["ulvl"]] >= dat["minimumlvl"] or udata["uid"] in dat["admin"]:
                            if udata['utex'].startswith("tr "):
                                trans(udata)
                            elif udata['utex'].startswith("cariakun "):
                                cariviwer(udata)
                            elif udata['utex'].startswith("cari "):
                                carihost(udata)
                            elif udata['utex'].startswith("changelvl "):
                                if udata["uid"] in dat["admin"]:
                                    clvl(udata)
                                else:
                                    tex = "Hanya adminku yang boleh"
                                    sen(idroom, token, tex)

                            if udata['utex'] == "siapa aku?":
                                if udata["uid"] in dat["admin"]:
                                    tex = "kamu itu adminku"
                                    sen(idroom, token, tex)
                                else:
                                    tex = "kamu viwer biasa"
                                    sen(idroom, token, tex)
                            elif udata['utex'] == "bisa apa aja?":
                                texs = [
                                    "Cek Admin : cil siapa aku?",
                                    "Jam live host  : cil cari [namahost]",
                                    "Letak viwer   : cil cariakun [nama]",
                                    "Terjemahkan bahasa : cil tr [bahasa] [text]",
                                    "ex = cil cari INDO : Bebyj",
                                    "ex = cil cari New Xnxx",
                                    "ex = cil tr en pagi",
                                ]
                                for tex in texs:
                                    sen(idroom, token, tex)
                                    time.sleep(2)
                        else:
                            tex = f"Hanya dapat di gunakan oleh LVL {str(dat['minimumlvl'])} keatas"
                            sen(idroom, token, tex)
                    except Exception as e:
                        print(f"Error : {e}")

                print(
                    f" > [{udata['uid']}][{lepel[udata['ulvl']]}] {udata['uname']}\t: {udata['utex']}")
            # print(datadadu)
        except:
            pass

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