import json
import sys


def cek():
    with open("sicbo.json", "r") as openfile:
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
    idxiterasi = 0
    print(f'id dimulai dari {int(data["results"][0]["game_number"][8:])}')
    idxid = int(data["results"][0]["game_number"][8:]) - 1

    for ppp in range(len(idfilt)):
        dd = idfilt[ppp]
        aidi = int(dd[8::])
        if idxid == 1440:
            idxid = 0
        idxid += 1
        idxiterasi += 1
        # if idxiterasi>9280:
        # print(f"{dd}[{aidi}] {idxid}")
        if aidi != idxid:
            print(f"  break in iteration {idxiterasi}")
            print(f"  kesalahan...!  {dd}[{aidi}] harusnya {idxid}\n")
            exit()


x = cek()
