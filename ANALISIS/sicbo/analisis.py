import json, os
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
    "big": 0,
    "small": 0,
    "odd": 0,
    "even": 0,
    "be": 0,
    "bo": 0,
    "se": 0,
    "so": 0,
    "triple": 0,
    "anytime": [],
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
        "dadu": itr["cards"],
        "tip": itr["tip"],
        "any": "no",
    }

    if isidata["tip"][1] == "Big":
        db["all"]["big"] += 1
        if isidata["tip"][2] == "Even":
            db["all"]["be"] += 1
        else:
            db["all"]["bo"] += 1
    else:
        db["all"]["small"] += 1
        if isidata["tip"][2] == "Even":
            db["all"]["se"] += 1
        else:
            db["all"]["so"] += 1
    if isidata["tip"][2] == "Odd":
        db["all"]["odd"] += 1
    else:
        db["all"]["even"] += 1
    if (
        isidata["dadu"][0] == isidata["dadu"][1]
        and isidata["dadu"][1] == isidata["dadu"][2]
    ):
        db["all"]["triple"] += 1
        isidata["any"] = "yes"
    db["all"]["data"].append(isidata)

    try:
        db[wday]["data"].append(isidata)
        if isidata["tip"][1] == "Big":
            db[wday]["big"] += 1
            if isidata["tip"][2] == "Even":
                db[wday]["be"] += 1
            else:
                db[wday]["bo"] += 1
        else:
            db[wday]["small"] += 1
            if isidata["tip"][2] == "Even":
                db[wday]["se"] += 1
            else:
                db[wday]["so"] += 1
        if isidata["tip"][2] == "Odd":
            db[wday]["odd"] += 1
        else:
            db[wday]["even"] += 1
        if (
            isidata["dadu"][0] == isidata["dadu"][1]
            and isidata["dadu"][1] == isidata["dadu"][2]
        ):
            db[wday]["triple"] += 1
            isidata["any"] = "yes"
            db[wday]["anytime"].append(str(getmenit(menit)))
    except:
        db[wday] = {
            "data": [],
            "big": 0,
            "small": 0,
            "odd": 0,
            "even": 0,
            "be": 0,
            "bo": 0,
            "se": 0,
            "so": 0,
            "triple": 0,
            "anytime": [],
        }
        db[wday]["data"].append(isidata)

# pindahin all ke paling belakang
dballbck = db["all"]
db.pop("all")
db["all"] = dballbck

print()
print(f" Total data : {len(data['results'])}")


# tiap tumpuk 3 ganti mode
def algohanzo1(bs):
    # print(json.dumps(hanzo1, indent=2))
    gantimode = 0
    if hanzo1["modeon"] == False:
        if hanzo1["caripola"] == "null":
            hanzo1["caripola"] = bs
        if bs == hanzo1["caripola"]:
            hanzo1["tumpuk"] += 1
            if hanzo1["tumpuk"] > 0:
                hanzo1["modeon"] = True
                hanzo1["tumpuk"] = 0
                hanzo1["mode"] = bs
            return [1, 0]
        else:
            hanzo1["caripola"] = bs
            hanzo1["tumpuk"] = 0
            return [1, 0]
    else:
        if bs == hanzo1["mode"]:
            hanzo1["tumpuk"] = 0
            return [1, 0]
        else:
            hanzo1["tumpuk"] += 1
            if hanzo1["tumpuk"] > 0:
                hanzo1["modeon"] = True
                return [0, 1]
            return [0, gantimode]


# tiap tumpuk 3 ganti mode


def algoduadua(bs):
    # print(json.dumps(hanzo1, indent=2))
    gantimode = 0
    if duadua["modeon"] == False:
        if duadua["caripola"] == "null":
            duadua["caripola"] = bs
        if bs == duadua["caripola"]:
            duadua["tumpuk"] += 1
            if duadua["tumpuk"] > 1:
                duadua["modeon"] = True
                duadua["tumpuk"] = 0
                duadua["mode"] = bs
            return [1, 0]
        else:
            duadua["caripola"] = bs
            duadua["tumpuk"] = 0
            return [1, 0]
    else:
        if bs == duadua["mode"]:
            duadua["tumpuk"] = 0
            return [1, 0]
        else:
            duadua["tumpuk"] += 1
            if duadua["tumpuk"] > 1:
                duadua["modeon"] = True
                return [0, 1]
            return [0, gantimode]


def algotigatiga(bs):
    # print(json.dumps(hanzo1, indent=2))
    gantimode = 0
    if tigatiga["modeon"] == False:
        if tigatiga["caripola"] == "null":
            tigatiga["caripola"] = bs
        if bs == tigatiga["caripola"]:
            tigatiga["tumpuk"] += 1
            if tigatiga["tumpuk"] > 2:
                tigatiga["modeon"] = True
                tigatiga["tumpuk"] = 0
                tigatiga["mode"] = bs
            return [1, 0]
        else:
            tigatiga["caripola"] = bs
            tigatiga["tumpuk"] = 0
            return [1, 0]
    else:
        if bs == tigatiga["mode"]:
            tigatiga["tumpuk"] = 0
            return [1, 0]
        else:
            tigatiga["tumpuk"] += 1
            if tigatiga["tumpuk"] > 2:
                tigatiga["modeon"] = True
                return [0, 1]
            return [0, gantimode]


def algoempatempat(bs):
    # print(json.dumps(hanzo1, indent=2))
    gantimode = 0
    if empatempat["modeon"] == False:
        if empatempat["caripola"] == "null":
            empatempat["caripola"] = bs
        if bs == empatempat["caripola"]:
            empatempat["tumpuk"] += 1
            if empatempat["tumpuk"] > 3:
                empatempat["modeon"] = True
                empatempat["tumpuk"] = 0
                empatempat["mode"] = bs
            return [1, 0]
        else:
            empatempat["caripola"] = bs
            empatempat["tumpuk"] = 0
            return [1, 0]
    else:
        if bs == empatempat["mode"]:
            empatempat["tumpuk"] = 0
            return [1, 0]
        else:
            empatempat["tumpuk"] += 1
            if empatempat["tumpuk"] > 3:
                empatempat["modeon"] = True
                return [0, 1]
            return [0, gantimode]


while True:
    hanzo1 = {
        "caripola": "null",
        "clrwin": ["black", 0],
        "modeon": False,
        "mode": "null",
        "tumpuk": 0,
        "win": 0,
        "lose": 0,
    }
    duadua = {
        "caripola": "null",
        "clrwin": ["black", 0],
        "modeon": False,
        "mode": "null",
        "tumpuk": 0,
        "win": 0,
        "lose": 0,
    }
    tigatiga = {
        "caripola": "null",
        "clrwin": ["black", 0],
        "modeon": False,
        "mode": "null",
        "tumpuk": 0,
        "win": 0,
        "lose": 0,
    }
    empatempat = {
        "caripola": "null",
        "clrwin": ["black", 0],
        "modeon": False,
        "mode": "null",
        "tumpuk": 0,
        "win": 0,
        "lose": 0,
    }

    print()
    i = 0
    dthari = []
    for x in db:
        i += 1
        dthari.append(x)
        print(
            f"""{i}. {x}
        \tjumlah : {len(db[x]["data"])}
        \tBig    : {db[x]["big"]}
        \tSmall  : {db[x]["small"]}
        \tOdd    : {db[x]["odd"]}
        \tEven   : {db[x]["even"]}
        \tBE     : {db[x]["be"]}
        \tBO     : {db[x]["bo"]}
        \tSE     : {db[x]["se"]}
        \tSO     : {db[x]["so"]}
        \tTriple : {db[x]["triple"]}
        """
        )

        dispanytime = ""
        switcherjam = 0
        for ty in db[x]["anytime"]:
            if int(ty[1]) == switcherjam:
                dispanytime += f"\t{ty}"
            else:
                switcherjam = int(ty[1])
                dispanytime += f"\n\t{ty}"
        print(dispanytime)

    pil = input("input[all/nomor]:")

    cekdata = db[dthari[int(pil) - 1]]
    print(len(cekdata["data"]))
    for dataobj in cekdata["data"]:
        clrid = ["cyan", 0]
        clrbs = ["white", 0]
        clroe = ["white", 0]
        clrany = ["black", 0]
        hanzo1["clrwin"] = ["black", 0]
        duadua["clrwin"] = ["black", 0]
        tigatiga["clrwin"] = ["black", 0]
        empatempat["clrwin"] = ["black", 0]

        if dataobj["any"] == "yes":
            clrany[0] = "red"
            clrany[1] = 1
            clrid[1] = 1
            clrbs[1] = 1
            clroe[1] = 1
        if dataobj["tip"][1] == "Big":
            clrbs[0] = "red"
        else:
            clrbs[0] = "yellow"
        if dataobj["tip"][2] == "Odd":
            clroe[0] = "magenta"
        else:
            clroe[0] = "blue"

        gethanzo1 = algohanzo1(dataobj["tip"][1])
        if hanzo1["modeon"] == True:
            if gethanzo1[0] == 1:
                hanzo1["clrwin"][0] = "green"
                hanzo1["win"] += 1
            else:
                hanzo1["lose"] += 1
        getduadua = algoduadua(dataobj["tip"][1])
        if duadua["modeon"] == True:
            if getduadua[0] == 1:
                duadua["clrwin"][0] = "green"
                duadua["win"] += 1
            else:
                duadua["lose"] += 1
        gettigatiga = algotigatiga(dataobj["tip"][1])
        if tigatiga["modeon"] == True:
            if gettigatiga[0] == 1:
                tigatiga["clrwin"][0] = "green"
                tigatiga["win"] += 1
            else:
                tigatiga["lose"] += 1
        getempatempat = algoempatempat(dataobj["tip"][1])
        if empatempat["modeon"] == True:
            if getempatempat[0] == 1:
                empatempat["clrwin"][0] = "green"
                empatempat["win"] += 1
            else:
                empatempat["lose"] += 1

        if dataobj["any"] == "yes":
            print(
                f'\t|{c(clrid[0],dataobj["id"][8::],clrid[1])}\t{c(clrbs[0],dataobj["tip"][1],clrbs[1])}\t{c(clroe[0],dataobj["tip"][2],clroe[1])}\t{dataobj["dadu"][0]} {dataobj["dadu"][1]} {dataobj["dadu"][2]}\t{c(clrany[0],dataobj["any"],clrany[1])}\t{c(clrany[0],getmenit(dataobj["id"][8::]),clrany[1])}\t|{c(hanzo1["clrwin"][0],"█",hanzo1["clrwin"][1])}Pola1:{hanzo1["mode"]}\t{c(duadua["clrwin"][0],"█",duadua["clrwin"][1])}Pola2:{duadua["mode"]}\t{c(tigatiga["clrwin"][0],"█",tigatiga["clrwin"][1])}Pola3:{tigatiga["mode"]}\t{c(empatempat["clrwin"][0],"█",empatempat["clrwin"][1])}Pola4:{empatempat["mode"]}'
            )
        else:
            print(
                f'\t|{c(clrid[0],dataobj["id"][8::],clrid[1])}\t{c(clrbs[0],dataobj["tip"][1],clrbs[1])}\t{c(clroe[0],dataobj["tip"][2],clroe[1])}\t   \t{c(clrany[0],dataobj["any"],clrany[1])}\t{c(clrany[0],getmenit(dataobj["id"][8::]),clrany[1])}\t|{c(hanzo1["clrwin"][0],"█",hanzo1["clrwin"][1])}Pola1:{hanzo1["mode"]}\t{c(duadua["clrwin"][0],"█",duadua["clrwin"][1])}Pola2:{duadua["mode"]}\t{c(tigatiga["clrwin"][0],"█",tigatiga["clrwin"][1])}Pola3:{tigatiga["mode"]}\t{c(empatempat["clrwin"][0],"█",empatempat["clrwin"][1])}Pola4:{empatempat["mode"]}'
            )

        if gethanzo1[1] == 1:
            if hanzo1["mode"] == "Big":
                hanzo1["mode"] = "Small"
            else:
                hanzo1["mode"] = "Big"
            hanzo1["tumpuk"] = 0
        if getduadua[1] == 1:
            if duadua["mode"] == "Big":
                duadua["mode"] = "Small"
            else:
                duadua["mode"] = "Big"
            duadua["tumpuk"] = 0
        if gettigatiga[1] == 1:
            if tigatiga["mode"] == "Big":
                tigatiga["mode"] = "Small"
            else:
                tigatiga["mode"] = "Big"
            tigatiga["tumpuk"] = 0
        if getempatempat[1] == 1:
            if empatempat["mode"] == "Big":
                empatempat["mode"] = "Small"
            else:
                empatempat["mode"] = "Big"
            empatempat["tumpuk"] = 0
        # time.sleep(0.2)
    print(f"algoritma satusatu  : {hanzo1['win']} Win dan {hanzo1['lose']} Lose")
    print(f"algoritma duadua : {duadua['win']} Win dan {duadua ['lose']} Lose")
    print(f"algoritma tigatiga : {tigatiga['win']} Win dan {tigatiga ['lose']} Lose")
    print(
        f"algoritma empatempat : {empatempat['win']} Win dan {empatempat ['lose']} Lose"
    )

    if input("lagi? y/n :") == "n":
        break
