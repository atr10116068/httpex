import os, json
import caripolafull as cpf

import colorama
from colorama import Fore, Style, Back

colorama.init()


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


pat = os.getcwd()

with open(pat + "/bck/20211223.json", "r") as openfile:
    datapp = json.load(openfile)

polabs = ""
polaoe = ""
lenpola = 3
itr = 1

prediknya = {"bs": "", "oe": ""}
data = {"bswin": 0, "bslose": 0, "oewin": 0, "oelose": 0}

for tp in datapp["results"]:
    # if itr > 15:
    #     exit()
    # else:
    #     itr += 1
    itr += 1

    print("----------------------------------------------------------")
    warna = ["white", "white", "white", "white"]
    if len(prediknya["bs"]) != 0:
        if prediknya["bs"] == tp["tip"][1]:
            warna[0] = "green"
            data["bswin"] += 1
            # print(
            #     f'prediksi {c("green",prediknya["bs"],0)}  -> {c("green",tp["tip"][1],0)}'
            # )
        else:
            warna[1] = "red"
            data["bslose"] += 1
            # print(
            #     f'prediksi {c("red",prediknya["bs"],0)}  -> {c("red",tp["tip"][1],0)}'
            # )
    if len(prediknya["oe"]) != 0:
        if prediknya["oe"] == tp["tip"][2]:
            warna[2] = "green"
            data["oewin"] += 1
            # print(
            #     f'prediksi {c("green",prediknya["oe"],0)}  -> {c("green",tp["tip"][2],0)}'
            # )
        else:
            warna[3] = "red"
            data["oelose"] += 1
            # print(
            #     f'prediksi {c("red",prediknya["oe"],0)}  -> {c("red",tp["tip"][2],0)}'
            # )
    itt = 0
    for pu in data:
        print(f"{pu}\t{c(warna[itt],data[pu],0)}")
        itt += 1

    prediknya["bs"] = ""
    prediknya["oe"] = ""

    if len(polabs) > lenpola:
        polabs = polabs[1:]
        polaoe = polaoe[1:]
        polabs += tp["tip"][1][:1]
        polaoe += tp["tip"][2][:1]
    else:
        polabs += tp["tip"][1][:1]
        polaoe += tp["tip"][2][:1]

    if len(polabs) > lenpola:

        print()
        print(f"{polabs}\t {itr}")
        print(polaoe)
        algo = cpf.cari([polabs, polaoe])
        pr = algo["predik"]
        # print(pr)
        if pr["Big"] - pr["Small"] != 0:
            if pr["Big"] > pr["Small"]:
                prediknya["bs"] = "Big"
            elif pr["Big"] < pr["Small"]:
                prediknya["bs"] = "Small"

        if pr["Odd"] - pr["Even"] != 0:
            if pr["Odd"] > pr["Even"]:
                prediknya["oe"] = "Odd"
            elif pr["Odd"] < pr["Even"]:
                prediknya["oe"] = "Even"

        # print()
        # print(json.dumps(prediknya, indent=2))

        # print()
