import os,ambil,seting,getlive

tokk = ambil.token()
persi = seting.versi()
token = tokk[0]
room = getlive.roomall()

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

x = 1
for i in room:
    print("{}. {}".format(str(x), i["nickname"]))
    x += 1
    os.system(f'start cmd /k python jdysocket.py {x-1} {i["live_id"]} {targetgame}')
    # if x==10:
    #     break