import requests
import seting
import random
import ambil
import sys
import json
import time
from tinydb import *
from colorama import Fore, Style, init
import random
init()

idroom = sys.argv[1]
db = TinyDB(f"{idroom}.json")
tbl = Query()

persi = seting.versi()
tokenhost = ambil.tokenhost()

sett = {
    "1": {"clr": "black", "lvl": "1"},
    "2": {"clr": "yellow", "lvl": "4"},
    "3": {"clr": "red", "lvl": "13"},
    "4": {"clr": "yellow", "lvl": "5"},
    "5": {"clr": "cyan", "lvl": "6"},
    "6": {"clr": "cyan", "lvl": "7"},
    "7": {"clr": "blue", "lvl": "8"},
    "8": {"clr": "red", "lvl": "10"},
    "9": {"clr": "blue", "lvl": "9"},
    "10": {"clr": "red", "lvl": "11"},
    "11": {"clr": "red", "lvl": "12"},
    "12": {"clr": "green", "lvl": "Admin"},
    "13": {"clr": "white", "lvl": "2"},
    "14": {"clr": "white", "lvl": "3"},
}


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


def countt(x):
    print()
    for tcount in range(int(x), 0, -1):
        sys.stdout.write(f"\tWaiting for {tcount}   \r")
        sys.stdout.flush()
        time.sleep(1)


def gas2(id, tok):
    uri1 = f"https://wjxwd01mwyo.dt01showxx02.com/App/Live/RealTimePeopleList?live_id={id}&page=1"
    headers = {
        "User-Agent": f"HS-Android Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.17{random.randint(1000,9999)}.{random.randint(100,999)}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.{random.randint(1000,9999)}.{random.randint(100,999)} Mobile Safari/537.36",
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


while True:
    xd = gas2(idroom, tokenhost)
    db.truncate()
    for tt in xd:
        lvl = tt["vip"]
        aidi = tt["show_id"]
        nama = tt["nickname"]
        tex = f'    {sett[lvl]["lvl"]} "{aidi}" : ["{sett[lvl]["clr"]}","{nama}"],'
        if lvl != "1":
            print(c(sett[lvl]["clr"], tex, 0))
            if len(db.search(tbl["uid"] == aidi)) == 0:
                db.insert({"uid":  aidi})
    countt(5)
