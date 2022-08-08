from tinydb import *
import time
import os
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

while True:
    try:
        os.system('cls')
        db = TinyDB("data.json")
        xs = db.all()
        xnum=10
        for x in xs:
            print(f'________[ {x["game"]} ]_______')
            for xxx in x["data"]:
                clr=""
                clrnum="green"
                num=x["data"][xxx]
                if xnum<num:
                    clrnum="red"
                    xnum=num
                else:
                    clrnum="grey"

                if "Big" in xxx:
                    clr="red"
                if "Small" in xxx:
                    clr="blue"
                if "Odd" in xxx:
                    clr="cyan"
                if "Even" in xxx:
                    clr="magenta"
                if "Any" in xxx:
                    clr="purple"
                print(f'{c(clr,xxx,0)}:{c(clrnum,num,0)}')
        time.sleep(0.3)
    except:
        print("error")
        time.sleep(1)
