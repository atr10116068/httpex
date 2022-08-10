import json, os
import datetime as dt
import colorama
from colorama import Fore, Style, Back

colorama.init()

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


def caribs(caripolabase):
    caripola = caripolabase[:-3].upper()  # input("9pola : ").upper()
    polacek = caripolabase[-3:].upper()
    jumpola = len(caripola)

    pola = {}
    bs__arai = []
    tampilkan = 0
    idx = 0
    for dataobj in data["results"][0:1440]:
        idx += 1
        bs = dataobj["tip"][1]
        if len(bs__arai) > int(jumpola) - 1:
            polanya = ""

            for tpola in bs__arai:
                polanya += tpola[:1]

            if polanya == caripola:
                tampilkan = 20
                idxcek = 0
                print(f"\n----------[data POLA mulai dari bawah garis]")
            if tampilkan != 0:
                tampilkan -= 1
                idi = dataobj["game_number"]
                menit = int(idi[8::])
                hari = int(idi[6:8])
                bulan = int(idi[4:6])
                tahun = int(idi[:4])
                wday = dt.date(tahun, bulan, hari)
                wday = wday.strftime("%d %b %Y")
                wtime = getmenit(menit)

                clrcek = "cyan"
                if idxcek < len(polacek):
                    if polacek[idxcek] == bs[:1]:
                        # print(f"pola : {polacek[idxcek]}")
                        clrcek = "green"
                    idxcek += 1
                print(f'{c(clrcek,bs,0)}\t{c("yellow",wday,0)} [{c("red",wtime,0)}]')

            try:
                pola[polanya][bs] += 1
            except:
                pola[polanya] = {"Big": 1, "Small": 1}
            bs__arai.pop(0)

        bs__arai.append(bs)

    # print()
    # print("\tData Pola")
    # for h in pola:
    #     print(f"{h} = {pola[h]}")

    # print()
    # print(f"\tData Pola {caripola}")
    poll = {"pola": "999", "predik": {"Big": 1, "Small": 1}}
    for h in pola:
        if h == caripola:
            poll = {"pola": h + polacek, "predik": pola[caripola]}
    print()
    print(poll)


def carioe(caripolabase):
    caripola = caripolabase[:-3].upper()  # input("9pola : ").upper()
    polacek = caripolabase[-3:].upper()
    jumpola = len(caripola)

    pola = {}
    bs__arai = []
    tampilkan = 0
    for dataobj in data["results"]:
        bs = dataobj["tip"][2]
        if len(bs__arai) > int(jumpola) - 1:
            polanya = ""

            for tpola in bs__arai:
                polanya += tpola[:1]

            if polanya == caripola:
                tampilkan = 20
                idxcek = 0
                print(f"\n----------[data POLA mulai dari bawah garis]")
            if tampilkan != 0:
                tampilkan -= 1
                idi = dataobj["game_number"]
                menit = int(idi[8::])
                hari = int(idi[6:8])
                bulan = int(idi[4:6])
                tahun = int(idi[:4])
                wday = dt.date(tahun, bulan, hari)
                wday = wday.strftime("%d %b %Y")
                wtime = getmenit(menit)

                clrcek = "cyan"
                if idxcek < len(polacek):
                    if polacek[idxcek] == bs[:1]:
                        # print(f"pola : {polacek[idxcek]}")
                        clrcek = "green"
                    idxcek += 1
                print(f'{c(clrcek,bs,0)}\t\t{c("yellow",wday,0)} [{c("red",wtime,0)}]')

            try:
                pola[polanya][bs] += 1
            except:
                pola[polanya] = {"Odd": 1, "Even": 1}
            bs__arai.pop(0)

        bs__arai.append(bs)

    # print()
    # print("\tData Pola")
    # for h in pola:
    #     print(f"{h} = {pola[h]}")

    # print()
    # print(f"\tData Pola {caripola}")
    poll = {"pola": "999", "predik": {"Odd": 1, "Even": 1}}
    for h in pola:
        if h == caripola:
            poll = {"pola": h, "predik": pola[caripola]}
    print()
    print(poll)


pill = input("pola bs atau oe:")
if pill.lower() not in ["bs", "oe"]:
    exit()
while True:
    if pill == "bs":
        caribs(input("cari pola bs: "))
    else:
        carioe(input("cari pola oe: "))
