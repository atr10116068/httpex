import requests,json,ambil,time,pytz,sys
from datetime import datetime
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
def getinfo(x):
    uriweb = "https://wjxwd01mwyo.dt01showxx02.com/App/User_User/Info"
    headers = {
        "user-agent": "HS-Android Mozilla/5.0 (Linux; Android 8.1.0; SM-J730F Build/M1AJQ; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36",
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
        return krm

coin=0.0
tokk = ambil.token()
if input("Enter to set token from db")!="":
    with open("user_token.json") as json_file:
        token = json.load(json_file)["results"][0]
else:
    token=tokk[int(input("token ke : "))-1]
while True:
    tz = pytz.timezone("Asia/Jakarta")
    now = datetime.now(tz)
    xx=now.strftime("%H:%M:%S")
    detik=now.strftime("%S")
    sys.stdout.write(f"'\t{xx} \r")
    sys.stdout.flush()
    time.sleep(0.3)
    if detik == "10":
        xxz = getinfo(token)
        coinbaru=float(xxz[1])
        if coin>coinbaru:
            tex=(f"\t{xx} : {xxz[0]} [{str(coinbaru)}] {c('red','↓ '+str(round(coin-coinbaru)),0)}")
        else:
            tex=(f"\t{xx} : {xxz[0]} [{str(coinbaru)}] {c('green','↑ '+str(round(coinbaru-coin)),0)}")
        print(tex)
        coin=coinbaru
        time.sleep(4)
