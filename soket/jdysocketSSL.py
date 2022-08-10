import json
import requests
import seting
import getlive
import ambil
import translatepy as trs
from tinydb import *


import asyncio
import ssl
import websockets
import certifi
# import logging
# logging.basicConfig(filename="client.log", level=logging.DEBUG)
ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
ssl_context.load_verify_locations(certifi.where())


db = TinyDB("data.json")
tbl = Query()
db.truncate()

tokk = ambil.token()
persi = seting.versi()
token = tokk[int(input("token no : "))]

room = getlive.roomall()
x = 1
for i in room:
    print("{}. {}".format(str(x), i["nickname"]))
    x += 1

inp = input("room nomor : ")
idroom = room[int(inp)-1]["live_id"]
print("\nTarget Room : "+room[int(inp)-1]["nickname"])

datan = b"ping"
uriweb = "wss://dt001wsgew.qrdnk.cn/?token="+token
print(uriweb)
param = {
    "upgrade": "websocket",
    "connection": "Upgrade",
    "Accept-Encoding": "gzip",
    "host": "yoogs01wltb.dt01showxx03.com",
    "user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.171019.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36",
}
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

datajuday = {
    # Baccarat
    "daxiao_da": "Big",
    "daxiao_xiao": "Small",
    "duizi_or": "E-Pair",
    "duizi_xian": "P-Pair",
    "zhuangxian_xian": "Player",
    "zhuangxian_zhuang": "Banker",
    "zhuangxian_he": "Tie",

    # Sicbo
    "zonghe_dan": "Odd",
    "zonghe_da": "Big",
    "zonghe_xiao": "Small",
    "zonghe_shuang": "Even",
    "zonghe_weitou": "Any",

    # ThreeDice
    "quanwei_666": "666",
    "quanwei_555": "555",
    "quanwei_444": "444",
    "quanwei_333": "333",
    "quanwei_222": "222",
    "quanwei_111": "111",
    "quanwei_weitou": "Any",

    # Dragon Tiger
    "longhuhe_he": "Draw",
    "longhuhe_hu": "Tiger",
    "longhuhe_long": "Dragon",
    "longhuse_longhei": "B-Dra",
    "longhuse_longhong": "R-Dra",
    "longhuse_huhei": "B-Tig",
    "longhuse_huhong": "R-Tig",

    # Roulette
    "lunpandaxiao_da": "Big",
    "lunpandaxiao_xiao": "Small",
    "lunpanse_lunpansehong": "red",
    "lunpanse_lunpansehei": "black",
    "lunpandanshuang_dan": "Odd",
    "lunpandanshuang_shuang": "Even ",

    # Color
    "danma_1": "1",
    "danma_2": "2",
    "danma_3": "3",
    "danma_4": "4",
    "danma_5": "5",
    "danma_6": "6",
    "danma_7": "7",
    "danma_8": "8",
    "danma_9": "9",
    "sebo_hong": "entah1",
    "sebo_zi": "entah2",

    # M-12
    "weizhi_diyihang": "entah1",
    "liangmian_shuang": "entah2",
    "liangmian_shuang": "entah3",

}

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
    print(f"{idg}. {game[pkp]}")
    idg += 1
targetgameid = input("nomer : ")

idxg = 1
for pgp in game:
    if idxg == int(targetgameid):
        targetgame = pgp
    idxg += 1


def rp(str):
    bbb = str.replace("\'", "\"")
    return bbb



def xrespon(message):
    datadadu = json.loads(message)
    try:
        if datadadu[0]["action"] == "game_lock_award":
            print(f'{room[int(inp)-1]["nickname"]}_______[ Closing ]')
            db.truncate()
            db.all()
        elif datadadu[0]["action"] == "connected":
            print(f'\t\t{datadadu[0]["data"]["msg_body"]["client_id"]}')
            uriweb = "https://wjxwd01mwyo.dt01showxx02.com/App/LiveEnter/JoinGroup"
            headers = {
                "User-Agent": "HS-Android Mozilla/5.0 (Linux; Android 8.1.0; Pixel C Build/OPM1.171019.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36",
                "BundleIdentifier": "user",
                "X-Token": token,
                "Accept-Encoding": "identity",
                "X-Version": persi,
                "Host": "wjxwd01mwyo.dt01showxx02.com",
                "Connection": "Keep-Alive"
            }
            query = f'live_id={idroom}&client_id={datadadu[0]["data"]["msg_body"]["client_id"]}&type=1'
            req = requests.get(uriweb, params=query, headers=headers)
            ress = json.loads(req.text)
            print(ress)

        elif datadadu[0]["action"] == "game_do_order":
            try:
                sid = datadadu[0]["data"]["msg_body"]["show_id"]
                # hapus id BOT
                if "_" not in sid:
                    if datadadu[0]["data"]["msg_body"]["game"] == targetgame:
                        namgame = game[datadadu[0]
                                       ["data"]["msg_body"]["game"]]
                        nama = datadadu[0]["data"]["msg_body"]["nickname"]
                        bet = datadadu[0]["data"]["msg_body"]["order"]["detail"]
                        try:
                            for keybet in datajuday:
                                bet = bet.replace(
                                    keybet, datajuday[keybet])
                        except:
                            pass

                        coin = int(datadadu[0]["data"]["msg_body"]["cost"])
                        bet = bet.split(":")[0]

                        # add to data
                        if datadadu[0]["data"]["msg_body"]["game"] in game:
                            pupi = True
                        else:
                            pupi = False

                        print(
                            f'{room[int(inp)-1]["nickname"]}--[{namgame}] {bet}[{coin}]\t{nama}')
                        if pupi:
                            try:
                                if len(db.search(tbl["game"] == namgame)) == 0:
                                    # print("insert")
                                    db.insert(
                                        {"game": rp(namgame), "data": {rp(bet): coin}})
                                else:
                                    # print("update")
                                    x = db.get(tbl["game"] == namgame)
                                    if bet in x["data"]:
                                        # print(f">>> {bet} ada")
                                        xxxx = db.get(tbl["game"] == namgame)[
                                            "data"]
                                        # print(xxxx)
                                        xxxx[rp(bet)] += coin
                                        db.update({"data": xxxx},
                                                  tbl.game == namgame)
                                    else:
                                        # print(f">>>  {bet} tidak ada")
                                        xxxx = db.get(tbl["game"] == namgame)[
                                            "data"]
                                        xxxx[rp(bet)] = coin
                                        db.update({"data": xxxx},
                                                  tbl.game == namgame)
                                        # print(xxxx)
                            except Exception as e:
                                print(
                                    f"-----[ ERROR ] {e}")

                        # if len(nama) < 8:
                        #     print(
                        #         f"{nama}\t\t\t{bet}\t\t{json.dumps(dat['data'],indent=2)}")
                        # elif len(nama) < 16:
                        #     print(
                        #         f"{nama}\t\t{bet}\t\t{json.dumps(dat['data'],indent=2)}")
                        # else:
                        #     print(
                        #         f"{nama}\t{bet}\t\t{json.dumps(dat['data'],indent=2)}")
                    else:
                        pass  # targetgame
            except Exception as e:
                print(e)
                print(datadadu[0]["data"]["msg_body"])

    except Exception as e:
        print(f"Error: {e}")

while True:
    async def test():
        uri = uriweb
        async with websockets.connect(uri, ssl=ssl_context) as websocket:
            await websocket.send(datan)
            print("> test")
            while True:
                response = await websocket.recv()
                xrespon(response)

    asyncio.get_event_loop().run_until_complete(test())
