import requests
import sys
import seting
import json
import time
import pytz
import datetime as dt
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


def geth(token):
    link = "https://dt001piwfw.d9sph.cn/App/Game_Game/GetLatestLottery?page=1"
    headers = {
        "user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.171019.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36",
        "bundleidentifier": "user",
        "x-token": token,
        "accept-encoding": "identity",
        "xversion": seting.versi(),
    }

    req = requests.get(url=link, headers=headers, timeout=100)
    reqs = json.dumps(req.json())
    reqs = json.loads(reqs)

    status = req.status_code
    req.close()
    if status == 200:
        # print(f"{threadName}: Working page : {proxy['page']}")
        try:
            return(reqs["result"])
        except Exception as e:
            print(f"Error : {e}")
            pass
    else:
        # print(f"{threadName}: Connection Code Status Error:{status}")
        pass


with open(r"C:\Users\User\Desktop\tpx_pc\pc\user_token.json") as json_file:
    tokk = json.load(json_file)
token = tokk["results"][0]

gg = """ThreeDice
Sic Bo
Baccarat
Color Light
Dragon Tiger
All

Game:"""
inp = input(gg)
while True:
    tzn = pytz.timezone("Asia/Jakarta")
    now = datetime.now(tzn)
    wktu = now.strftime("%d-%m %H:%M:%S")
    dtk = now.strftime("%S")
    sys.stdout.write(f"{wktu} \r")
    sys.stdout.flush()
    if dtk == "03":
    # if int(dtk) %2 == 0:
        databc = geth(token)
        if inp == "All":
            for bc in databc:
                if bc["game_cname"] == "ThreeDice":
                    import sicbo as tpx
                    print(tpx.p(bc))
                elif bc["game_cname"] == "Sic Bo":
                    import sicbo as tpx
                    print(tpx.p(bc))
                elif bc["game_cname"] == "Baccarat":
                    import baccarat as tpx
                    print(tpx.p(bc))
                elif bc["game_cname"] == "Color Light":
                    import colorl as tpx
                    print(tpx.p(bc))
                elif bc["game_cname"] == "Dragon Tiger":
                    import dragon as tpx
                    print(tpx.p(bc))
        else:
            for bc in databc:
                if bc["game_cname"] == "ThreeDice" and inp=="ThreeDice":
                    import sicbo as tpx
                    print(tpx.p(bc))
                elif bc["game_cname"] == "Sic Bo" and inp=="Sic Bo":
                    import sicbo as tpx
                    print(tpx.p(bc))
                elif bc["game_cname"] == "Baccarat" and inp=="Baccarat":
                    import baccarat as tpx
                    print(tpx.p(bc))
                elif bc["game_cname"] == "Color Light" and inp=="Color Light":
                    import colorl as tpx
                    print(tpx.p(bc))
                elif bc["game_cname"] == "Dragon Tiger" and inp=="Dragon Tiger":
                    import dragon as tpx
                    print(tpx.p(bc))

    time.sleep(1)
