import os,seting,getlive,json,time,random

persi = seting.versi()

dat={"notoken":[]}

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

def buka(tokenno,liveid,targetgame):
    os.system(f'start cmd /k python jdysocket.py {tokenno} {liveid} {targetgame}')

def caritkn():
    rdmno=0
    while True:
        rdmno=random.randint(0,89)
        if rdmno not in dat["notoken"]:
            dat["notoken"].append(rdmno)
            break
    return rdmno
while True:
    room = getlive.roomall()
    # x=0
    for i in room:
        # print("{}. {}".format(str(x), i["nickname"]))
        idnya=i["live_id"]
        if idnya not in dat:
            tkn=caritkn()
            buka(str(tkn),idnya,targetgame)
            dat[idnya]=i["nickname"]
        # x+=1
        # if x==15:
        #     break
    time.sleep(120)
    # print(json.dumps(dat,indent=2))