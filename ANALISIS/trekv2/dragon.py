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

    keyw = {
        "longhuhe_he": "Draw",
        "longhuhe_hu": "Tiger",
        "longhuhe_long": "Dragon",
        "longhuse_longhei": "B-Dra",
        "longhuse_longhong": "R-Dra",
        "longhuse_huhei": "B-Tig",
        "longhuse_huhong": "R-Tig",
    }
    dr = dataobj["cards_dic"]["default"][0]
    tg = dataobj["cards_dic"]["default"][1]
    wrd = dataobj["cards_dic"]["long"]
    wrt = dataobj["cards_dic"]["hu"]

    # warnain text
    if dr == tg:
        draw = c("green", "  DRAW", 0)
        dr = c("green", dr, 0)
        tg = c("green", dr, 0)

        wday = c("magenta", wday, 0)
        server_time = c("white", server_time, 0)
        disp = f'\t{wday}[{server_time}] {dr} {tg}\t{draw}  '
    elif int(dr) > int(tg):
        dr = c("blue", dr, 0)
    else:
        tg = c("red", tg, 0)

    kd, kt = "█", "█"
    warnakartu = {
        "H": "red",
        "D": "red",
        "S": "black",
        "C": "black",
    }
    kd = c(warnakartu[wrd[0]], kd, 0)
    kt = c(warnakartu[wrt[0]], kt, 0)

    wday = c("magenta", wday, 0)
    server_time = c("white", server_time, 0)
    # disp = f'\t{wday}[{server_time}]       {dr} {tg} \t{kd}{kt}'
    disp = f'  [{server_time}]   {dr} {tg} \t{kd}{kt}'

    return disp
