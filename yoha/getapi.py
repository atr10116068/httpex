import random as rdm
import json
import ambil
import httpx

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


import pyrebase
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


with open("data.json") as json_file:
    data = json.load(json_file)["results"]


head = {
    "host": "api.yoha.pro",
    "content-type": "application/json; charset=utf-8",
    "user-agent": f"Mozilla/5.0 (iPhone13,2; U; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/602.{rdm.randint(0,255)}.{rdm.randint(0,255)} (KHTML, like Gecko) Version/10.0 Mobile/{rdm.randint(11,99)}E{rdm.randint(111,999)} Safari/602.1"
}
head["authorization"] = rdm.choice(ambil.token())
uri = f'{data["host"]}api/options/index?v=2.0.8&ip=180.{rdm.randint(1,255)}.{rdm.randint(1,255)}.{rdm.randint(1,255)}&l=in'
r = httpx.get(uri, headers=head)
if r.status_code == 200:
    ress = (json.loads(r.text))
    persi = ress["data"]["apk_ver"]
    print(f"\tCurrent Version [{persi}]")
else:
    print("GAGAL DETECT VERSI")
    exit()


def profile(token):
    head["authorization"] = token
    uri = f'{data["host"]}api/auth/me?v={persi}&ip=180.{rdm.randint(1,255)}.{rdm.randint(1,255)}.{rdm.randint(1,255)}&l=in'
    r = httpx.get(uri, headers=head)
    if r.status_code == 200:
        ress = (json.loads(r.text))
        for akun in ress["data"]:
            cek = ress['data'][akun]
            return ress
        else:
            print(f"gagal : {ress['message']}")
            return 0


def claim(token, days):
    head["authorization"] = token
    aipi = f'180.{rdm.randint(1,255)}.{rdm.randint(1,255)}.{rdm.randint(1,255)}'
    param1 = {
        "v": persi,
        "ip": aipi,
        "l": "in"
    }
    # entry
    uri = f'{data["host"]}api/activity/entry?v={persi}&v={persi}&ip=180.{rdm.randint(1,255)}.{rdm.randint(1,255)}.{aipi}&l=in'
    r = httpx.get(uri, headers=head)
    if r.status_code == 200:
        ress = (json.loads(r.text))
        print(f"Entry : {ress['status']}")
    # registerActv
    uri = f'{data["host"]}api/registerActivity/receiveAward?v={persi}&v={persi}&ip=180.{rdm.randint(1,255)}.{rdm.randint(1,255)}.{aipi}&l=in'
    r = httpx.post(uri, params=param1, headers=head)
    if r.status_code == 200:
        ress = (json.loads(r.text))
        print(f"Receive : {ress['status']}")
    # Auth
    uri = f'{data["host"]}api/auth/me?v={persi}&v={persi}&ip=180.{rdm.randint(1,255)}.{rdm.randint(1,255)}.{aipi}&l=in'
    r = httpx.get(uri, headers=head)
    if r.status_code == 200:
        ress = (json.loads(r.text))
        if ress['status'] != "error":
            print(
                f"Auth : [{ress['data']['coin']}]\t\t{ress['data']['user_nicename']}")
    # claim
    uri = f'{data["host"]}api/signs/store?day={days}&sign_id={days}&v={persi}&v={persi}&ip=180.{rdm.randint(1,255)}.{rdm.randint(1,255)}.{aipi}&l=in'
    r = httpx.post(uri, headers=head)
    if r.status_code == 200:
        ress = (json.loads(r.text))
        if ress["status"]=="success":
            msg=c('green',ress['data']['amount'],0)
            print(f"Claim : {msg}")
        else:
            msg=f"{c('red',ress['status'],0)} {ress['message']}"
            print(f"Claim : {msg}")
    return ress


def randcode():
    avail = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "1", "2", "3", "4", "5", "6", "7",
             "8", "9", "0", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m"]
    tex = ""
    for t in range(34):
        tex += rdm.choice(avail)
    return tex


def sendcode(nomer):
    head["accept"] = "application/json"
    head["accept-encoding"] = "gzip"
    param = {
        "mobile": nomer,
        "tag": "register",
        "v": persi,
        "ip": f'180.252.{rdm.randint(1,255)}.{rdm.randint(1,255)}',
        "l": "in",
    }
    uri = f'{data["host"]}api/sms/verify-code'
    r = httpx.post(uri, params=param, headers=head)
    if r.status_code == 200:
        ress = json.loads(r.text)
        try:
            return ress
        except:
            print(f'gagal : {r.text}')
    else:
        print(f"gagal status code : {r.text}")


def register(nomer, password, code):
    head["accept"] = "application/json"
    head["accept-encoding"] = "gzip"
    param = {
        "user_login": nomer,
        "user_pass": password,
        "user_pass2": password,
        "source": "android",
        "referral_code": "INoQDdUI2W4TZZDd",
        "channel_code": "2",
        "unique_code": f"{rdm.randint(100000,999999)}7{rdm.randint(100000,999999)}-{rdm.randint(100000,999999)}0{rdm.randint(100000,999999)}{rdm.randint(100000,999999)}",
        "code": code,
        "pasteboard": "",
        "device_code": randcode(),
        "guest_code": "",
        "v": persi,
        "ip": f'180.252.{rdm.randint(1,255)}.{rdm.randint(1,255)}',
        "l": "in",
    }
    uri = f'{data["host"]}api/auth/register'
    r = httpx.post(uri, params=param, headers=head, timeout=10)
    if r.status_code == 200:
    # if True:
        ress = json.loads(r.text)
        # ress=""
        try:
            dbb = {"results": []}
            req = db.child('yoha').child('akun').child("results").get()
            acc = req.val()
            idxkosong=0
            adakosong=[]
            for tott in acc:
                dbb["results"].append(tott)
                if tott["no"]=="kosong":
                    adakosong.append(idxkosong)
                idxkosong+=1
            if len(adakosong)==0:
                dbb["results"].append({"no": nomer, "pass": password})
                db.child("yoha").child("akun").update(dbb)
                print("data baru")
            else:
                db.child("yoha").child("akun").child("results").child(int(adakosong[0])).update({"no": nomer, "pass": password})
                print(f"ada kosong di urutan {adakosong[0]}")
            return ress
        except:
            print(f'gagal : {r.text}')
    else:
        print(f"gagal status code : {r.text}")

def getroom(token):
    head["authorization"] = token
    head["host"] = "tech04.yoha.pro"
    aipi = f'180.{rdm.randint(1,255)}.{rdm.randint(1,255)}.{rdm.randint(1,255)}'
    param1 = {
        "v": persi,
        "ip": aipi,
        "l": "in"
    }
    uri = f'{data["api"]}live/list?type=0&page=1&per_page=100&last_ids=&v={persi}&ip=180.252.129.{rdm.randint(1,255)}&l=in'
    try:
        r = httpx.post(uri, params=param1, headers=head, timeout=5)
        if r.status_code == 200:
            ressx = (json.loads(r.text))
            ress = []
            for dtr in ressx["data"]["list"]:
                vuid = dtr["uid"]
                if vuid not in ress:
                    ress.append(dtr)
            return ress
        print(f"{r.text}")
    except Exception as error:
        print(error)
    return 0


def send(token, streamid, tex):
    head["authorization"] = token
    head["host"] = "tech04.yoha.pro"
    aipi = f'180.{rdm.randint(1,255)}.{rdm.randint(1,255)}.{rdm.randint(1,255)}'
    param1 = {
        "stream": streamid,
        "content": tex,
        "v": persi,
        "ip": aipi,
        "l": "in"
    }
    uri = f'{data["api"]}live/sendMsg'
    try:
        r = httpx.post(uri, data=json.dumps(param1), headers=head, timeout=5)
        if r.status_code == 200:
            ressx = (json.loads(r.text))
            return ressx
        print(f"{r.text}")
    except Exception as error:
        print(error)
    return 0


def getgift(token):
    head["authorization"] = token
    head["host"] = "tech04.yoha.pro"
    param1 = {
    }
    uri = f'{data["api"]}live/getGiftList'
    try:
        r = httpx.post(uri, data=json.dumps(param1), headers=head, timeout=5)
        if r.status_code == 200:
            ressx = (json.loads(r.text))
            return ressx
        print(f"{r.text}")
    except Exception as error:
        print(error)
    return 0


def gift(token, stream, idgift, liveuid, num):
    head["authorization"] = token
    head["host"] = "tech04.yoha.pro"
    aipi = f'180.{rdm.randint(1,255)}.{rdm.randint(1,255)}.{rdm.randint(1,255)}'
    param1 = {
        "stream": stream,
        "num": num,
        "live_uid": liveuid,
        "gift_id": idgift,
        "combo": "true",
        "type": "0",
        "v": persi,
        "ip": aipi,
        "l": "in"
    }
    uri = f'{data["api"]}live/sendGift'
    try:
        r = httpx.post(uri, data=json.dumps(param1), headers=head, timeout=5)
        if r.status_code == 200:
            ressx = (json.loads(r.text))
            return ressx
        print(f"{r.text}")
    except Exception as error:
        print(error)
    return 0


def login(no, passw):
    head["accept"] = "application/json"
    head["accept-encoding"] = "gzip"
    param = {
        "user_login": no,
        "user_pass": passw,
        "user_email": "",
        "source": "",
        "v": persi,
        "ip": f'180.252.129.{rdm.randint(1,255)}',
        "l": "in",
    }
    uri = f'{data["host"]}api/auth/login'
    r = httpx.post(uri, params=param, headers=head)
    if r.status_code == 200:
        ress = json.loads(r.text)
        # print(f'\t\tCode : {ress["code"]}')
        if ress["code"]==500:#Akun atau kata sandi salah
            return 500
        else:
            try:
                token = f'Bearer {ress["data"]["access_token"]}'
                return token
            except:
                print(f'gagal : {r.text} {no}')
            return 0
    else:
        print(f"gagal status code : {r.text}")
        return 0
