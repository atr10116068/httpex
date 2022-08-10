import json, os
import datetime as dt


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


def cari(caripola):
    caripolabs = caripola[0].upper()  # input("9pola : ").upper()
    caripolaoe = caripola[1].upper()  # input("9pola : ").upper()
    jumpola = len(caripolabs)

    pola = {}
    bs__arai = []
    oe__arai = []
    tampilkan = 0
    for dataobj in data["results"]:
        bs = dataobj["tip"][1]
        oe = dataobj["tip"][2]
        idi = dataobj["game_number"]
        hari = int(idi[6:8])
        bulan = int(idi[4:6])
        tahun = int(idi[:4])
        wday = dt.date(tahun, bulan, hari)
        wday = wday.strftime("%d %b %Y")
        # print()
        if len(bs__arai) > int(jumpola) - 1:
            polabs = ""
            polaoe = ""
            filthari = []

            for tpola in bs__arai:
                polabs += tpola[:1]
            for tpola in oe__arai:
                polaoe += tpola[:1]

            filthari.append(wday)
            if polabs == caripolabs:
                if polaoe == caripolaoe:
                    # print(filthari)
                    tampilkan = 20
                    # print(f"\n----------[POLA mulai dari bawah garis]")
                    # print()
                    # print(f"{bs}")
                    # print(f"{oe}")
                    # print(f"{polabs} ->  {caripolabs} = {bs}")
                    # print(f"{polaoe} ->  {caripolaoe} = {oe}")

                    try:
                        pola[polabs + polaoe][bs] += 1
                        pola[polabs + polaoe][oe] += 1
                    except:
                        pola[polabs + polaoe] = {
                            "Big": 1,
                            "Small": 1,
                            "Odd": 1,
                            "Even": 1,
                        }
                        pola[polabs + polaoe][bs] += 1
                        pola[polabs + polaoe][oe] += 1

            if tampilkan != 0:
                tampilkan -= 1
                # print(f"{bs}\t{oe}\t{wday}\t{tampilkan}")
            bs__arai.pop(0)
            oe__arai.pop(0)

        bs__arai.append(bs)
        oe__arai.append(oe)

    poll = {"pola": "999", "predik": {"Big": 1, "Small": 1, "Odd": 1, "Even": 1}}
    for h in pola:
        if h == caripola[0].upper() + caripola[1].upper():
            poll = {"pola": h, "predik": pola[h]}
    return poll

