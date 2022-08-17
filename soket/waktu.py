from datetime import datetime
import pytz,time,sys
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


while True:
    tz = pytz.timezone("Asia/Jakarta")
    now = datetime.now(tz)
    xx=now.strftime("%d%b%Y-%H:%M:%S")
    detik=int(now.strftime("%S"))
    disp=f' #####################\n #       {c("cyan",xx[-5:],0)}       #\n #####################'
    dispred=f'{c("red"," #####################",1)}\n {c("red","#",1)}       {c("red",xx[-5:],0)}       {c("red","#",1)}\n{c("red"," #####################",1)}'
    dispyell=f'{c("yellow"," #####################",1)}\n {c("yellow","#",1)}       {c("yellow",xx[-5:],0)}       {c("yellow","#",1)}\n{c("yellow"," #####################",1)}'
    if detik>40:
        if detik%2==0:
            sys.stdout.write(f"{disp}  \r")
            sys.stdout.flush()
        else:
            sys.stdout.write(f"{dispred}  \r")
            sys.stdout.flush()
    elif detik>30:
        if detik%2==0:
            sys.stdout.write(f"{disp}  \r")
            sys.stdout.flush()
        else:
            sys.stdout.write(f"{dispyell}  \r")
            sys.stdout.flush()
    else:
        sys.stdout.write(f"{disp}  \r")
        sys.stdout.flush()
    time.sleep(0.3)