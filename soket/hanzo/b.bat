import websocket
import json
import time
import requests
import sys
import seting
import sys,random
import ambil
from datetime import datetime
import pytz
from tinydb import *
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

db = TinyDB("data.json")
dbtkn = TinyDB("datatokenroom.json")
tbl = Query()

tokk = ambil.token()
persi = seting.versi()
token = tokk[int(sys.argv[1])]

idroom=sys.argv[2]
namanya=sys.argv[4]
print(f"\nTarget Room : {namanya}")

datan = b"ping"
uriweb = "wss://yoogs01wltb.dt01showxx03.com/?token="+token

param = {
    "upgrade": "websocket",
    "connection": "Upgrade",
    "Accept-Encoding": "gzip",
    "host": "yoogs01wltb.dt01showxx03.com",
    "user-agent": f"Mozilla/5.0 (iPhone11,2; U; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/602.{random.randint(0,255)}.{random.randint(0,255)} (KHTML, like Gecko) Version/9.0 Mobile/{random.randint(11,99)}E{random.randint(111,999)} Safari/602.1",
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

# idg = 1
# for pkp in game:
#     print(f"{idg}. {game[pkp]}")
#     idg += 1
# targetgameid = input("nomer : ")

# idxg = 1
# for pgp in game:
#     if idxg == int(targetgameid):
#         targetgame = pgp
#     idxg += 1
targetgame=sys.argv[3]

def rp(str):
    bbb = str.replace("\'", "\"")
    return bbb

datroom={
    "menitclosing":"",
    "viwermasuk":0,
    "kosong_brp_kali":0,
    "isexit":False,
    "lockclosing":False,
    "keyclosing":0,
    }



#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

import translatepy as trs
dat = {
    "admin": [
        "1119943580",
        "1708242561",
        "1696182045",
        "1665699504",
        "1037219061",
        "1188860696",
        "1696985118",
        "1702716897",
        "1702616359",
        "1000361907",
        "1298487258",
        "1770366476"
    ],
    "minimumlvl": 7
}
host=["1"]
lepel = {
    "1": 15,  # host
    "13": 2,
    "14": 3,
    "2": 4,
    "4": 5,
    "5": 6,
    "6": 7,
    "7": 8,
    "9": 9,
    "8": 10,
    "10": 11,
    "11": 12,
    "3": 13,
    "12": 14,  # admin
}

tokenhost = ambil.tokenhost()

gid = []
imb = ["karena", "ketika", "saat", "dan", "melihat", "mendengar"]
gamechat = {}


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def lagi():
    import _thread as thread

    def on_message(ws, message):
        try:
            tz = pytz.timezone("Asia/Jakarta")
            now = datetime.now(tz)
            menit=now.strftime("%M")
            detik=now.strftime("%S")
            datadadu = json.loads(message)

            if int(detik)-int(datroom["keyclosing"])>5:
                if datroom["lockclosing"]==True:
                    print(c("green",f"-----------> UnLock",0))
                datroom["lockclosing"]=False
            # if datadadu[0]["action"] != "game_lock_award":
            #     print(f"keyclosing : {datroom['keyclosing']}/{detik}")
            # print(c("green",f"{datadadu[0]}",0))
            # print(c("yellow",f"->>>>>>> closing {datroom['lockclosing']}",0))
            if datadadu[0]["action"] == "game_lock_award":
                print(c("red","closing",0))
                if datroom["lockclosing"]==False:
                    datroom["lockclosing"]=True
                    datroom["keyclosing"]=int(detik)
                    if datroom["viwermasuk"]<3:
                        if datroom["kosong_brp_kali"]<3:
                            datroom["kosong_brp_kali"]+=1
                            print(c("red",f"closing viwer < 2  ke-{datroom['kosong_brp_kali']} kali",0))
                        else:
                            print(c("red",f'EXIT...!!! kosong sekian kali {datroom["kosong_brp_kali"]}',0))
                            datroom["isexit"]=True
                            dbtkn.remove(where('tokenno') == sys.argv[1])
                            exit()
                    else:
                        datroom["kosong_brp_kali"]=0
                    
                if datroom["menitclosing"]!=menit:
                    print(f'\t[ Closing ] jumlah viwer masuk[{datroom["viwermasuk"]}] {namanya}')
                    datroom["menitclosing"]=menit
                    datroom["viwermasuk"]=0
                    db.truncate()
                    db.all()
                else:
                    pass
            elif datadadu[0]["action"] == "enter":
                sys.stdout.write(f'Masuk {datadadu[0]["data"]["msg_body"]["nickname"]}\t\tjumlah viwer : {datroom["viwermasuk"]}      \r')
                sys.stdout.flush()
                datroom["viwermasuk"]+=1
            elif datadadu[0]["action"] == "connected":
                print(f'\t\t{datadadu[0]["data"]["msg_body"]["client_id"]}')
                uriweb = "https://wjxwd01mwyo.dt01showxx02.com/App/LiveEnter/JoinGroup"
                headers = {
                    "User-Agent": f"Mozilla/5.0 (iPhone11,2; U; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/602.{random.randint(0,255)}.{random.randint(0,255)} (KHTML, like Gecko) Version/9.0 Mobile/{random.randint(11,99)}E{random.randint(111,999)} Safari/602.1",
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
                            namgame = game[datadadu[0]["data"]["msg_body"]["game"]]
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
                                f'{namanya}--[{namgame}] {bet}[{coin}]\t{nama}')
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
            print(f"Error : [{e}]")
            if e==0:
                input("lanjut? enter")

    def on_error(ws, error):
        pass
        # print("error : "+str(error))

    def on_close(ws, x, y):
        if datroom["isexit"]==False:
            print(c("cyan","____________[ RECONNECT ]____________",0))
            # for i in range(3):
            #     sys.stdout.write(f"Reconnect after {i} \r")
            #     sys.stdout.flush()
            #     time.sleep(1)
            lagi()
        else:
            db.remove(where('tokenno') == sys.argv[1])
            exit()

    def on_open(ws):
        def run(*args):
            ws.send(datan)
            # ws.close()
        thread.start_new_thread(run, ())

    if __name__ == "__main__":
        # websocket.enableTrace(True)
        ws = websocket.WebSocketApp(uriweb,
                                    header=param,
                                    on_open=on_open,
                                    on_message=on_message,
                                    on_error=on_error,
                                    on_close=on_close)

        ws.run_forever()

try:
    while True:
        tz = pytz.timezone("Asia/Jakarta")
        now = datetime.now(tz)
        detik=now.strftime("%S")
        masuk=5
        if int(detik)==masuk:
            lagi()
        else:
            sys.stdout.write(f"Waiting time [{detik}]/{masuk}     \r")
            sys.stdout.flush()
        time.sleep(1)

except Exception as e:
    print(f"\tError : {e}")
input("exit")
