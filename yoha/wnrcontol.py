import wnrapi
import time
import getapi,ambil
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
        
    dispjum=f"••••••••>>   jumlah : {len(ambil.uid())}"
    print(c("magenta", f"{dispjum}", 0))
    # print(c("magenta", f"{str(vnum)}", 0))

    try:
        for tg in msg["data"]:
            rid = tg["phone_identifier"]
            rnum = tg["phone_number"]
            rmsg = tg["phone_message"]
            
            tz = pytz.timezone("Asia/Jakarta")
            now = datetime.now(tz)
            rwaktu = int(now.strftime("%M")) - \
                int(tg["created_at"].split("T")[1][3:5])
            #jika menit minus maka tambahin 60
            if rwaktu<0:
                rwaktu=int(now.strftime("%M"))+60 - int(tg["created_at"].split("T")[1][3:5])
            rstat = tg["status"]
            if rnum in vnum:
                if rstat != "Dibatalkan":
                    if rwaktu >=15:
                        wnrapi.cancel(API_KEY, rid)

                    print(
                        f'{c("green",rnum,0)}\t{c("green",rstat,0)} {c("yellow",f"{rwaktu} menit",0)}')
                    if rmsg != None:
                        print(f'{c("cyan",rmsg,0)}')
                        code = rmsg.replace("Enter: ", "").split("\n")[0]
                        print(f" code = [{code}]")
                        tesdaptar=(getapi.register(rnum, "t4ufiq654321", code))
                        if tesdaptar["message"]!="Kesalahan kode verifikasi":
                            for rdd in range(10, 0, -1):
                                sys.stdout.write(f"Wait.. to Login  {rdd}  \r")
                                sys.stdout.flush()
                                time.sleep(1)

                            tkn = getapi.login(rnum, "t4ufiq654321")
                            getapi.claim(tkn, 1)

                            tini.remove(where('nomer') == rnum)
                        else:
                            print(f"Gagal daftar : {rnum}")
                            if input("hapus ? :") == "y":
                                tini.remove(where('nomer') == rnum)
                else:
                    # Dibatalkan
                    print(f'{c("red",rnum,0)}\t{c("red",rstat,0)}')
                    tini.remove(where('nomer') == rnum)
    except:
        pass
    for rdd in range(50, 0, -1):
        sys.stdout.write(f"Wait.. {rdd}  \r")
        sys.stdout.flush()
        time.sleep(1)
