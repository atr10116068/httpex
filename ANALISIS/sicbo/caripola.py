import json, os


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


def caribs(caripola):
    caripola = caripola.upper()  # input("9pola : ").upper()
    jumpola = len(caripola)

    pola = {}
    bs__arai = []
    tampilkan = 0
    for dataobj in data["results"]:
        bs = dataobj["tip"][1]
        if len(bs__arai) > int(jumpola) - 1:
            polanya = ""

            for tpola in bs__arai:
                polanya += tpola[:1]

            if polanya == caripola:
                tampilkan = 20
                # print(f"\n----------[POLA mulai dari bawah garis]")
            if tampilkan != 0:
                tampilkan -= 1
                # print(f"{bs}\t\t---{tampilkan}")

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
            poll = {"pola": h, "predik": pola[caripola]}
    return poll


def carioe(caripola):
    caripola = caripola.upper()  # input("9pola : ").upper()
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
                # print(f"\n----------[POLA mulai dari bawah garis]")
            if tampilkan != 0:
                tampilkan -= 1
                # print(f"{bs}\t\t---{tampilkan}")

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
    return poll

