
import time
import sys
import pytz
import pyrebase
from datetime import datetime

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


def getjam():
    now = datetime.now(pytz.timezone("Asia/Jakarta"))
    pj0 = now.strftime("%H")
    pj1 = now.strftime("%M")
    pj2 = now.strftime("%S")
    return [pj0, pj1, pj2]


def gethostnow():
    import getlive
    room = getlive.roomall()
    return room


def adadidb(nm):
    try:
        if not db.child('host').child(nm).shallow().get().val():
            # print("users does not exist")
            return 0
        else:
            # print("users exist")
            return 1
    except Exception as e:
        print(e)
        return 0


# kkk = "["
# for t in range(48, 57):
#     kkk += f"{t},"
# kkk += "]"
# print(kkk)
# exit()


def proses():
    # print("---------------------------[ BACKUP ID & NAME HOST LIVE ]--")
    try:
        dthostbaru = gethostnow()
    except:
        print("Lost Koneksi")

    tz = pytz.timezone("Asia/Jakarta")
    now = datetime.now(tz)
    datenow = now.strftime("%d-%b-%Y %H:%M:%S")
    for idd in range(len(dthostbaru)):
        sys.stdout.write(f"{idd} \r")
        sys.stdout.flush()
        dt = dthostbaru[idd]
        # hurufkcl
        aaa = [33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44,
               46, 47, 59, 60, 61, 62, 63, 91, 93, 123, 125]

        namanya = dt["nickname"]
        dt["nickname"] = ""
        for tt in namanya:
            cchar = ord(tt)
            if cchar not in aaa:
                dt["nickname"] += tt
            else:
                dt["nickname"] += "-"

        # print(dt["nickname"])
        sys.stdout.write(f"\t{idd}\r")
        sys.stdout.flush()
        # nama ada di json
        if adadidb(dt["nickname"]) == 1:
            jk = getjam()
            dt["jamlive"] = f"{jk[0]}:{jk[1]}:{jk[2]}"
            dt["is_live"] = 1
            # print(dt["jamlive"])
            # jika live id sekarang != live id di db
            if dt["live_id"] != db.child('host').child(dt["nickname"]).child("live_id").get().val():
                print(f'{datenow}\tHost Lama Live >> {dt["nickname"]}')
                jk = getjam()
                jam = f"{jk[0]}:{jk[1]}:{jk[2]}"
                db.child("host").child(dt["nickname"]).update(
                    {"jamlive": jam, "is_live": 1, "live_id": dt["live_id"]})
        else:
            jk = getjam()
            dt["jamlive"] = f"{jk[0]}:{jk[1]}:{jk[2]}"
            dt["is_live"] = 1
            db.child("host").child(dt["nickname"]).update(dt)
            print(
                f'{datenow}\tHost Baru Live >> {dt["live_id"]}:{dt["nickname"]}')

    #print(f"\n___________> {len(dthostbaru)} Host yg live")
    namahostbaru = []
    iq = 0
    for t in dthostbaru:
        namahostbaru.append(t["nickname"])
        iq += 1
        # print(f'{iq}. {t["nickname"]}')

    # offkan host
    xcx = db.child('host').get()
    for t in xcx:
        nama = t.val()["nickname"]
        if nama not in namahostbaru:
            if t.val()["is_live"] == 1:
                db.child("host").child(nama).update({"is_live": 0})
                db.child("host").child(nama).update({"last_live": datenow})
                print(f"{datenow}\tDi offkan {nama}")


proses()
while True:
    try:
        pj = getjam()
        sys.stdout.write(f"\t{pj[0]}:{pj[1]}:{pj[2]} \r")
        sys.stdout.flush()
        jam, menit, detik = pj[0], pj[1], pj[2]
        if detik == "00":
            if int(menit) % 2 == 0:
                proses()
        time.sleep(1)
    except Exception as e:
        print(str(e))
        for t in range(10):
            time.sleep(1)
