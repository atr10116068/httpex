import json
import datetime as dt
from colorama import Fore, Style, init
init()


def c(colr, tex, dim):
    try:
        w = {
            "RED": Fore.RED,
            "GREEN": Fore.GREEN,
            "YELLOW": Fore.YELLOW,
            "BLUE": Fore.BLUE,
            "MAGENTA": Fore.MAGENTA,
            "CYAN": Fore.CYAN,

            "BLACK": Fore.BLACK,
            "WHITE": Fore.WHITE,
            "RESET": Fore.RESET,
        }
        if dim == 1:
            return f"{Style.DIM}{w[colr.upper()]}{tex}{Style.RESET_ALL}"
        else:
            return f"{w[colr.upper()]}{tex}{Style.RESET_ALL}"
    except:
        return tex


def p(dataobj):
    idi = dataobj["game_number"]
    aidi = idi[8:]
    hari = int(idi[6:8])
    bulan = int(idi[4:6])
    tahun = int(idi[:4])
    wday = dt.date(tahun, bulan, hari)
    wday = wday.strftime("%d %b %Y")
    minut = int(idi[8:])*60
    minut = minut-(60*60)
    server_time = str(dt.timedelta(seconds=minut))[0:5]
    if server_time[4:5] == ":":
        server_time = server_time[0:4]

    # print(json.dumps(dataobj, indent=2))
    card = f'  {dataobj["cards_dic"]["default"][0]} {dataobj["cards_dic"]["default"][1]} {dataobj["cards_dic"]["default"][2]}'
    bs = dataobj["tip"][1]
    oe = dataobj["tip"][2]

    # warnain text
    if bs == "Big":
        bs = c("red", bs+"  ", 0)
    else:
        bs = c("cyan", bs, 0)
    if oe == "Odd":
        oe = c("blue", oe+" ", 0)
    else:
        oe = c("yellow", oe, 0)
    wday = c("magenta", wday, 0)
    server_time = c("white", server_time, 0)
    if dataobj["cards_dic"]["default"][0] == dataobj["cards_dic"]["default"][1] and dataobj["cards_dic"]["default"][1] == dataobj["cards_dic"]["default"][2]:
        # if dat["smsg"] == True:
        #     sendmsg(
        #         f'Cukup Aniiiii.... {dataobj["cards"][0]}{dataobj["cards"][0]}{dataobj["cards"][0]}')
        any = c("green", "ANY TRIPLE", 0)
        disp = f'  [{server_time}] {card}\t{any}  '
    else:
        disp = f'  [{server_time}] {card}\t{bs} {oe}  '
    return disp
