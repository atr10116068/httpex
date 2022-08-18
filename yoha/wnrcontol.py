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

    tz = pytz.timezone("Asia/Jakarta")
    now = datetime.now(tz)
    for tg in msg["data"]:
        rid = tg["phone_identifier"]
        rnum = tg["phone_number"]
        rmsg = tg["phone_message"]
        rwaktu = int(now.strftime("%M")) - \
            int(tg["created_at"].split("T")[1][3:5])
        rstat = tg["status"]
        if rwaktu > 15:
            wnrapi.cancel(API_KEY, rid)
        if rnum in vnum:
            if rstat != "Dibatalkan":
                print(
                    f'{c("green",rnum,0)}\t{c("green",rstat,0)} {c("yellow",f"{rwaktu} menit",0)}')
                if rmsg != None:
                    print(f'{c("cyan",rmsg,0)}')
                    code = rmsg.replace("Enter: ", "").split("\n")[0]
                    getapi.register(rnum, "t4ufiq654321", code)
                    tini.remove(where('nomer') == rnum)
                    print("================================")
            else:
                # Dibatalkan
                print(f'{c("red",rnum,0)}\t{c("red",rstat,0)}')
                tini.remove(where('nomer') == rnum)
    for rdd in range(20, 0, -1):
        sys.stdout.write(f"Wait.. {rdd}  \r")
        sys.stdout.flush()
        time.sleep(1)
