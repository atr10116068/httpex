import json, time, pytz, sys
import datetime
from datetime import datetime
import colorama
from colorama import Fore, Style, Back

colorama.init()

db = {}


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


def getmenit(x):
    return "{:02d}:{:02d}".format(*divmod(int(x), 60))


def disp(t):
    cx = {
        "id": ["YELLOW", 0],
        "dadu": ["WHITE", 0],
        "B": ["CYAN", 0],
        "O": ["CYAN", 0],
        "S": ["BLUE", 0],
        "E": ["BLUE", 0],
    }
    aidi = t["game_number"][8::]
    dadu = f'{t["cards"][0]} {t["cards"][1]} {t["cards"][2]}'
    if t["tip"][1] == "Big":
        bs = "B"
    else:
        bs = "S"
    if t["tip"][2] == "Odd":
        oe = "O"
    else:
        oe = "E"

    if t["cards"][0] == t["cards"][1] and t["cards"][1] == t["cards"][2]:
        cx["id"][1] = 1
        cx["dadu"][1] = 1
        cx[bs][1] = 1
        cx[oe][1] = 1

    cxaidi = c(cx["id"][0], getmenit(aidi), cx["id"][1])
    cxdadu = c(cx["dadu"][0], dadu, cx["dadu"][1])
    cxbs = c(cx[bs][0], bs, cx[bs][1])
    cxoe = c(cx[oe][0], oe, cx[oe][1])
    print(f"\t{cxaidi} {cxdadu} {cxbs} {cxoe}")


data = {"results": []}


with open("sicbo.json", "r") as openfile:
    # Reading from json file
    datapp = json.load(openfile)

    for tyew in datapp["results"]:
        data["results"].append(tyew)

for t in data["results"]:
    disp(t)

dat = {"menit": ""}

tz = pytz.timezone("Asia/Jakarta")
now = datetime.now(tz)
dat["jam"] = now.strftime("%d%b%Y-%H:%M:%S")
menit = now.strftime("%M")
dat["menit"] = int(menit)
while True:
    tz = pytz.timezone("Asia/Jakarta")
    now = datetime.now(tz)
    dat["jam"] = now.strftime("%d%b%Y-%H:%M:%S")
    menit = now.strftime("%M")
    detik = now.strftime("%S")
    sys.stdout.write(f"\trealtime : {menit}:{detik}                    \r")
    sys.stdout.flush()
    if int(menit) != dat["menit"]:
        time.sleep(6)
        dat["menit"] = int(menit)
        with open("sicbo.json", "r") as openfile:
            # Reading from json file
            datapp = json.load(openfile)
        databaru = []
        for t in datapp["results"]:
            databaru.append(t)
        databaru.reverse()
        apdet = databaru[0]
        data["results"].append(apdet)
        disp(apdet)

