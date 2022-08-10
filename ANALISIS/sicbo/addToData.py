import json
import datetime as dt


def getmenit(x):
    return "{:02d}:{:02d}".format(*divmod(int(x), 60))


with open(f"sicbo.json", "r") as openfile:
    # Reading from json file
    data = json.load(openfile)

dat = {"hari": ""}
harian = []
namafile = ""
for itr in data["results"]:
    harian.append(itr)
    idi = itr["game_number"]
    menit = int(idi[8::])
    hari = int(idi[6:8])
    bulan = int(idi[4:6])
    tahun = int(idi[:4])
    wday = dt.date(tahun, bulan, hari)
    # print(f"{idi}")
    if dat["hari"] != wday:
        # print(f'\n>>>>>>>>>>>>>   {harian[0]["game_number"]}')
        dat["hari"] = wday
        wday = wday.strftime("%d %b %Y")

        print(f"{namafile} {idi} {len(harian)}")
        harian.pop(harian.index(itr))
        if len(harian) >= 1440:
            print(f"Save {namafile} ")
            # Writing to sample.json
            with open(f"datadadu/{namafile}.json", "w") as outfile:
                outfile.write(json.dumps({"results": harian}, indent=2))
        harian.clear()
        harian.append(itr)
    else:
        namafile = idi[:8]
