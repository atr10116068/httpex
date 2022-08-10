import json
import os

pat = os.getcwd()
pat = pat + "/datadadu/"

listfile = []
x = [f.name for f in os.scandir(pat) if f.is_file()]
with os.scandir(pat) as i:
    for entry in i:
        if entry.is_file():
            listfile.append(entry.name)


def cek(fn):
    with open(pat + fn, "r") as openfile:
        # Reading from json file
        data = json.load(openfile)

    datafilt = []
    idfilt = []
    for x in data["results"]:
        aidi = x["game_number"]
        if aidi not in idfilt:
            idfilt.append(aidi)
            datafilt.append(x)
        else:
            print(f"id {aidi} sama")

    for p in range(len(idfilt)):
        if p + 1 != int(idfilt[p][8::]):
            print(f"{fn} => {idfilt[p][8::]} Hilang")


for fn in listfile:
    cek(fn)
