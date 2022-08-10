import json
import time
import pytz
import sys
import datetime
import os
from datetime import datetime
import colorama
from colorama import Fore, Style, Back

colorama.init()

db = {}
setting = {"disp": 0}


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
    x = int(x)-60
    return "{:02d}:{:02d}".format(*divmod(int(x), 60))


def disp(t):
    cx = {
        "id": ["WHITE", 0],
        "pcards": ["WHITE", 0],
        "bcards": ["WHITE", 0],
        "ppair": ["WHITE", 0],
        "bpair": ["WHITE", 0],
    }
    aidi = t["game_number"][8::]
    cards = t["cards"][0]["default"]

    # H=HEart D=Diamond C=Keriting S=Sekop
    symb = {"S": "♠", "H": "♥", "C": "♣", "D": "♦"}
    cardsym = {"p": [], "b": []}
    disppcard = f"[{cards[0]}]"
    dispbcard = f"[{cards[1]}]"

    # ubah pake simbol
    for x in t["cards"][0]["player"]:
        if len(x) != 1:
            cardsym["p"].append(f"{symb[x[0]]}{x[1::]}")
    for x in t["cards"][0]["banker"]:
        if len(x) != 1:
            cardsym["b"].append(f"{symb[x[0]]}{x[1::]}")

    # masukin ke tampilan disp
    for t in cardsym:
        for i in t:
            tt = cardsym[i]
            for p in tt:
                if i == "p":
                    disppcard += f"{p} "
                elif i == "b":
                    dispbcard += f"{p} "

    bpair, ppair, tie = 0, 0, 0
    # cekpair
    tp = cardsym["p"]
    tb = cardsym["b"]
    try:
        if tp[0][1::] == tp[1][1::]:
            ppair += 1
        if tb[0][1::] == tb[1][1::]:
            bpair += 1

        if tp[1][1::] == tp[2][1::]:
            ppair += 1
        if tb[1][1::] == tb[2][1::]:
            bpair += 1
    except:
        pass

    cxbalok = ""
    cxpair = ""
    # add balok p dan b
    if cards[0] == cards[1]:
        cxbalok += c("GREEN", "█", 0)
        cx["id"][0] = "GREEN"
        cx["pcards"][0] = "GREEN"
        cx["bcards"][0] = "GREEN"
    elif cards[0] > cards[1]:
        cxbalok += c("BLUE", "█", 0)
        cx["pcards"][0] = "BLUE"
        cx["id"][0] = "BLUE"
    else:
        cx["id"][0] = "RED"
        cx["bcards"][0] = "RED"
        cxbalok += c("RED", "█", 0)

    if cards[0] == cards[1]:
        cxpair += f'{c("GREEN", "  << TIE >>", 0)}'
    elif ppair > 0:
        cx["ppair"][0] = "BLUE"
        cxpair += f'{c("BLUE", "  << PAIR >>", 0)}'
    elif bpair > 0:
        cx["bpair"][0] = "RED"
        cxpair += f'{c("RED", "  << PAIR >>", 0)}'
    else:
        cxpair += f'\t'

    cxpcard = c(cx["pcards"][0], disppcard, cx["pcards"][1])
    cxbcard = c(cx["bcards"][0], dispbcard, cx["bcards"][1])

    cxaidi = c(cx["id"][0], getmenit(aidi), cx["id"][1])

    if len(cxpcard) > 20:
        print(f'[{cxaidi}]{cxpair}\t{cxbalok} {cxpcard}\t{cxbcard}')
    else:
        print(f'[{cxaidi}]{cxpair}\t{cxbalok} {cxpcard}\t\t{cxbcard}')


class Watcher(object):
    running = True
    refresh_delay_secs = 1

    # Constructor
    def __init__(self, watch_file, call_func_on_change=None, *args, **kwargs):
        self._cached_stamp = 0
        self.filename = watch_file
        self.call_func_on_change = call_func_on_change
        self.args = args
        self.kwargs = kwargs

    # Look for changes
    def look(self):
        stamp = os.stat(self.filename).st_mtime
        if stamp != self._cached_stamp:
            self._cached_stamp = stamp
            # File has changed, so do something...
            # print('File changed')
            if self.call_func_on_change is not None:
                self.call_func_on_change(*self.args, **self.kwargs)

    # Keep watching in a loop
    def watch(self):
        while self.running:
            try:
                # Look for changes
                time.sleep(self.refresh_delay_secs)
                self.look()
            except KeyboardInterrupt:
                print('\nDone')
                break
            except FileNotFoundError:
                # Action on file not found
                pass
            except:
                print('Unhandled error: %s' % sys.exc_info()[0])

# Call this function each time a change happens


def custom_action():
    if setting["disp"] == 0:
        os.system("clear")

    try:
        data = {"results": []}

        with open("bacarat.json", "r") as openfile:
            # Reading from json file
            datapp = json.load(openfile)

            for tyew in datapp["results"]:
                data["results"].append(tyew)

        # switcher print or write
        if setting["disp"] == 0:
            for t in data["results"][len(data["results"])-19:len(data["results"])]:
                disp(t)
            setting["disp"] = 1
        else:
            disp(data["results"][len(data["results"])-1])

        dat = {"menit": ""}

        tz = pytz.timezone("Asia/Jakarta")
        now = datetime.now(tz)
        dat["jam"] = now.strftime("%d%b%Y-%H:%M:%S")
        menit = now.strftime("%M")
        dat["menit"] = int(menit)
    except Exception as e:
        time.sleep(1)
        pass
        # print(str(e))


watch_file = 'bacarat.json'

# watcher = Watcher(watch_file)  # simple
# also call custom action function
watcher = Watcher(watch_file, custom_action)
watcher.watch()  # start

# while True:

#     if int(menit) != dat["menit"]:
#         time.sleep(6)
#         dat["menit"] = int(menit)
#         with open("bacarat.json", "r") as openfile:
#             # Reading from json file
#             datapp = json.load(openfile)
#         databaru = []
#         for t in datapp["results"]:
#             databaru.append(t)
#         databaru.reverse()
#         apdet = databaru[0]
#         data["results"].append(apdet)
#         disp(apdet)
