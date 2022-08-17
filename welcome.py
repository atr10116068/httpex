import requests
import json
import getlive
import seting
import sys,random
import time
import ambil
import random as rdm
import translatepy as trs

# idbaby
# show_id=1174711928&live_id=

# id perusuh baby (pen menang)
# 1006307062
# akun aslinya
# 1220915084

gip = {}
host = "https://wjxwd01mwyo.dt01showxx02.com/"
persi = seting.versi()

konyol = [
    "Istri Tetangga Siap Melayani Anda 24 Jam!",
    "2x Coly Dalam Sebulan Seperti Gaji!!!",
    "uncep sangat cepat, 2 menit sudah sampai rekening",
    "Lottere tiap waktu buka, uncep dan topup",
    "Buaya, Bucin, Pascol Semua Tersedia Di Sini !!!",
    "Atur pacar anda tiap hari dapet cuan",
    "Aku sangat menarik, klik di layar taruhan dan bet",
    "Pilih merah/hijau dan jangan lupakan aku!",
    "suhu game akan panduin gimana cara geterin remot",
]
dbb = {
    "caramel": [
        "5 coin pakai babyoil di dada",
        "5 coin sikut challange",
        "25 coin Remes luar",
        "50 coin Remes dalam"],
    "wa": ["085 163 678 123"],
    "dinda": [
        f"apa kabar n4m",
        f"lama tak jumpa",
        f"rasanya hampir 2 purnama",
        f"rindu didada tak siapa yang tahu",
        f"n4m jgn marah-marah",
        f"takut nanti lekas tua",
        f"kanda setia orangnya",
        f"takkan pernah mendua",
    ],
    "baby": [
        # f"5 coin jilat ketek bang",
        f"20 coin hostnya masukin es batu ke TT",
        # f"guardian 1 minggu (39 coin) nungging+tepuk pantat",
        f"50 coin hostnya masukin es batu ke bawah",
        f"100 coin hostnya buka BH",
    ],
    "hanzo": [
        f"Yang mau mabar ML typing ID",
        f"Kalau banyak yg ikut kita main custom",
        f"Hadiah 10 coin buat team yang menang custom",
        f"Syarat = Follow + juday disini 1 coin",
        f"Whats_app = 085 163 678 123",
    ],
    "sha": [
        f"Welcome yg baru dateng, jgn lupa follow n4m",
        f"Cicil Gift dikit2 yuk, biar dapet nomer WA nya",
        f"n4m mulai jam 18:10 sampai selesai ya guys",
    ],
    "afk": [
        f"Welcome yg baru dateng",
        f"jangan lupa follow n4mnya",
        f"Cicil Gift dikit2 yuk, biar dapet nomer WA nya",
        f"n4m live pagi pagi ya guys",
        # f"20 coin hostnya masukin es batu ke TT",
        # f"50 coin hostnya masukin es batu ke bawah",
        # f"100 coin hostnya buka BH",
        # f"500 coin babynya tidur",
    ],
    "gombal1": [
        f"Halo...",
        f"n4m biasanya di panggil apa?",
        f"ku panggil ani aja ya",
        f"anitime i always think of you",
    ],
    "gombal2": [
        f"tadi ada yang namanya aldo gak?",
        f"yang nama akunnya ALDO",
        f"ALDO any thing for you",
    ],
    "gombal3": [f"kamu orang mana?", f"aku jawa", f"jawa-ban atas doamu selama ini", ],
    "gombal4": [
        f"bantar ya, aku mau ganti nama dlu",
        f"nama riski udah dipake orang, ga bisa nama yg sama",
        f"padahal mau jadi riski biar kamu ga bisa nolak aku",
        f"kan klo riski itu ga boleh di tolak :v",
    ],
    "gombal5": [
        f"bantar ya, aku mau ganti nama dlu",
        f"nama dilan juga udah dipake orang",
        f"kan aku lagi dilanda cintamu :3",
    ],
    "ketawa": [
        f"nulis wkwkwk nya tanpa ketawa ya?",
        f"jgn2 nulis i love you juga tanpa perasaan",
    ],
    "mole": ["47578202"],

}


def getguard(id, tok):
    uri = "https://wjxwd01mwyo.dt01showxx02.com/App/Guard/Buy"
    headers = {
        "user-agent": f"HS-Android Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.17{random.randint(1000,9999)}.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.{random.randint(1000,9999)}.82 Mobile Safari/537.36",
        "bundleidentifier": "user",
        "x-token": tok,
        "accept-encoding": "identity",
        "x-version": persi,
        "host": "wjxwd01mwyo.dt01showxx02.com",
        "connection": "keep-alive",
    }
    para = {"guard_id": "1", "live_id": id}

    req = requests.post(uri, params=para, headers=headers)
    ress = json.loads(req.text)
    return ress


def getmsg(tok):
    uri = "https://wjxwd01mwyo.dt01showxx02.com/App/BusinessCard/List?page=1"
    headers = {
        "user-agent": f"HS-Android Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.17{random.randint(1000,9999)}.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.{random.randint(1000,9999)}.82 Mobile Safari/537.36",
        "bundleidentifier": "user",
        "x-token": tok,
        "accept-encoding": "identity",
        "x-version": persi,
        "host": "wjxwd01mwyo.dt01showxx02.com",
        "connection": "keep-alive",
    }
    para = {}

    req = requests.get(uri, params=para, headers=headers)
    ress = json.loads(req.text)
    return ress


def bacaivc(tok, showid):
    uri = f"https://wjxwd01mwyo.dt01showxx02.com/App/BusinessCard/ContentList?show_id={showid}&page=1"
    headers = {
        "user-agent": f"HS-Android Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.17{random.randint(1000,9999)}.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.{random.randint(1000,9999)}.82 Mobile Safari/537.36",
        "bundleidentifier": "user",
        "x-token": tok,
        "accept-encoding": "identity",
        "x-version": persi,
        "host": "wjxwd01mwyo.dt01showxx02.com",
        "connection": "keep-alive",
    }
    para = {}

    req = requests.get(uri, params=para, headers=headers)
    ress = json.loads(req.text)
    ress = json.dumps(ress["result"], indent=2)
    return ress


def getidol(id, tok):
    uri = "https://wjxwd01mwyo.dt01showxx02.com/App/BusinessCard/UserGet"
    headers = {
        "user-agent": f"HS-Android Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.17{random.randint(1000,9999)}.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.{random.randint(1000,9999)}.82 Mobile Safari/537.36",
        "bundleidentifier": "user",
        "x-token": tok,
        "accept-encoding": "identity",
        "x-version": persi,
        "host": "wjxwd01mwyo.dt01showxx02.com",
        "connection": "keep-alive",
    }
    para = {"live_id": id}

    req = requests.get(uri, params=para, headers=headers)
    ress = json.loads(req.text)
    return ress


def nama(x):
    uriweb = host + "App/User_User/Info"
    headers = {
        "user-agent": f"HS-Android Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.17{random.randint(1000,9999)}.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.{random.randint(1000,9999)}.82 Mobile Safari/537.36",
        "bundleidentifier": "user",
        "x-token": x,
        "accept-encoding": "identity",
        "x-version": persi,
        "connection": "keep-alive",
    }
    f = requests.get(uriweb, headers=headers)
    ress = json.loads(f.text)
    try:
        print("Nickname: " + ress["result"]["nickname"])
        return 1
    except:
        print("Token Expiret")
        return 0


def sen(id, tok, tex):
    uri = host + "App/Live/SendMsg"
    headers = {
        "user-agent": f"HS-Android Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.17{random.randint(1000,9999)}.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.{random.randint(1000,9999)}.82 Mobile Safari/537.36",
        "bundleidentifier": "user",
        "x-token": tok,
        "accept-encoding": "identity",
        "x-version": persi,
        "connection": "keep-alive",
    }
    para = {"live_id": id, "content": tex}

    req = requests.get(uri, params=para, headers=headers)
    ress = json.loads(req.text)
    return ress


def main(ttt):
    room = getlive.roomall()
    x = 1
    for i in room:
        print("{}. {}".format(str(x), i["nickname"]))
        x += 1

    inp = input("room nomor : ")
    idroom = room[int(inp) - 1]["live_id"]
    print("\nTarget Room : " + room[int(inp) - 1]["nickname"])

    tokenawal = ambil.token()
    idxakun = 0
    if "loop" in ttt:
        satu, dua = int(ttt.split(" ")[1]), int(ttt.split(" ")[2])
        idxakun = satu
    gantiketek = 0
    while True:
        if "loop" in ttt:
            if gantiketek == 0:
                gantiketek = 1
                if idxakun == dua:
                    idxakun = satu
                else:
                    idxakun += 1
                token = tokenawal[idxakun]
            else:
                gantiketek = 0
                if idxakun == dua:
                    idxakun = satu
                else:
                    idxakun += 1
                token = tokenawal[idxakun]
        else:
            token = tokenawal[int(ttt) - 1]
        print()
        nama(token)
        inpt = input(" : ")
        if inpt == "q":
            break
        elif inpt == "help":
            t = """>> All Commnad
-q
-tr
-trlist
-list
-sp
-db [db]
-konyol
-ivc
-ivclist
-guard
-blank
-loop [count] [text]
-loop [db] [durasi]
-kntl
-crot
"""
            print(t)
        elif inpt == "trlist":
            trs.trlist()
        elif inpt == "list":
            for t in dbb:
                print(t)
        elif inpt == "kntl":
            sen(idroom, token, "𓂸")
        elif inpt == "crot":
            sen(idroom, token, "𓂺")
        elif inpt == "blank":
            blng = """ᅠ
ᅠ
ᅠ
ᅠ
ᅠ
ᅠ
ᅠ
ᅠ
ᅠ
ᅠ
ᅠ
ᅠ
ᅠ
ᅠ
ᅠ
ᅠ
ᅠ
ᅠ
ᅠ
ᅠ
ᅠ
ᅠ
ᅠ
ᅠ
ᅠ
"""
            sen(idroom, token, blng)
        elif inpt == "sp":
            while True:
                namviw = input("nick : ")
                if namviw == "q":
                    break
                nam = room[int(inp) - 1]["nickname"]

                if "INDO" in nam:
                    nam = nam.replace("INDO : ", "")
                if "MALAY" in nam:
                    nam = nam.replace("MALAY : ", "")

                tek = [
                    f"Welcome {namviw} 😁, jgn pindah dulu ya",
                    f"Support hostnya yuk, bantu gift {nam} ♥️",
                    f"Jgn lupa gamenya dimainin ya {namviw} 😘",
                ]

                for idop in tek:
                    sen(idroom, token, idop)
                    time.sleep(0.1)
        elif inpt.startswith("tr"):
            dess = inpt.split(" ")[1]
            tex = inpt.split(" ")
            tex.pop(0)
            tex.pop(0)
            text = ""
            for p in tex:
                text += p+" "
            translet = trs.tpy(text, dess)
            sen(idroom, token, translet[1])
        elif inpt.startswith("db "):
            nam = room[int(inp) - 1]["nickname"]
            namalagu = inpt.replace("db ", "")

            if "INDO" in nam:
                nam = nam.replace("INDO : ", "")
            if "MALAY" in nam:
                nam = nam.replace("MALAY : ", "")

            for x in dbb[namalagu]:
                if "n4m" in x:
                    x = x.replace("n4m", nam)
                sen(idroom, token, x)
                for t in range(7, 1, -1):
                    sys.stdout.write(f"{t}  \r")
                    sys.stdout.flush()
                    time.sleep(1)
        elif inpt == "konyol":
            nam = room[int(inp) - 1]["nickname"]
            for x in range(len(konyol)):
                sen(idroom, token, konyol[x])
                if x == 0:
                    pass
                    # time.sleep(8)
                time.sleep(20)
        elif inpt == "ivc":
            print(getidol(idroom, token))
        elif inpt == "ivclist":
            data = getmsg(token)["result"]["list"]
            i = 0
            for t in data:
                print(f'{i}. {t["nickname"]}')
                i += 1

            ygmana = input("ivc nomor: ")
            kontk = bacaivc(token, data[int(ygmana)]["show_id"])
            print(kontk)

        elif inpt == "guard":
            print(getguard(idroom, token))
        elif inpt.startswith("count "):
            inpt = inpt.replace("count ", "")
            for titr in range(int(inpt),0,-1):
                if titr %10==0:
                    sen(idroom, token, f"{titr} detik lagi")
                time.sleep(1)
        elif inpt.startswith("loop "):
            inpt = inpt.replace("loop ", "")
            dbbs = inpt.split(" ")[0]
            itr = inpt.split(" ")[1]

            nam = room[int(inp) - 1]["nickname"]

            if "INDO" in nam:
                nam = nam.replace("INDO : ", "")
            if "MALAY" in nam:
                nam = nam.replace("MALAY : ", "")

            while True:
                try:
                    for tex in dbb[dbbs]:
                        if "n4m" in tex:
                            tex = tex.replace("n4m", nam)
                        sen(idroom, token, tex)
                        time.sleep(8)
                    for i in range(int(itr)):
                        sys.stdout.write(f"{i} \r")
                        sys.stdout.flush()
                        time.sleep(1)
                except:
                    itr = inpt.split(" ")[0]
                    tex = ""
                    texa = inpt.split(" ")
                    texa.pop(0)
                    for p in texa:
                        tex += f"{p} "

                    for itre in range(int(itr)):
                        sen(idroom, token, tex)
                        sys.stdout.write(f">>>>>>>>>>>>>>>>>> {itre}/{itr} \r")
                        for i in range(8, 0, -1):
                            sys.stdout.write(f"{i} \r")
                            sys.stdout.flush()
                            time.sleep(1)
                    break
        else:
            sen(idroom, token, inpt)

    print("selesai...")


tehj = input("Token no (loop n-n juga bisa):")
print(tehj)
while True:
    main(tehj)
