import httpx,json,time,pytz,sys,random
from tinydb import *
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
        "user-agent": f"HS-Android Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.17{random.randint(1000,9999)}.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.{random.randint(1000,9999)}.82 Mobile Safari/537.36",
        "bundleidentifier": "user",
        "x-token": x,
        "accept-encoding": "identity",
        "host": "wjxwd01mwyo.dt01showxx02.com",
        "connection": "keep-alive",
    }
    f = httpx.get(uriweb, headers=headers)
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

with open(f"user_token.json", 'r') as json_file:
    xtokens=json.load(json_file)["results"]
token=xtokens[int(input("Token ke: "))-1]
    
while True:
    tz = pytz.timezone("Asia/Jakarta")
    now = datetime.now(tz)
    xx=now.strftime("%H:%M:%S")
    detik=now.strftime("%S")
    sys.stdout.write(f"'\t{xx} \r")
    sys.stdout.flush()
    time.sleep(0.3)
    if detik == "10":
        try:
            disp=""
            db = TinyDB("rec.json")
            sett = db.table('data')
            tkk =sett.all()
            tkk=(tkk[len(tkk)-1])
            if tkk["pola"] == 1:
                pola=c("green","↑",0)
            else:
                pola=c("red","↓",0)
            big,small,odd,even,any,sbs,soe=c("red",tkk["big"],0),c("blue",tkk["small"],0),c("cyan",tkk["odd"],0),c("magenta",tkk["even"],0),c("yellow",tkk["any"],0),c("yellow",tkk["selisihbs"],0),c("yellow",tkk["selisihoe"],0)
            disp+=(f"  [{xx[:5]}] Big:{big} Small:{small} Odd:{odd} Even:{even} any:{any} {pola}[{sbs}:{soe}]")

            xxz = getinfo(token)
            nickname=xxz[0]
            piaipi=xxz[2]
            coinbaru=float(xxz[1])
            if coin>coinbaru:
                disp+=(f" {c('red','↓ '+str(round(coin-coinbaru)),0)}  [{coinbaru}]")
            else:
                disp+=(f" {c('green','↑ '+str(round(coinbaru-coin)),0)}  [{coinbaru}]")
            coin=coinbaru
            print(disp)
            time.sleep(4)
        except Exception as e:
            print(getinfo(token))
            # print(f"Error : {e}")


