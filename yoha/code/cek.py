import ambil,getapi
from colorama import Fore,Style ,init
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

token=ambil.token()
def cekakun():
    x=1
    for tkn in token:
        acc=getapi.profile(tkn)
        if acc != 0:
            acc=acc["data"]
            print(f'{x}.\t{c("magenta",acc["id"],0)}\t{acc["user_nicename"]} {c("cyan",acc["diamonds"],0)} {c("yellow",acc["coin"],0)} ')
        x+=1

menus="""
1. cek akun
"""
while True:
    x=input(f"{menus}-> ")
    if x=="1":
        cekakun()