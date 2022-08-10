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

    p = {
        'game': 'honglv_1',
        'game_number': '202203271169',
        'cards': [8],
        'cards_dic': {'default': ['8']},
        'win_key': ['danma_8'],
        'cards_status': 1,
        'tip': [],
        'next_round_game_number': '202203271170',
        'next_round_draw_at': 1648380600,
        'next_round_countdown': 58
    }
    wrna = {
        "0": "red",
        "1": "green",
        "2": "red",
        "3": "green",
        "4": "red",
        "5": "green",
        "6": "red",
        "7": "green",
        "8": "red",
        "9": "green",
    }
    janda = ["0", "5"]
    wink = str(dataobj["cards"][0])

    wday = c("magenta", wday, 0)
    server_time = c("white", server_time, 0)
    if wink in janda:
        # disp = f'\t{wday}[{server_time}]\t{c("magenta",wink,0)} {wrna[wink]}  '
        disp = f'  [{server_time}]   {c(wrna[wink],wink,0)} Purple(janda)  '    
    else:
        # disp = f'\t{wday}[{server_time}]\t{c(wrna[wink],wink,0)}  '
        disp = f'  [{server_time}]   {c(wrna[wink],wink,0)}  '
    return disp
