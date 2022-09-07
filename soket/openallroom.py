import os
import seting
import getlive
import time
import random
from tinydb import *

db = TinyDB("datatokenroom.json")
tbl = Query()
db.truncate()


persi = seting.versi()

dat = {"ittrr":0}

game = {
    "baijiale_1": "Ba",
    "toubao_1": "Si",
    "kuaisan_1": "Th",
    "longhu_1": "Dr",
    "lunpan_1": "Ro",
    "honglv_1": "Co",
    "m12_1": "M12",
    "liuhecai_1": "M6",
}

idg = 1
for pkp in game:
    print(f"{idg}. {game[pkp]} = {pkp}")
    idg += 1
targetgameid = input("game nomer : ")

idxg = 1
for pgp in game:
    if idxg == int(targetgameid):
        targetgame = pgp
    idxg += 1

def cekbug():
    print(dat["ittrr"])
    if dat["ittrr"]>80:
        db.truncate()
        kil()
        return 1
    return 0
def buka(liveid, targetgame,namanya):
    rdmno = 0
    while True:
        rdmno = random.randint(0, 89)
        if len(db.search(tbl["tokenno"] == rdmno)) == 0:
            # db.insert({"tokenno":  "48", "data": {"liveid": "0"}})
            print(f"{rdmno}/{len(db.all())} insert")
            dat["ittrr"]+=1
            break
        else:
            if cekbug()==1:break
            print(f"{rdmno} terpakai")
    # os.system(f'start cmd /k python jdysocket.py {rdmno} {liveid} {targetgame}')#tetap terbuka
    # langsung tutup
    print(f"->>>>>>>>> {namanya}")
    os.system(
        f'start cmd /c python jdysocket.py {rdmno} {liveid} {targetgame} {namanya}')
    print(f'python jdysocket.py {rdmno} {liveid} {targetgame} {namanya}')
    db.insert({"tokenno":  rdmno, "data": {"liveid": liveid}})


bckpid=[]
import psutil,sys
# process.terminate()
plist = list(psutil.process_iter())
plist = sorted(plist, key=lambda i: i.name())
print()
for i in plist:
    bckpid.append(i.pid)
    sys.stdout.write(f"\t{i.pid}\t{i.name()}          /r")
    sys.stdout.flush()
print()

def kil():
    plist = list(psutil.process_iter())
    plist = sorted(plist, key=lambda i: i.name())
    for i in plist:
        if i.pid not in bckpid:
            p = psutil.Process(i.pid)
            p.terminate()

while True:
    db = TinyDB("datatokenroom.json")
    tbl = Query()
    room = getlive.roomall()
    x = 0
    for i in room:
        # print("{}. {}".format(str(x), i["nickname"]))
        idnya = i["live_id"]
        namanya = i["nickname"].replace(" ","_")
        if idnya not in dat:
            buka(idnya, targetgame,namanya)
            dat[idnya] = i["nickname"]
            time.sleep(0.4)
        x += 1
        # if x > 7:
            # kil()
            # break
    
    # if cekbug()==1:break
    time.sleep(305)
    # print(json.dumps(dat,indent=2))
