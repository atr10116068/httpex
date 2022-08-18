import wnrapi
import time
import getapi
from datetime import datetime
import pytz
import time
import sys
from tinydb import *

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


API_KEY = "bb70dfdd-bc0b-5066-a985-66dbed98ad3a"

while True:
    msg = wnrapi.otp(API_KEY)
    tini = TinyDB("wnrotp.json")
    tbl = tini.all()
    vnum = []
    for gh in tbl:
        vnum.append(gh["nomer"])
    print(c("magenta", str(vnum), 0))

    for tg in msg["data"]:
        rnum = tg["phone_number"]
        rmsg = tg["phone_message"]
        rstat = tg["status"]
        if rnum in vnum:
            print(f'{c("green",rnum,0)}\t{c("green",rstat,0)}\n{c("cyan",rmsg,0)}')
            if rmsg != None:
                code = rmsg.replace("Enter: ", "").split("\n")[0]
                getapi.register(rnum, "t4ufiq654321", code)
                tini.remove(where('nomer') == rnum)
                print("================================")
        # else:
        #     print(f"{rnum}\t{rstat}")
    time.sleep(10)
