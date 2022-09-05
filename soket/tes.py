
from tinydb import *


from colorama import Fore, Style, init
init()
xla="16:04:10"
print(xla[:5])
input("")
exit()

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
disp=""
print()
tkk =sett.all()
tkk=(tkk[len(tkk)-1])


gamenum=c("yellow",tkk["gamenum"],0)
if tkk["pola"] == 1:
    pola=c("green","↑",0)
else:
    pola=c("red","↓",0)
big,small,odd,even,sbs,soe=c("red",tkk["big"],0),c("blue",tkk["small"],0),c("cyan",tkk["odd"],0),c("magenta",tkk["even"],0),c("black",tkk["selisihbs"],0),c("black",tkk["selisihoe"],0)
disp+=(f"\n  {gamenum} Big:{big} Small:{small} Odd:{odd} Even:{even}\t{pola}[{sbs}:{soe}]")

print(disp)