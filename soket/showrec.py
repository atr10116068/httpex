from tinydb import *
import time,os
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


db = TinyDB("rec.json")
sett = db.table('data')
q = Query()
disp=""
bck=[]
while True:
    for tkk in sett:
        if tkk not in bck:
            os.system('cls')
            gamenum=c("yellow",tkk["gamenum"],0)
            if tkk["pola"] == 1:
                pola=c("green","↑",0)
            else:
                pola=c("red","↓",0)
            big,small,odd,even,sbs,soe=c("red",tkk["big"],0),c("blue",tkk["small"],0),c("cyan",tkk["odd"],0),c("magenta",tkk["even"],0),c("black",tkk["selisihbs"],0),c("black",tkk["selisihoe"],0)
            disp+=(f"\n  {gamenum} Big:{big} Small:{small} Odd:{odd} Even:{even}\t{pola}[{sbs}:{soe}]")
            bck.append(tkk)
            print(disp)
    time.sleep(1)
# find key
# result = sett.search(q.data == 'detik')[0]["gamenum"]
# print(result)


#update key
# sett.update_multiple([
#     ({'val': "turun"}, where('profile') == 'pola'),
#     ({'val': 8}, where('profile') == 'detik'),
#     ({'val': 0.2}, where('profile') == 'persenan'),
#     ({'val': 10}, where('profile') == 'maxbet'),
#     ])
