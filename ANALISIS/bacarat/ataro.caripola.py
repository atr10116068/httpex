import json
import os
import datetime as dt
import colorama
from colorama import Fore, Style, Back
colorama.init()

print()
print("""
Fix : 
-Support Player (p)
-Support Banker (b)
-Support Tie (t)
""")
print()


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


data = {"results": []}


pat = os.getcwd()
pat = pat + "/datadadu/"

listfile = []
x = [f.name for f in os.scandir(pat) if f.is_file()]
with os.scandir(pat) as i:
    for entry in i:
        if entry.is_file():
            listfile.append(entry.name)

for fn in listfile:
    with open(pat + fn, "r") as openfile:
        # Reading from json file
        datapp = json.load(openfile)

        for tyew in datapp["results"]:
            data["results"].append(tyew)


def getmenit(x):
    return "{:02d}:{:02d}".format(*divmod(int(x), 60))


def caripb(caripola):
    caripola = caripola.upper()  # input("9pola : ").upper()
    jumpola = len(caripola)

    pola = {}
    bs__arai = []
    tampilkan = 0

    for dataobj in data["results"]:
        idi = dataobj["game_number"]
        menit = int(idi[8::])
        hari = int(idi[6:8])
        bulan = int(idi[4:6])
        tahun = int(idi[:4])
        wday = dt.date(tahun, bulan, hari)
        wday = wday.strftime("%d %b %Y")
        wtime = getmenit(menit)

        cp = dataobj["cards_dic"]["default"][0]
        cb = dataobj["cards_dic"]["default"][1]

        if cp == cb:
            bs = "T"
        elif cp > cb:
            bs = "P"
        else:
            bs = "B"
        if len(bs__arai) > int(jumpola) - 1:
            polanya = ""

            for tpola in bs__arai:
                polanya += tpola[:1]

            if polanya == caripola:
                tampilkan = 15
                print(
                    f"\n--[{c('yellow',polanya,0)}]--[{c('green',wday,0)} {c('magenta',wtime,0)}]")
            if tampilkan != 0:
                tampilkan -= 1
                if bs == "P":
                    print(f"\t{c('blue',bs,0)}")
                elif bs == "B":
                    print(f"\t{c('red',bs,0)}")
                else:
                    print(f"\t{c('green',bs,0)}")

            try:
                pola[polanya][bs] += 1
            except:
                pola[polanya] = {"P": 1, "B": 1, "T": 1}
            bs__arai.pop(0)
        bs__arai.append(bs)

    # print()
    # print("\tData Pola")
    # for h in pola:
    #     print(f"{h} = {pola[h]}")

    print()
    print(f"\tData Pola {caripola}")
    poll = {"pola": "999", "predik": {"P": 1, "B": 1, "T": 1}}
    for h in pola:
        if h == caripola:
            poll = {"pola": h, "predik": pola[caripola]}

    # print(data["results"][0])
    return poll


while True:
    print(f"\t\t{c('red','~ ATΛRO x Hanzo ~',1)}")
    print(caripb(input("pola pb : ")))
    print()
