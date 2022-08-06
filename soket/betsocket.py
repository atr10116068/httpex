import websocket
import json
import time
import requests
import sys
import seting
import getlive
import ambil
import translatepy as trs
# TinyDB woiii

dat = {
    "data": {
        "Ba": {},
        "Si": {},
        "Th": {},
        "Dr": {},
        "Ro": {},
        "Co": {},
    }
}

tokk = ambil.token()
persi = seting.versi()
token = tokk[1]

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
}

datajuday = {
    # Baccarat
    "daxiao_da": "Big  ",
    "daxiao_xiao": "Small",
    "duizi_or": "E-Pair",
    "duizi_xian": "P-Pair",
    "zhuangxian_xian": "Plyer",
    "zhuangxian_zhuang": "Bnker",
    "zhuangxian_he": "Tie",

    # Sicbo
    "zonghe_dan": "Odd  ",
    "zonghe_da": "Big  ",
    "zonghe_xiao": "Small",
    "zonghe_shuang": "Even ",
    "zonghe_weitou": "Any  ",

    # ThreeDice
    "quanwei_666": "666  ",
    "quanwei_555": "555  ",
    "quanwei_444": "444  ",
    "quanwei_333": "333  ",
    "quanwei_222": "222  ",
    "quanwei_111": "111  ",
    "quanwei_weitou": "Any  ",
    "lunpanse_lunpansehong": "Red  ",

    # Dragon Tiger
    "longhuhe_he": "Draw ",
    "longhuhe_hu": "Tiger",
    "longhuhe_long": "Drgon",
    "longhuse_longhei": "B-Dra",
    "longhuse_longhong": "R-Dra",
    "longhuse_huhei": "B-Tig",
    "longhuse_huhong": "R-Tig",

    # Roulette
    "lunpandaxiao_da": "Big  ",
    "lunpandaxiao_xiao": "Small",
    "lunpanse_lunpansehong": "red  ",
    "lunpanse_lunpansehei": "black",
    "lunpandanshuang_dan": "Odd  ",
    "lunpandanshuang_shuang": "Even ",

    # Color
    "danma_1": "1    ",
    "danma_2": "2    ",
    "danma_3": "3    ",
    "danma_4": "4    ",
    "danma_5": "5    ",
    "danma_6": "6    ",

}


def lagi():
    try:
        import thread
    except ImportError:
        import _thread as thread

    def on_message(ws, message):
        datadadu = json.loads(message)
        try:
            if datadadu[0]["action"] == "game_lock_award":
                dat["data"] = {
                    "Ba": {},
                    "Si": {},
                    "Th": {},
                    "Dr": {},
                    "Ro": {},
                    "Co": {},
                }
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
                        try:
                            print(
                                f'---------[ {nama} ]-----------[ {bet} ]--------> coin:{coin}')
                            dat["data"][namgame][bet] = dat["data"][namgame][bet]+coin
                        except Exception as e:
                            dat["data"][namgame][bet] = coin

                        print(json.dumps(dat['data'], indent=2))
                        # if len(nama) < 8:
                        #     print(
                        #         f"{nama}\t\t\t{bet}\t\t{json.dumps(dat['data'],indent=2)}")
                        # elif len(nama) < 16:
                        #     print(
                        #         f"{nama}\t\t{bet}\t\t{json.dumps(dat['data'],indent=2)}")
                        # else:
                        #     print(
                        #         f"{nama}\t{bet}\t\t{json.dumps(dat['data'],indent=2)}")
                except Exception as e:
                    print(e)
                    print(datadadu[0]["data"]["msg_body"])

        except:
            pass

    def on_error(ws, error):
        pass
        #print("error : "+str(error))

    def on_close(ws, x, y):
        for i in range(3):
            sys.stdout.write(f"Reconnect after {i} \r")
            sys.stdout.flush()
            time.sleep(1)
        lagi()

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


lagi()
