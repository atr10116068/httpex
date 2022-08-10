import json, os
import datetime as dt
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
    cx={
        "id":["YELLOW",0],
        "dadu":["WHITE",0]
    }
    aidi=t["game_number"][8::]
    dadu=f'{t["cards"][0]} {t["cards"][1]} {t["cards"][2]}'
    if t["cards"][0]==t["cards"][1] and t["cards"][1]==t["cards"][2]:
        cx["id"][1]=1
        cx["dadu"][1]=1


    cxaidi=c(cx["id"][0],aidi,cx["id"][1])
    cxdadu=c(cx["dadu"][0],dadu,cx["dadu"][1])
    print(f'\t{cxaidi} {cxdadu}')

    
data = {"results": []}

with open("sicbo.json", "r") as openfile:
		# Reading from json file
		datapp = json.load(openfile)

		for tyew in datapp["results"]:
				data["results"].append(tyew)

for t in data["results"]:
    disp(t)


print(data["results"][0])