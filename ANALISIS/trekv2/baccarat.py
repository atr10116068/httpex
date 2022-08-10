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

    pb = "~"
    hsl = dataobj["cards_dic"]["default"]
    if hsl[0] > hsl[1]:
        pb = "p"
    else:
        pb = "b"
    if hsl[0] == hsl[1]:
        pb = "t"

    cp = dataobj["cards_dic"]["player"]
    cb = dataobj["cards_dic"]["banker"]

    # cari big or small
    if cp[2] == "0":
        cp.pop(2)
    if cb[2] == "0":
        cb.pop(2)
    bs = "small"
    if len(cp) != 2:
        bs = "big"
    if len(cb) != 2:
        bs = "big"

    ispair = "|   ~"
    wdh = []
    for pir in cb:
        if len(cb) == 3:
            cb.pop(2)
        if pir[1:] not in wdh:
            wdh.append(pir[1:])
        else:
            ispair = c("red", "| bpair", 1)
    wdh.clear()
    for pir in cp:
        if len(cp) == 3:
            cp.pop(2)
        if pir[1:] not in wdh:
            wdh.append(pir[1:])
        else:
            ispair = c("blue", "| ppair", 1)

    # warnain text
    if pb == "p":
        pb = c("blue", "   player", 0)
    elif pb == "b":
        pb = c("red", "   banker", 0)
    else:
        pb = c("magenta", "   tie   ", 0)
    if bs == "big":
        bs = c("red", "| "+bs, 0)
    else:
        bs = c("blue", "| "+bs, 0)
    wday = c("magenta", wday, 0)
    server_time = c("white", server_time, 0)

    # disp = f'  {wday}[{server_time}]{pb}\t{ispair}\t{bs}  '
    disp = f'  [{server_time}]{pb}\t{ispair}\t{bs}  '

    return(disp)
