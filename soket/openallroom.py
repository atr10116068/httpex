import os
import seting
import getlive
import json
import time
import ambil
import random
from tinydb import *

db = TinyDB("datatokenroom.json")
tbl = Query()
db.truncate()

getproxx = ambil.proxy()
listObj = {"prox": getproxx}
with open("proxy.json", 'w') as json_file:
    json.dump(listObj, json_file, indent=2,  separators=(',', ': '))


persi = seting.versi()

dat = {}

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


def buka(liveid, targetgame):
    rdmno = 0
    while True:
        rdmno = random.randint(0, 89)
        if len(db.search(tbl["tokenno"] == rdmno)) == 0:
            db.insert({"tokenno":  "48", "data": {"liveid": "0"}})
            print(f"{rdmno} insert")
            break
        else:
            print(f"{rdmno} terpakai")
    # os.system(f'start cmd /k python jdysocket.py {rdmno} {liveid} {targetgame}')#tetap terbuka
    # langsung tutup
    os.system(
        f'start cmd /c python jdysocket.py {rdmno} {liveid} {targetgame}')
    db.insert({"tokenno":  rdmno, "data": {"liveid": liveid}})


while True:
    room = getlive.roomall()
    x = 0
    for i in room:
        # print("{}. {}".format(str(x), i["nickname"]))
        idnya = i["live_id"]
        if idnya not in dat:
            buka(idnya, targetgame)
            dat[idnya] = i["nickname"]
            time.sleep(0.4)
        x += 1
        if x == 6:
            break
    time.sleep(120)
    # print(json.dumps(dat,indent=2))
