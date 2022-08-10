import json
import os
import time
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


db["all"] = {
    "data": [],
    "player": 0,
    "banker": 0
}
for itr in data["results"]:
    idi = itr["game_number"]
    menit = int(idi[8::])
    hari = int(idi[6:8])
    bulan = int(idi[4:6])
    tahun = int(idi[:4])
    wday = dt.date(tahun, bulan, hari)
    wday = wday.strftime("%d %b %Y")
    wtime = getmenit(menit)

    isidata = {
        "id": idi,
        "waktu": wtime,
        "dadu": itr["cards"][0]
    }

    cplayer, cbanker = isidata["dadu"]["default"][0], isidata["dadu"]["default"][1]

    if cplayer > cbanker:
        db["all"]["player"] += 1
    else:
        db["all"]["banker"] += 1

    db["all"]["data"].append(isidata)

    try:
        db[wday]["data"].append(isidata)
        if cplayer > cbanker:
            db[wday]["player"] += 1
        else:
            db[wday]["banker"] += 1
    except:
        db[wday] = {
            "data": [],
            "player": 0,
            "banker": 0
        }
        db[wday]["data"].append(isidata)

# pindahin all ke paling belakang
dballbck = db["all"]
db.pop("all")
db["all"] = dballbck

print()
print(f" Total data : {len(data['results'])}")


while True:
    print()
    i = 0
    dthari = []
    for x in db:
        i += 1
        dthari.append(x)
        print(
            f"""{i}. {x}
        \tjumlah : {len(db[x]["data"])}
        \tplayer : {db[x]["player"]}
        \tbanker : {db[x]["banker"]}
        """
        )

    pil = input("input[all/nomor]:")

    cekdata = db[dthari[int(pil) - 1]]
    print(len(cekdata["data"]))
    for dataobj in cekdata["data"]:
        clrid = ["white", 0]
        clrpb = ["white", 0]
        clrpl = ["white", 0]
        clrba = ["white", 0]

        cplayer, cbanker = dataobj["dadu"]["default"][0], dataobj["dadu"]["default"][1]
        # print(dataobj)
        if cplayer > cbanker:
            clrpb[0] = "blue"
            clrpl[0] = "cyan"
        else:
            clrpb[0] = "red"
            clrba[0] = "red"

        print(
            f'\t|{c(clrid[0],dataobj["id"][8::],clrid[1])}\t{c(clrpl[0],cplayer,clrpl[1])}\t{c(clrba[0],cbanker,clrba[1])}\t{c(clrpb[0],"█",clrpb[1])}'
        )

        # time.sleep(0.2)

    if input("lagi? y/n :") == "n":
        break
