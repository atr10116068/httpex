import pyrebase
import random as rdm
import json
import ambil
import fakebio
import httpx
import webbrowser

from colorama import Fore, Style, init
init()


def oweb(url):
    webbrowser.register('chrome',
                        None,
                        webbrowser.BackgroundBrowser("C:\\Users\\User\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe"))
    webbrowser.get('chrome').open_new(url)


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
    "accept": "application/json",
    "content-type": "application/json; charset=utf-8",
    "user-agent": f"Mozilla/5.0 (iPhone11,2; U; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/602.{rdm.randint(0,255)}.{rdm.randint(0,255)} (KHTML, like Gecko) Version/9.0 Mobile/{rdm.randint(11,99)}E{rdm.randint(111,999)} Safari/602.1"
}
head["authorization"] = rdm.choice(ambil.token())
aipi = f'{rdm.randint(1,255)}.{rdm.randint(1,255)}.{rdm.randint(1,255)}.{rdm.randint(1,255)}'
uri = f'{data["host"]}api/options/index?v=2.0.8&ip={aipi}&l=in'
r = httpx.get(uri, headers=head)
if r.status_code == 200:
    ress = (json.loads(r.text))
    persi = ress["data"]["apk_ver"]
    print(f"\tCurrent Version [{persi}]")
else:
    print("GAGAL DETECT VERSI")
    exit()


def profile(token):
    head = {
        "authorization": token,
        "host": "api.yoha.pro",
        "accept": "application/json",
        "content-type": "application/json; charset=utf-8",
        "user-agent": f"Mozilla/5.0 (iPhone11,2; U; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/602.{rdm.randint(0,255)}.{rdm.randint(0,255)} (KHTML, like Gecko) Version/9.0 Mobile/{rdm.randint(11,99)}E{rdm.randint(111,999)} Safari/602.1"
    }
    aipi = f'{rdm.randint(1,255)}.{rdm.randint(1,255)}.{rdm.randint(1,255)}.{rdm.randint(1,255)}'
    uri = f'{data["host"]}api/auth/me?v={persi}&ip={aipi}&l=in'
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
    head = {
        "authorization": token,
        "host": "api.yoha.pro",
        "accept": "application/json",
        "content-type": "application/json; charset=utf-8",
        "user-agent": f"Mozilla/5.0 (iPhone11,2; U; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/602.{rdm.randint(0,255)}.{rdm.randint(0,255)} (KHTML, like Gecko) Version/9.0 Mobile/{rdm.randint(11,99)}E{rdm.randint(111,999)} Safari/602.1"
    }
    aipi = f'{rdm.randint(1,255)}.{rdm.randint(1,255)}.{rdm.randint(1,255)}.{rdm.randint(1,255)}'
    param1 = {
        "v": persi,
        "ip": aipi,
        "l": "in"
    }
    # entry
    uri = f'{data["host"]}api/activity/entry?v={persi}&ip={aipi}&l=in'
    r = httpx.get(uri, headers=head)
    if r.status_code == 200:
        ress = (json.loads(r.text))
        print(f"Entry : {ress['status']}")
    # registerActv
    uri = f'{data["host"]}api/registerActivity/receiveAward?v={persi}&ip={aipi}&l=in'
    r = httpx.post(uri, params=param1, headers=head)
    if r.status_code == 200:
        ress = (json.loads(r.text))
        print(f"Receive : {ress['status']}")
    # Auth
    uri = f'{data["host"]}api/auth/me?v={persi}&ip={aipi}&l=in'
    r = httpx.get(uri, headers=head)
    if r.status_code == 200:
        ress = (json.loads(r.text))
        if ress['status'] != "error":
            print(
                f"Auth : [{ress['data']['coin']}]\t\t{ress['data']['user_nicename']}")
    # claim
    uri = f'{data["host"]}api/signs/store?day={days}&sign_id={days}&v={persi}&v={persi}&ip={aipi}&l=in'
    r = httpx.post(uri, headers=head)
    if r.status_code == 200:
        ress = (json.loads(r.text))
        if ress["status"] == "success":
            msg = c('green', ress['data']['amount'], 0)
            print(f"Claim : {msg}")
        else:
            msg = f"{c('red',ress['status'],0)} {ress['message']}"
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
    aipi = f'{rdm.randint(1,255)}.{rdm.randint(1,255)}.{rdm.randint(1,255)}.{rdm.randint(1,255)}'
    head = {
        "host": "api.yoha.pro",
        "accept": "application/json",
        "content-type": "application/json; charset=utf-8",
        "user-agent": f"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.{rdm.randint(100000,999999)}.{rdm.randint(100,999)}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0 Mobile Safari/537.36"
    }
    param = {
        "mobile": nomer,
        "tag": "register",
        "v": persi,
        "ip": aipi,
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
    aipi = f'{rdm.randint(1,255)}.{rdm.randint(1,255)}.{rdm.randint(1,255)}.{rdm.randint(1,255)}'
    head = {
        "host": "api.yoha.pro",
        "accept": "application/json",
        "content-type": "application/json; charset=utf-8",
        "user-agent": f"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.{rdm.randint(100000,999999)}.{rdm.randint(100,999)}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0 Mobile Safari/537.36"
    }
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
        "ip": aipi,
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
            idxkosong = 0
            adakosong = []
            for tott in acc:
                dbb["results"].append(tott)
                if tott["no"] == "kosong":
                    adakosong.append(idxkosong)
                idxkosong += 1
            if len(adakosong) == 0:
                dbb["results"].append({"no": nomer, "pass": password})
                db.child("yoha").child("akun").update(dbb)
                print("data baru")
            else:
                db.child("yoha").child("akun").child("results").child(
                    int(adakosong[0])).update({"no": nomer, "pass": password})
                print(f"ada kosong di urutan {adakosong[0]}")
            return ress
        except:
            print(f'gagal : {r.text}')
    else:
        print(f"gagal status code : {r.text}")


def registernodb(nomer, password, code):
    aipi = f'{rdm.randint(1,255)}.{rdm.randint(1,255)}.{rdm.randint(1,255)}.{rdm.randint(1,255)}'
    head = {
        "host": "api.yoha.pro",
        "accept": "application/json",
        "content-type": "application/json; charset=utf-8",
        "user-agent": f"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.{rdm.randint(100000,999999)}.{rdm.randint(100,999)}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0 Mobile Safari/537.36"
    }
    param = {
        "user_login": nomer,
        "user_pass": password,
        "user_pass2": password,
        "source": "android",
        "referral_code": "5qwVgDlmvk6faexE",
        "channel_code": "2",
        "unique_code": f"{rdm.randint(100000,999999)}7{rdm.randint(100000,999999)}-{rdm.randint(100000,999999)}0{rdm.randint(100000,999999)}{rdm.randint(100000,999999)}",
        "code": code,
        "pasteboard": "",
        "device_code": randcode(),
        "guest_code": "",
        "v": persi,
        "ip": aipi,
        "l": "in",
    }
    uri = f'{data["host"]}api/auth/register'
    r = httpx.post(uri, params=param, headers=head, timeout=10)
    if r.status_code == 200:
        # if True:
        ress = json.loads(r.text)
        # ress=""
        try:
            return ress
        except:
            print(f'gagal : {r.text}')
    else:
        print(f"gagal status code : {r.text}")


def getroom(token):
    head = {
        "authorization": token,
        "host": "tech04.yoha.pro",
        "accept": "application/json",
        "content-type": "application/json; charset=utf-8",
        "user-agent": f"Mozilla/5.0 (iPhone11,2; U; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/602.{rdm.randint(0,255)}.{rdm.randint(0,255)} (KHTML, like Gecko) Version/9.0 Mobile/{rdm.randint(11,99)}E{rdm.randint(111,999)} Safari/602.1"
    }
    aipi = f'{rdm.randint(1,255)}.{rdm.randint(1,255)}.{rdm.randint(1,255)}.{rdm.randint(1,255)}'
    param1 = {
        "v": persi,
        "ip": aipi,
        "l": "in"
    }
    uri = f'{data["api"]}live/list?type=0&page=1&per_page=200&last_ids=&v={persi}&ip={aipi}&l=in'
    try:
        r = httpx.post(uri, params=param1, headers=head, timeout=5)
        if r.status_code == 200:
            ressx = (json.loads(r.text))
            ress = []
            for dtr in ressx["data"]["list"]:
                vuid = dtr["uid"]
                if vuid not in ress and dtr["user_nicename"].lower() not in ["yoha movie", "dj yoha", "yoha game", "yoha lisa", "yoha xix", "yoha lala", "yoha bola", "yoha luxi", "yoha2", "yoha yayqa"]:
                    ress.append(dtr)
            return ress
        print(f"{r.text}")
    except Exception as error:
        print(error)
    return 0


def send(token, streamid, tex):
    head = {
        "authorization": token,
        "host": "tech04.yoha.pro",
        "accept": "application/json",
        "content-type": "application/json; charset=utf-8",
        "user-agent": f"Mozilla/5.0 (iPhone11,2; U; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/602.{rdm.randint(0,255)}.{rdm.randint(0,255)} (KHTML, like Gecko) Version/9.0 Mobile/{rdm.randint(11,99)}E{rdm.randint(111,999)} Safari/602.1"
    }
    aipi = f'{rdm.randint(1,255)}.{rdm.randint(1,255)}.{rdm.randint(1,255)}.{rdm.randint(1,255)}'
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
    head = {
        "authorization": token,
        "host": "tech04.yoha.pro",
        "accept": "application/json",
        "content-type": "application/json; charset=utf-8",
        "user-agent": f"Mozilla/5.0 (iPhone11,2; U; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/602.{rdm.randint(0,255)}.{rdm.randint(0,255)} (KHTML, like Gecko) Version/9.0 Mobile/{rdm.randint(11,99)}E{rdm.randint(111,999)} Safari/602.1"
    }
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
    head = {
        "authorization": token,
        "host": "tech04.yoha.pro",
        "accept": "application/json",
        "content-type": "application/json; charset=utf-8",
        "user-agent": f"Mozilla/5.0 (iPhone11,2; U; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/602.{rdm.randint(0,255)}.{rdm.randint(0,255)} (KHTML, like Gecko) Version/9.0 Mobile/{rdm.randint(11,99)}E{rdm.randint(111,999)} Safari/602.1"
    }
    aipi = f'{rdm.randint(1,255)}.{rdm.randint(1,255)}.{rdm.randint(1,255)}.{rdm.randint(1,255)}'
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
    head = {
        "host": "api.yoha.pro",
        "accept": "application/json",
        "content-type": "application/json; charset=utf-8",
        "user-agent": f"Mozilla/5.0 (iPhone11,2; U; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/602.{rdm.randint(0,255)}.{rdm.randint(0,255)} (KHTML, like Gecko) Version/9.0 Mobile/{rdm.randint(11,99)}E{rdm.randint(111,999)} Safari/602.1"
    }
    aipi = f'{rdm.randint(1,255)}.{rdm.randint(1,255)}.{rdm.randint(1,255)}.{rdm.randint(1,255)}'
    param = {
        "user_login": no,
        "user_pass": passw,
        "user_email": "",
        "source": "",
        "v": persi,
        "ip": aipi,
        "l": "in",
    }
    uri = f'{data["host"]}api/auth/login'
    r = httpx.post(uri, params=param, headers=head)
    if r.status_code == 200:
        ress = json.loads(r.text)
        # print(f'\t\tCode : {ress["code"]}')
        if ress["code"] == 500:  # Akun atau kata sandi salah
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


def enter(token, aidi):
    head = {
        "authorization": token,
        "host": "tech04.yoha.pro",
        "accept": "application/json",
        "content-type": "application/json; charset=utf-8",
        "user-agent": f"Mozilla/5.0 (iPhone11,2; U; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/602.{rdm.randint(0,255)}.{rdm.randint(0,255)} (KHTML, like Gecko) Version/9.0 Mobile/{rdm.randint(11,99)}E{rdm.randint(111,999)} Safari/602.1"
    }
    aipi = f'{rdm.randint(1,255)}.{rdm.randint(1,255)}.{rdm.randint(1,255)}.{rdm.randint(1,255)}'
    param = {
        "v": persi,
        "ip": aipi,
        "l": "in",
    }
    uri = f'{data["api"]}live/enter?anchor_id={aidi}&v={persi}&ip={aipi}&l=in'
    r = httpx.post(uri, params=param, headers=head)
    if r.status_code == 200:
        ress = json.loads(r.text)
        return ress
    else:
        print(f"gagal status code : {r.text}")
        return 0


def startwatch(token, stream):
    head = {
        "authorization": token,
        "host": "tech04.yoha.pro",
        "accept": "application/json",
        "content-type": "application/json; charset=utf-8",
        "user-agent": f"Mozilla/5.0 (iPhone11,2; U; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/602.{rdm.randint(0,255)}.{rdm.randint(0,255)} (KHTML, like Gecko) Version/9.0 Mobile/{rdm.randint(11,99)}E{rdm.randint(111,999)} Safari/602.1"
    }
    aipi = f'{rdm.randint(1,255)}.{rdm.randint(1,255)}.{rdm.randint(1,255)}.{rdm.randint(1,255)}'
    param = {
        "v": persi,
        "ip": aipi,
        "l": "in",
    }
    uri = f'{data["api"]}live/startWatch?stream={stream}&v={persi}&ip={aipi}&l=in'
    r = httpx.post(uri, params=param, headers=head)
    if r.status_code == 200:
        ress = json.loads(r.text)
        return ress
    else:
        print(f"gagal status code : {r.text}")
        return 0


def kuit(token, aidi):
    head = {
        "authorization": token,
        "host": "tech04.yoha.pro",
        "accept": "application/json",
        "content-type": "application/json; charset=utf-8",
        "user-agent": f"Mozilla/5.0 (iPhone11,2; U; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/602.{rdm.randint(0,255)}.{rdm.randint(0,255)} (KHTML, like Gecko) Version/9.0 Mobile/{rdm.randint(11,99)}E{rdm.randint(111,999)} Safari/602.1"
    }
    aipi = f'{rdm.randint(1,255)}.{rdm.randint(1,255)}.{rdm.randint(1,255)}.{rdm.randint(1,255)}'
    param = {
        "v": persi,
        "ip": aipi,
        "l": "in",
    }
    uri = f'{data["api"]}live/quit?anchor_id={aidi}&watch_time={rdm.randint(7000,15000)}&v={persi}&ip={aipi}&l=in'
    r = httpx.post(uri, params=param, headers=head)
    if r.status_code == 200:
        ress = json.loads(r.text)
        return ress
    else:
        print(f"gagal status code : {r.text}")
        return 0


def balance(token, uid):
    head = {
        "host": "api.yoha.pro",
        "accept": "application/json",
        "content-type": "application/json; charset=utf-8",
        "user-agent": f"Mozilla/5.0 (iPhone11,2; U; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/602.{rdm.randint(0,255)}.{rdm.randint(0,255)} (KHTML, like Gecko) Version/9.0 Mobile/{rdm.randint(11,99)}E{rdm.randint(111,999)} Safari/602.1"
    }
    aipi = f'{rdm.randint(1,255)}.{rdm.randint(1,255)}.{rdm.randint(1,255)}.{rdm.randint(1,255)}'
    uri = f'{data["host"]}api/user/balance?token={token}&uid={uid}&v={persi}&ip={aipi}&l=in'
    r = httpx.get(uri, headers=head)
    if r.status_code == 200:
        ress = (json.loads(r.text))
        try:
            cek = ress['data']['diamonds']
            return cek
        except Exception as e:
            print(f"gagal : {ress['message']}")
            return 0


def follow(token, aidi):
    head = {
        "authorization": token,
        "host": "api.yoha.pro",
        "accept": "application/json",
        "content-type": "application/json; charset=utf-8",
        "user-agent": f"Mozilla/5.0 (iPhone11,2; U; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/602.{rdm.randint(0,255)}.{rdm.randint(0,255)} (KHTML, like Gecko) Version/9.0 Mobile/{rdm.randint(11,99)}E{rdm.randint(111,999)} Safari/602.1"
    }
    aipi = f'{rdm.randint(1,255)}.{rdm.randint(1,255)}.{rdm.randint(1,255)}.{rdm.randint(1,255)}'
    param = {
        "v": persi,
        "ip": aipi,
        "l": "in",
    }
    uri = f'{data["host"]}api/usersAttention/follow?inRoom=0&touid={aidi}&v={persi}.2&ip={aipi}&l=in'
    r = httpx.post(uri, params=param, headers=head)
    if r.status_code == 200:
        ress = (json.loads(r.text))
        msg = ress['status']
        return msg


def updateuser(token):
    head = {
        "authorization": token,
        "host": "api.yoha.pro",
        "accept": "application/json",
        "accept-encoding": "gzip",
        "content-type": "application/json; charset=utf-8",
        "user-agent": f"Mozilla/5.0 (iPhone11,2; U; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/602.{rdm.randint(0,255)}.{rdm.randint(0,255)} (KHTML, like Gecko) Version/9.0 Mobile/{rdm.randint(11,99)}E{rdm.randint(111,999)} Safari/602.1"
    }
    param = {
        "fields": {
            "avatar": input("avatar : "),
            "user_nicename": input("nama : "),
            # "is_anchor": True,
        },
    }
    uri = f'{data["host"]}api/auth/update-user'
    r = httpx.post(uri, data=json.dumps(param), headers=head)
    print(r.text)
    if r.status_code == 200:
        ress = (json.loads(r.text))
        msg = ress['status']
        return msg


def profileuser(token, id):
    head = {
        "authorization": token,
        "host": "api.yoha.pro",
        "accept": "application/json",
        "content-type": "application/json; charset=utf-8",
        "user-agent": f"Mozilla/5.0 (iPhone11,2; U; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/602.{rdm.randint(0,255)}.{rdm.randint(0,255)} (KHTML, like Gecko) Version/9.0 Mobile/{rdm.randint(11,99)}E{rdm.randint(111,999)} Safari/602.1"
    }
    aipi = f'{rdm.randint(1,255)}.{rdm.randint(1,255)}.{rdm.randint(1,255)}.{rdm.randint(1,255)}'
    uri = f'{data["host"]}api/auth/me?user_id={id}&v={persi}&ip={aipi}&l=in'
    r = httpx.get(uri, headers=head)
    if r.status_code == 200:
        ress = (json.loads(r.text))
        for akun in ress["data"]:
            cek = ress['data'][akun]
            return ress
        else:
            print(f"gagal : {ress['message']}")
            return 0


def rewardlist(token):
    head = {
        "authorization": token,
        "host": "api.yoha.pro",
        "accept": "application/json",
        "content-type": "application/json; charset=utf-8",
        "user-agent": f"Mozilla/5.0 (iPhone11,2; U; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/602.{rdm.randint(0,255)}.{rdm.randint(0,255)} (KHTML, like Gecko) Version/9.0 Mobile/{rdm.randint(11,99)}E{rdm.randint(111,999)} Safari/602.1"
    }
    aipi = f'{rdm.randint(1,255)}.{rdm.randint(1,255)}.{rdm.randint(1,255)}.{rdm.randint(1,255)}'
    param = {
        "v": persi,
        "ip": aipi,
        "l": "in",
    }
    uri = f'{data["host"]}api/tasks/userPoll?v={persi}&ip={aipi}&l=in'
    r = httpx.post(uri, params=param, headers=head)
    if r.status_code == 200:
        ress = json.loads(r.text)
        return ress
    else:
        print(f"gagal status code : {r.text}")
        return 0


def rewardclaim(token, aidi):
    head = {
        "authorization": token,
        "host": "api.yoha.pro",
        "accept": "application/json",
        "content-type": "application/json; charset=utf-8",
        "user-agent": f"Mozilla/5.0 (iPhone11,2; U; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/602.{rdm.randint(0,255)}.{rdm.randint(0,255)} (KHTML, like Gecko) Version/9.0 Mobile/{rdm.randint(11,99)}E{rdm.randint(111,999)} Safari/602.1"
    }
    aipi = f'{rdm.randint(1,255)}.{rdm.randint(1,255)}.{rdm.randint(1,255)}.{rdm.randint(1,255)}'
    param = {
        "v": persi,
        "ip": aipi,
        "l": "in",
    }
    uri = f'{data["host"]}api/tasks/receive/{aidi}?v={persi}&ip={aipi}&l=in'
    r = httpx.post(uri, params=param, headers=head)
    if r.status_code == 200:
        ress = json.loads(r.text)
        return ress
    else:
        print(f"gagal status code : {r.text}")
        return 0


def updaterandom(token):
    head = {
        "authorization": token,
        "host": "api.yoha.pro",
        "accept": "application/json",
        "content-type": "application/json; charset=utf-8",
        "user-agent": f"Mozilla/5.0 (iPhone11,2; U; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/602.{rdm.randint(0,255)}.{rdm.randint(0,255)} (KHTML, like Gecko) Version/9.0 Mobile/{rdm.randint(11,99)}E{rdm.randint(111,999)} Safari/602.1"
    }
    datp = fakebio.get()
    nama = datp["name"]
    if len(nama) > 20:
        nama = nama[0:20]
    head["user-agent"] = datp["useragent"]
    print("          >> "+nama.split(" ")[0][0:10])
    param = {
        "fields": {
            "user_nicename": nama.split(" ")[0][0:10]
        },
    }

    uri = f'{data["host"]}api/auth/update-user'
    r = httpx.post(uri, data=json.dumps(param), headers=head)
    if r.status_code == 200:
        ress = (json.loads(r.text))
        msg = ress['status']
        return msg


def tu(token):
    uag = f"Mozilla/5.0 (iPhone11,2; U; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/602.{rdm.randint(0,255)}.{rdm.randint(0,255)} (KHTML, like Gecko) Version/9.0 Mobile/{rdm.randint(11,99)}E{rdm.randint(111,999)} Safari/602.1"
    head = {
        "authorization": token,
        "host": "api.yoha.pro",
        "accept": "application/json, text/plain, */*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "id-ID,id;q=0.9",
        "content-type": "application/json; charset=utf-8",
        "cache-control": "no-store",
        "origin": "https://wv.yoha.pro",
        "referer": "https://wv.yoha.pro",
        "user-agent": uag
    }

    uid = profile(token)["data"]["id"]
    param = {
        "uid": uid,
        "token": token,
        "payment_channel_id": 69,
        "amount": input("jumlah topup : "),
        "get_recharge_gift": "0",
    }

    uri = f'{data["host"]}api/paymentorders/createorder'
    r = httpx.post(uri, params=param, headers=head)
    print(r.text)
    if r.status_code == 200:
        ress = (json.loads(r.text))
        oweb(ress["data"]["pay_url"])
        print(ress)


def getmsg(token, streamid):
    head = {
        "authorization": token,
        "host": "tech04.yoha.pro",
        "accept": "application/json",
        "content-type": "application/json; charset=utf-8",
        "user-agent": f"Mozilla/5.0 (iPhone11,2; U; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/602.{rdm.randint(0,255)}.{rdm.randint(0,255)} (KHTML, like Gecko) Version/9.0 Mobile/{rdm.randint(11,99)}E{rdm.randint(111,999)} Safari/602.1"
    }
    aipi = f'{rdm.randint(1,255)}.{rdm.randint(1,255)}.{rdm.randint(1,255)}.{rdm.randint(1,255)}'
    param1 = {
        "stream": streamid,
        "v": persi,
        "ip": aipi,
        "l": "in"
    }
    uri = f'{data["api"]}live/msgHistory'
    try:
        r = httpx.post(uri, data=json.dumps(param1), headers=head, timeout=5)
        if r.status_code == 200:
            ressx = (json.loads(r.text))
            return ressx
        print(f"{r.text}")
    except Exception as error:
        print(error)
    return 0


def getuser(token, streamid):
    head = {
        "authorization": token,
        "host": "tech04.yoha.pro",
        "accept": "application/json",
        "content-type": "application/json; charset=utf-8",
        "user-agent": f"Mozilla/5.0 (iPhone11,2; U; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/602.{rdm.randint(0,255)}.{rdm.randint(0,255)} (KHTML, like Gecko) Version/9.0 Mobile/{rdm.randint(11,99)}E{rdm.randint(111,999)} Safari/602.1"
    }
    aipi = f'{rdm.randint(1,255)}.{rdm.randint(1,255)}.{rdm.randint(1,255)}.{rdm.randint(1,255)}'
    param1 = {
        "anchor_id": streamid,
        "type": "1",
        "page": "1",
        "per_page": "100",
        "need_robot": "false",
        "v": persi,
        "ip": aipi,
        "l": "in"
    }
    uri = f'{data["api"]}live/getUserList'
    try:
        r = httpx.post(uri, data=json.dumps(param1), headers=head, timeout=5)
        if r.status_code == 200:
            ressx = (json.loads(r.text))
            return ressx
        print(f"{r.text}")
    except Exception as error:
        print(error)
    return 0

def simi(tex):
    uriweb = f"https://api.simsimi.net/v2/?text={tex}&lc=id"
    headers = {
        "user-agent": f"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.{rdm.randint(100000,999999)}.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.{rdm.randint(1000,9999)}.{rdm.randint(100,999)} Mobile Safari/537.36",
    }
    res = httpx.get(uriweb, headers=headers)
    res = json.loads(res.text)
    return res
