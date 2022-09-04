import pyrebase
import requests
import json,time
import seting,getcodebind
import sys
import webbrowser,random
import ambil
from datetime import datetime


persi = seting.versi()
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

tes = True
dat = {
    "jam": []
}
try:
    kusus1 = int(sys.argv[1])
    kusus2 = int(sys.argv[2])
except:
    kusus1 = 0
    kusus2 = 999


ataroinvcode = "yBooNa"


def disp(x):
    sys.stdout.write(f"\t                   \r")
    sys.stdout.flush()
    sys.stdout.write(f"\t{x}\r")
    sys.stdout.flush()
def oweb(url):
    webbrowser.register('chrome',
                        None,
                        webbrowser.BackgroundBrowser("C:\\Users\\User\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe"))
    webbrowser.get('chrome').open_new(url)


def loginid(x):
    uri = "https://wjxwd01mwyo.dt01showxx02.com/App/User_LoginRegister/Login"
    headers = {
        "User-Agent": f"HS-Android Mozilla/5.0 (Linux; Android 8.1.0; SM-J730F Build/{random.randint(1000,9999)}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.{random.randint(1000,9999)}.129 Mobile Safari/537.36",
        "BundleIdentifier": "user",
        "Accept-Encoding": "identity",
        "X-Version": persi,
        "Content-Type": "application/json; charset=UTF-8",
        "Host": "wjxwd01mwyo.dt01showxx02.com",
        "Connection": "Keep-Alive"
    }
    param = x
    # kalau mau reset v1
    param['force_new'] = '1'
    param['invite_code'] = ataroinvcode
    # print(param)
    # exit()

    proxx={
        "https":input("Proxy : ")
    }
    try:
        req = requests.post(uri, data=json.dumps(param), headers=headers,proxies=proxx)
        ress = json.loads(req.text)
        return ress
    except Exception as e:
        print("Failed : "+str(e))
        return 0

def logingame(x):
    uri = "https://wjxwd01mwyo.dt01showxx02.com/App/ThirdGame_Index/Login"
    headers = {
        "User-Agent": f"HS-Android Mozilla/5.0 (Linux; Android 8.1.0; SM-J730F Build/{random.randint(1000,9999)}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.{random.randint(1000,9999)}.129 Mobile Safari/537.36",
        "BundleIdentifier": "user",
        "Accept-Encoding": "identity",
        "X-Version": persi,
        "x-token": x,
        "Content-Type": "application/json; charset=UTF-8",
        "Host": "wjxwd01mwyo.dt01showxx02.com",
        "Connection": "Keep-Alive"
    }
    param = {
        "kind_id":256,
        "live_id":0,
        "platform":"sb"
    }

    try:
        req = requests.post(uri, data=json.dumps(param), headers=headers)
        ress = json.loads(req.text)
        print(ress)
        dispgame="""
    1. Saldo
    2. Saba
    """
        game3=input(f"{dispgame}game nomer :")
        if game3=="1":
            uri="https://wjxwd01mwyo.dt01showxx02.com/App/ThirdGame_Index/Accounts?platforms=sb"
            req = requests.get(uri,  headers=headers)
            ress = json.loads(req.text)
            print(json.dumps(ress["result"],indent=2))
        elif game3=="2":
            mensaba="""
    1. TU
    2. WD
    3. Open
    """
            sabb=input(f"{mensaba}pilih nomer :")
            if sabb=="1":
                uri="https://wjxwd01mwyo.dt01showxx02.com/App/ThirdGame_Index/UpperScore"
                param={
                    "from":"cp",
                    "score":input("coin : "),
                    "to":"sb"
                }
                req = requests.post(uri, data=json.dumps(param), headers=headers)
                ress1 = json.loads(req.text)
                print(ress1)
            elif sabb=="2":
                uri="https://wjxwd01mwyo.dt01showxx02.com/App/ThirdGame_Index/LowerScore"
                param={
                    "from":"sb",
                    "score":input("coin : "),
                    "to":"cp"
                }
                req = requests.post(uri, data=json.dumps(param), headers=headers)
                ress1 = json.loads(req.text)
                print(ress1)
            elif sabb=="3":
                oweb(ress["result"]["url"])
            else:
                print("pilihan tidak ada")

        else:
            print("pilihan tidak ada")
    except Exception as e:
        print("Failed : "+str(e))
        return 0

def getbankinfo(x):
    uriweb = "https://wjxwd01mwyo.dt01showxx02.com/App/Pay_BankCard/Mine"
    headers = {
        "user-agent": f"HS-Android Mozilla/5.0 (Linux; Android 8.1.0; SM-J730F Build/{random.randint(1000,9999)}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.{random.randint(1000,9999)}.129 Mobile Safari/537.36",
        "bundleidentifier": "user",
        "x-token": x,
        "accept-encoding": "identity",
        "host": "wjxwd01mwyo.dt01showxx02.com",
        "connection": "keep-alive"
    }
    f = requests.get(uriweb, headers=headers)
    ress = json.loads(f.text)
    try:
        return ress
    except:
        print("Token Expiret")
        return 0


def setpwd(x, pwnya):
    uri = "https://wjxwd01mwyo.dt01showxx02.com/App/Pay_User/SetPwd"
    headers = {
        "User-Agent": f"HS-Android Mozilla/5.0 (Linux; Android 8.1.0; SM-J730F Build/{random.randint(1000,9999)}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.{random.randint(1000,9999)}.129 Mobile Safari/537.36",
        "BundleIdentifier": "user",
        "Accept-Encoding": "identity",
        "x-token": x,
        "X-Version": persi,
        "Content-Type": "application/json; charset=UTF-8",
        "Host": "wjxwd01mwyo.dt01showxx02.com",
        "Connection": "Keep-Alive"
    }
    param = {'pwd': pwnya}

    try:
        req = requests.post(uri, data=json.dumps(param), headers=headers)
        ress = json.loads(req.text)
        return ress
    except Exception as e:
        print("Failed : "+str(e))
        return 0


def setemail(tkn, email, code):
    uri = "https://wjxwd01mwyo.dt01showxx02.com/App/User_User/BindEmail"
    headers = {
        "User-Agent": f"HS-Android Mozilla/5.0 (Linux; Android 8.1.0; SM-J730F Build/{random.randint(1000,9999)}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.{random.randint(1000,9999)}.129 Mobile Safari/537.36",
        "BundleIdentifier": "user",
        "x-token": tkn,
        "Accept-Encoding": "identity",
        "X-Version": persi,
        "Content-Type": "application/x-www-form-urlencoded",
        "Host": "wjxwd01mwyo.dt01showxx02.com",
        "Connection": "Keep-Alive"
    }
    param = {
        "email": email,
        "code": code
    }

    try:
        req = requests.post(uri, data=param, headers=headers)
        ress = json.loads(req.text)
        return ress["msg"]
    except Exception as e:
        print("Failed : "+str(e))
        return 0


def setphone(tkn, phone, code):
    uri = "https://wjxwd01mwyo.dt01showxx02.com/App/User_User/BindPhone"
    headers = {
        "User-Agent": f"HS-Android Mozilla/5.0 (Linux; Android 8.1.0; SM-J730F Build/{random.randint(1000,9999)}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.{random.randint(1000,9999)}.129 Mobile Safari/537.36",
        "BundleIdentifier": "user",
        "x-token": tkn,
        "Accept-Encoding": "identity",
        "X-Version": persi,
        "Content-Type": "application/x-www-form-urlencoded",
        "Host": "wjxwd01mwyo.dt01showxx02.com",
        "Connection": "Keep-Alive"
    }
    param = {
        "email": "+62",
        "email": phone,
        "code": code
    }

    try:
        req = requests.post(uri, data=param, headers=headers)
        ress = json.loads(req.text)
        return ress["msg"]
    except Exception as e:
        print("Failed : "+str(e))
        return 0


def setbank(x, data):
    uri = "https://wjxwd01mwyo.dt01showxx02.com/App/Pay_BankCard/Add"
    headers = {
        "User-Agent": f"HS-Android Mozilla/5.0 (Linux; Android 8.1.0; SM-J730F Build/{random.randint(1000,9999)}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.{random.randint(1000,9999)}.129 Mobile Safari/537.36",
        "BundleIdentifier": "user",
        "Accept-Encoding": "identity",
        "x-token": x,
        "X-Version": persi,
        "Content-Type": "application/json; charset=UTF-8",
        "Host": "wjxwd01mwyo.dt01showxx02.com",
        "Connection": "Keep-Alive"
    }
    param = data

    try:
        req = requests.post(uri, data=json.dumps(param), headers=headers)
        ress = json.loads(req.text)
        return ress
    except Exception as e:
        print("Failed : "+str(e))
        return 0


def proseswd(x, data):
    uri = "https://wjxwd01mwyo.dt01showxx02.com/App/Pay_Withdrawal/Apply"
    headers = {
        "User-Agent": f"HS-Android Mozilla/5.0 (Linux; Android 8.1.0; SM-J730F Build/{random.randint(1000,9999)}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.{random.randint(1000,9999)}.129 Mobile Safari/537.36",
        "BundleIdentifier": "user",
        "Accept-Encoding": "identity",
        "x-token": x,
        "X-Version": persi,
        "Content-Type": "application/json; charset=UTF-8",
        "Host": "wjxwd01mwyo.dt01showxx02.com",
        "Connection": "Keep-Alive"
    }
    param = data
    prox = {
        "https": input("proxy : ")
    }
    try:
        req = requests.post(uri, data=json.dumps(
            param), headers=headers, proxies=prox)
        ress = json.loads(req.text)
        return ress
    except Exception as e:
        print("Failed : "+str(e))
        return 0


def getmsg(x):
    uriweb = "https://wjxwd01mwyo.dt01showxx02.com/App/Message/List?page1"
    headers = {
        "user-agent": f"HS-Android Mozilla/5.0 (Linux; Android 8.1.0; SM-J730F Build/{random.randint(1000,9999)}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.{random.randint(1000,9999)}.129 Mobile Safari/537.36",
        "bundleidentifier": "user",
        "x-token": x,
        "accept-encoding": "identity",
        "host": "wjxwd01mwyo.dt01showxx02.com",
        "connection": "keep-alive",
    }
    f = requests.get(uriweb, headers=headers)
    ress = json.loads(f.text)
    try:
        krm = [
            ress["result"]
        ]
        return krm
    except:
        krm = [
            "expiret",
            0.0,
            "expiret",
            "expiret",
        ]
        return krm


def getrecord(x):
    waktu = input("waktunya [2022-08-04] :")
    uriweb = f"https://wjxwd01mwyo.dt01showxx02.com/App/Game_Order/GetBetList?date={waktu}&status=0&page=1"
    headers = {
        "user-agent": f"HS-Android Mozilla/5.0 (Linux; Android 8.1.0; SM-J730F Build/{random.randint(1000,9999)}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.{random.randint(1000,9999)}.129 Mobile Safari/537.36",
        "bundleidentifier": "user",
        "x-token": x,
        "accept-encoding": "identity",
        "host": "wjxwd01mwyo.dt01showxx02.com",
        "connection": "keep-alive",
    }
    f = requests.get(uriweb, headers=headers)
    ress = json.loads(f.text)
    try:
        krm = ress["result"]
        return krm
    except:
        krm = [
            "expiret",
            0.0,
            "expiret",
            "expiret",
        ]
        return krm


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
    stat=0
    while stat!=200:
        f = requests.get(uriweb, headers=headers)
        stat=f.status_code
        if stat==200:
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
                    str(ress),
                    "expiret",
                ]
        else:
            disp("Reconnect")
    return krm


def getinfofull(x):
    uriweb = "https://wjxwd01mwyo.dt01showxx02.com/App/User_User/Info"
    headers = {
        "user-agent": f"HS-Android Mozilla/5.0 (Linux; Android 8.1.0; SM-J730F Build/{random.randint(1000,9999)}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.{random.randint(1000,9999)}.129 Mobile Safari/537.36",
        "bundleidentifier": "user",
        "x-token": x,
        "accept-encoding": "identity",
        "host": "wjxwd01mwyo.dt01showxx02.com",
        "connection": "keep-alive",
    }
    f = requests.get(uriweb, headers=headers)
    ress = json.loads(f.text)
    try:
        krm = [
            ress["result"]
        ]
        return krm
    except:
        krm = [
            "expiret",
            0.0,
            "expiret",
            "expiret",
        ]
        return krm


def getcashlog(x):
    uriweb = f"https://wjxwd01mwyo.dt01showxx02.com/App/User_User/CashLogList?page={input('page : ')}"
    headers = {
        "user-agent": f"HS-Android Mozilla/5.0 (Linux; Android 8.1.0; SM-J730F Build/{random.randint(1000,9999)}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.{random.randint(1000,9999)}.129 Mobile Safari/537.36",
        "bundleidentifier": "user",
        "x-token": x,
        "accept-encoding": "identity",
        "host": "wjxwd01mwyo.dt01showxx02.com",
        "connection": "keep-alive",
    }
    f = requests.get(uriweb, headers=headers)
    ress = json.loads(f.text)
    try:
        return ress["result"]
    except:
        krm = [
            "expiret",
            0.0,
            "expiret",
            "expiret",
        ]
        return krm


def lvl(x):
    stat=0
    while stat!=200:
        uriweb = "https://wjxwd01mwyo.dt01showxx02.com/App/Vip_Vip/MyVip"
        headers = {
            "x-ws-apm-id": "0068CBCA-9E03-4264-A904-EC90ADE4F434-259",
            "user-agent": f"HS-Android Mozilla/5.0 (Linux; Android 8.1.0; SM-J730F Build/{random.randint(1000,9999)}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.{random.randint(1000,9999)}.129 Mobile Safari/537.36",
            "bundleidentifier": "user",
            "x-token": x,
            "accept-encoding": "identity",
            "x-version": persi,
            "host": "wjxwd01mwyo.dt01showxx02.com",
            "connection": "keep-alive"
        }
        f = requests.get(uriweb, headers=headers)
        stat=f.status_code
        if stat==200:
            datas = json.loads(f.text)
            break
        else:
            disp("Reconnect")
    return datas["result"]


def tu(tkn, mett):
    uri = "https://wjxwd01mwyo.dt01showxx02.com/App/Pay_Recharge/Auto"
    headers = {
        "User-Agent": f"HS-Android Mozilla/5.0 (Linux; Android 8.1.0; SM-J730F Build/{random.randint(1000,9999)}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.{random.randint(1000,9999)}.129 Mobile Safari/537.36",
        "BundleIdentifier": "user",
        "x-token": tkn,
        "Accept-Encoding": "identity",
        "X-Version": persi,
        "Content-Type": "application/x-www-form-urlencoded",
        "Host": "wjxwd01mwyo.dt01showxx02.com",
        "Connection": "Keep-Alive"
    }
    param = f"money=10&channel_id={mett}"

    try:
        req = requests.post(uri, data=param, headers=headers)
        ress = json.loads(req.text)
        return ress
    except Exception as e:
        print("Failed : "+str(e))
        return 0


def jam():
    now = datetime.now()
    jamm = now.strftime("%d %H")
    minut = now.strftime("%M")
    if minut == "01":
        if jamm not in dat["jam"]:
            # print(dat["jam"])
            return True
        else:
            # print("sudah")
            return False
    else:
        # print(minut)
        return False


def filterspace(x):
    d = ""
    for i in x:
        if i != "\n":
            d += i
    return d


menu = """

       [MENU]
  > connection
  > cekfull
  > cek
  > lvl
  > tu
  > reset
  > gtoken
  > gmsg
  > grecord
  > gcashlog
  > cekbank
  > setbank
  > setphone
  > getcodeemail
  > setemail
  > wd
  > q
\tChoice : """
while True:
    jlk = input(menu)
    print()
    if jlk == "q":
        break
    elif jlk == "gtoken":
        tokk = ambil.token()
        print(tokk[int(input("token ke : "))-1])
    elif jlk == "connection":
        tokk = ambil.token()
        token = tokk[0]
        uriweb = "https://wjxwd01mwyo.dt01showxx02.com/App/User_User/Info"
        headers = {
            "user-agent": f"HS-Android Mozilla/5.0 (Linux; Android 8.1.0; SM-J730F Build/{random.randint(1000,9999)}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.{random.randint(1000,9999)}.129 Mobile Safari/537.36",
            "bundleidentifier": "user",
            "x-token": token,
            "accept-encoding": "identity",
            "host": "wjxwd01mwyo.dt01showxx02.com",
            "connection": "keep-alive",
        }
        f = requests.get(uriweb, headers=headers)
        print(f"status code : {f.status_code}")
        print(f"status code : {f.headers}")
        print(f"status code : {f.text}")
    elif jlk == "setbank":
        tokk = ambil.token()
        token = tokk[int(input("token ke : "))-1]
        pwd = input("set password len[6]")
        print(f"password : {pwd}")
        print("Auto set to Gopay")
        databank = {
            "name": input("nama : "),
            "number": input("number : "),
            "type": "138",
            "pwd": pwd,
            "extra_content": "",
        }

        print(setpwd(token, pwd))
        print(setbank(token, databank))
    elif jlk == "getcodeemail":
        tokk = ambil.token()
        token = tokk[int(input("token ke : "))-1]
        ema = input("email : ")
        ksign = input("sign : ")
        print(getcodebind.getcode(token, ema, ksign))
    elif jlk == "setemail":
        print("ambil codenya dr hp")
        tokk = ambil.token()
        token = tokk[int(input("token ke : "))-1]
        ema = input("email : ")
        kodd = input("kode : ")
        print(setemail(token, ema, kodd))
    elif jlk == "setphone":
        print("req codenya dr hp")
        tokk = ambil.token()
        token = tokk[int(input("token ke : "))-1]
        ema = input("nomer tanpa 0 : ")
        kodd = input("kode : ")
        print(setphone(token, ema, kodd))
    elif jlk == "wd":
        tokk = ambil.token()
        token = tokk[int(input("token ke : "))-1]
        gbi = getbankinfo(token)["result"]
        print(json.dumps(gbi, indent=2))

        databank = {
            "money": int(input("coin : ")),
            "card_id": int(input("card_id : ")),
            "pwd": int(input("pwd : "))
        }
        print(databank)
        reqwd = proseswd(token, databank)
        print(reqwd)
    elif jlk == "cekbank":
        tokk = ambil.token()
        token = tokk[int(input("token ke : "))-1]
        gbi = getbankinfo(token)["result"]
        print(json.dumps(gbi, indent=2))
    elif jlk == "game":
        tokk = ambil.token()
        token = tokk[int(input("token ke : "))-1]
        logingame(token)
    elif jlk == "gmsg":
        tokk = ambil.token()
        token = tokk[int(input("token ke : "))-1]
        xxz = getmsg(token)
        for tiu in xxz:
            print(
                "==========================================================================")
            for tiuu in tiu:
                print(f'{tiuu["created_at"]} : {tiuu["content"]}')
                print(
                    "==========================================================================")
    elif jlk == "grecord":
        tokk = ambil.token()
        token = tokk[int(input("token ke : "))-1]
        xxz = getrecord(token)
        for tiu in xxz["data"]:
            if tiu["status"] == 2:
                wl = "Win"
            else:
                wl = "Lose"
            print(
                f'===================================[ {tiu["game_type"]} ]')
            print(f'\tStatus : {wl}')
            print(f'\tBet : {tiu["total_cost"]}')
            print(f'\t<- : {tiu["win_amount"]}')
            print(f'\tGame_number : {tiu["game_number"]}')
            print(f'\tId : {tiu["order_id"]}')
    elif jlk == "gcashlog":
        tokk = ambil.token()
        token = tokk[int(input("token ke : "))-1]
        xxz = getcashlog(token)
        for tiu in xxz:
            print(
                "==========================================================================")
            print(f"> {tiu}")
            for tiuu in xxz[tiu]:
                if "dealed_at" in tiuu:
                    print(f'\tdealed_at : {tiuu["dealed_at"]}')
                    print(f'\tcontent : {tiuu["content"]}')
                    print(f'\tbalance_before : {tiuu["balance_before"]}')
                    print(f'\tbalance_after : {tiuu["balance_after"]}')
                    print(f'\ttype_name : {tiuu["type_name"]}')
                    print(
                        "==========================================================================")
                else:
                    print(tiuu)

    elif jlk == "cekfull":
        tokk = ambil.token()
        token = tokk[int(input("token ke : "))-1]
        try:
            dtt = getinfofull(token)
            print(json.dumps(dtt[0], indent=2))

        except Exception as e:
            print(f"error {e}")
            tn = input("exit y/n :")
            if tn == "y":
                exit()
    elif jlk == "cek":
        tokk = ambil.token()
        if kusus2 == 999:
            kusus2 = len(tokk)
        token = tokk[kusus1:kusus2]

        tota = []
        for i in range(len(token)):
            time.sleep(5)
            try:
                dtt = getinfo(token[i])
                # print(dtt)
                nam, bele, rnk, idd = dtt[0], dtt[1], dtt[2], dtt[3]
                kj = len(nam)
                print(
                    "   {}. [{}][{}][{}] {}".format(
                        str(i + 1), idd, rnk, bele, filterspace(nam)
                    )
                )
                try:
                    tota.append(float(bele))
                except:
                    pass

            except Exception as e:
                print(f"error {e}")
                tn = input("exit y/n :")
                if tn == "y":
                    exit()
        tot = sum(map(float, tota))

        now = datetime.now()
        klj = now.strftime("%H:%M:%S")
        print("\nTotal : " + str(tot) + " ____ " + klj)
        ess = ((60.0 / 100) * (float(tot) - 28)) * 3000
        print(f"estimasi wd : {ess}")
    elif jlk == "lvl":
        tokk = ambil.token()
        if kusus2 == 999:
            kusus2 = len(tokk)
        token = tokk[kusus1:kusus2]

        tota = []
        for i in range(len(token)):
            time.sleep(4)
            data = lvl(token[i])
            try:
                nama = data["nickname"]
                if len(nama) < 9:
                    nama = nama+"\t"
                vip = data["vip_name"]
                target = data["vip_relegation"]["relegation_recharge"]
                sudah_tu = data["vip_relegation"]["recharge_amount"]
                expiret = data["vip_relegation"]["remainder_days"]
                print(
                    f"   {i+1}. {nama}\t[{vip}] [{target}/{sudah_tu}] {expiret} days")
            except Exception as e:
                print(data)
                print(f"error {e}")
                tn = input("exit y/n :")
                if tn == "y":
                    exit()
        now = datetime.now()
        klj = now.strftime("%H:%M:%S")
        print(f"\tScanning Time : {klj}")
    elif jlk == "tu":
        print("""
        1. Bank QR
        2. Dana
        """)
        mett = input("method : ")
        if mett == "1":
            mett = "173"
        elif mett == "2":
            mett = "189"
        while True:
            idxtu = input("\n   Token ke : ")
            print()
            if idxtu == "q":
                break

            idxtu = int(idxtu)-1

            tokk = ambil.token()
            if kusus2 == 999:
                kusus2 = len(tokk)
            token = tokk[kusus1:kusus2]

            token = token[idxtu]
            xc = tu(token, mett)
            try:
                print(xc["result"]["pay_url"])
                oweb(xc["result"]["pay_url"])
            except:
                print(xc)
    elif jlk == "reset":
        try:
            while True:
                idxtu = input("   Token ke : ")
                if idxtu == "q":
                    break
                idxtu = int(idxtu)-1

                tokk = ambil.token()
                uid = ambil.uid()[idxtu]
                print(uid)

                print("=============================================================")
                token = loginid(uid)
                print(token)
                token=token["result"]["access_token"]
                print(json.dumps(token, indent=2))

                print("=============================================================")
                tokk[idxtu] = token
                print(getinfo(token))

                aplot = {"results": tokk}
                db.child("account").child("token").update(aplot)
        except Exception as e:
            print(str(e))
    else:
        print("menu not found")
