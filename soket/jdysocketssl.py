import _thread as thread
import translatepy as trs
import websockets
import json
import time
import requests
import sys
import seting
import getlive
import sys,os
import random
import ambil
from datetime import datetime
import pytz
from tinydb import *

import asyncio
import ssl
import websockets
import certifi

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

# import logging
# logging.basicConfig(filename="client.log", level=logging.DEBUG)
ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
ssl_context.load_verify_locations(certifi.where())


db = TinyDB("data.json")
dbtkn = TinyDB("datatokenroom.json")
tbl = Query()
# db.truncate()

tokk = ambil.token()
persi = seting.versi()
# token = tokk[int(input("token no : "))]
token = tokk[int(sys.argv[1])]
# room = getlive.roomall()
# x = 1
# for i in room:
#     print("{}. {}".format(str(x), i["nickname"]))
#     if i["live_id"] == sys.argv[2]:
#         idroom = i["live_id"]
#         namanya = i["nickname"]
#         break
#     x += 1

# inp = input("room nomor : ")
# idroom = room[int(inp)-1]["live_id"]
# print("\nTarget Room : "+room[int(inp)-1]["nickname"])

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
    "user-agent": f"HS-Android Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.17{random.randint(1000,9999)}.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.{random.randint(1000,9999)}.82 Mobile Safari/537.36",
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
targetgame = sys.argv[3]


def rp(str):
    bbb = str.replace("\'", "\"")
    return bbb


datroom = {
    "menitclosing": "",
    "viwermasuk": 0,
    "kosong_brp_kali": 0,
    "isexit": False,
    "simi": False,
    "lockclosing":False,
    "keyclosing":0,
}


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

dat = {
    "admin": [
        "1780067882",
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
        "1298487258"
    ],
    "minimumlvl": 7
}
host = ["1"]
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


def gas2(id, tok):
    uri1 = f"https://wjxwd01mwyo.dt01showxx02.com/App/Live/RealTimePeopleList?live_id={id}&page=1"
    headers = {
        "User-Agent": f"HS-Android Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.17{random.randint(1000,9999)}.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.{random.randint(1000,9999)}.82 Mobile Safari/537.36",
        "BundleIdentifier": "anchor",
        "X-Token": tok,
        "Accept-Encoding": "identitpython host/host.pyy",
        "X-Version": persi,
        "Host": "wjxwd01mwyo.dt01showxx02.com",
        "Connection": "Keep-Alive",
    }
    try:
        req1 = requests.get(uri1, headers=headers)
        ress1 = json.loads(req1.text)["result"]["list"]
        return ress1
    except:
        return [9, 9]


def cekkoin(x):
    print(x)
    tokk = ambil.token()
    tokence = tokk[int(x)-1]
    print(tokence)
    uriweb = "https://wjxwd01mwyo.dt01showxx02.com/App/User_User/Info"
    headers = {
        "user-agent": f"HS-Android Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.17{random.randint(1000,9999)}.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.{random.randint(1000,9999)}.82 Mobile Safari/537.36",
        "bundleidentifier": "user",
        "x-token": tokence,
        "accept-encoding": "identity",
        "host": "wjxwd01mwyo.dt01showxx02.com",
        "connection": "keep-alive",
    }
    f = requests.get(uriweb, headers=headers)
    ress = json.loads(f.text)
    try:
        krm = [
            ress["result"]["nickname"],
            ress["result"]["balance"],
            ress["result"]["vip_name"],
            ress["result"]["id"],
        ]
        sen(idroom, token,
            f'{ress["result"]["nickname"]} ada {ress["result"]["balance"]} coin bang')
    except:
        sen(idroom, token, f"rusak bang :v")


def cariviwer(udata):
    udata["utex"] = udata["utex"].replace("cariakun ", "")
    viwerny = udata["utex"]
    roomxx = getlive.roomall()
    nemu = False
    for iii in roomxx:
        idroomss = iii["live_id"]
        namaroom = iii["nickname"]
        try:
            datas = gas2(idroomss, tokenhost)
            for pp in datas:
                nama = pp["nickname"]
                if nama == viwerny:
                    nemu = {0: nama, 1: namaroom}
        except:
            print("Gagal Capture Data")
    if nemu != False:
        sen(idroom, token, f"{nemu[0]} di {nemu[1]}")
    else:
        sen(idroom, token, f"Ga nemu bang")


def clvl(udata):
    try:
        udata["utex"] = udata["utex"].replace("changelvl ", "")
        dat["minimumlvl"] = int(udata["utex"])
        sen(idroom, token, f"Sudah di sett ke {udata['utex']}")
    except Exception as e:
        print(f"Error : {e}")

gid=[]
imb = ["karena", "ketika", "saat", "dan", "melihat", "mendengar"]
gamechat = {
    "nama":[],
    "kerja":[]
    }


def jumhost():
    rgame = getlive.roomgame(
        {"idx": 1, "result": [], "rapihkanjson": [], "terfilter": []})
    rindo = getlive.roomindo(
        {"idx": 1, "result": [], "rapihkanjson": [], "terfilter": []})
    rsexy = getlive.roomsexy(
        {"idx": 1, "result": [], "rapihkanjson": [], "terfilter": []})
    dat = {
        "game": len(rgame),
        "indo": len(rindo),
        "sexy": len(rsexy),
    }
    return dat


def sen(id, tok, tex):
    uri = "https://wjxwd01mwyo.dt01showxx02.com/App/Live/SendMsg"
    headers = {
        "user-agent": f"HS-Android Mozilla/5.0 (Linux; Android 8.1.0; SM-J730F Build/{random.randint(1000,9999)}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.{random.randint(1000,9999)}.129 Mobile Safari/537.36",
        "bundleidentifier": "user",
        "x-token": tok,
        "accept-encoding": "identity",
        "host": "wjxwd01mwyo.dt01showxx02.com",
        "connection": "keep-alive"
    }
    para = {"live_id": id, "content": tex}

    req = requests.get(uri, params=para, headers=headers)
    ress = json.loads(req.text)
    return ress


def trans(udata):
    try:
        udata["utex"] = udata["utex"].replace("tr ", "")
        desx = udata["utex"].split(" ")[0]
        if desx == "cn":
            desx = "zh-tw"
        se0 = udata["utex"].split(" ")
        del se0[0]
        texxx = ""
        for tp in se0:
            texxx += f'{tp} '

        # print(f"texx : {texx}")
        # print(f"desx : {desx}")
        # print(f"texxx : {texxx}")
        hasi = trs.tpy(texxx, desx)
        # <<<< ['入力しようとしています', 'Nyūryoku shiyou to shite imasu'] >>>>>>
        sen(idroom, token, hasi[1])
    except Exception as e:
        print(f"Error : {e}")
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


def xrespon(message):
    datadadu = json.loads(message)
    # print(datadadu[0])
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
                if datroom["viwermasuk"]<4:
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


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        if datadadu[0]["action"] == "send_msg":
            utex = datadadu[0]['data']['msg_body']['content']
            udata = {
                "uid": datadadu[0]['data']['msg_body']['show_id'],
                "ulvl": datadadu[0]['data']['msg_body']['vip'],
                "uname": datadadu[0]['data']['msg_body']['nickname'],
                "utex": utex,
            }

            if udata['utex'].lower() in ["taro", "bangtaro","bang taro","tar","ro","bang at","at"]:
                bawel = [
                    "apa sih... cok",
                    "apaan?",
                    "ada apa sayang?",
                    "oiiiii",
                    "kenapa?",
                    "gw disini...",
                    "ada apa 𓂸",
                    "manggil mulu, ada apa sih",
                ]
                tex = random.choice(bawel)
                sen(idroom, token, tex)
            try:
                if utex.startswith("."):
                    texx = utex.replace(".", "")
                    udata["utex"] = texx
                    if udata['utex'] == "reset":
                        if udata["uid"] in dat["admin"] or udata["ulvl"] in host:
                            gamechat.clear()
                            gid.clear()
                        else:
                            tex = "Hanya adminku yang boleh"
                            sen(idroom, token, tex)
                    if udata['utex'] == "cek":
                        tex = f"{len(gid)} akun ikutan"
                        sen(idroom, token, tex)
                    if udata['utex'] == "main":
                        if udata["uid"] in dat["admin"] or udata["ulvl"] in host:
                            for tex in ["ketik .add [nama]-[kerja]-[nama]-[kerja]", 'contoh .add budi-terkejut-alex-uncep']:
                                sen(idroom, token, tex)

                    elif udata['utex'] == "acak":
                        if udata["uid"] in dat["admin"] or udata["ulvl"] in host:
                            print(gid)
                            print(gamechat)
                            disp = f"{gamechat[random.choice(gid)][0]} {gamechat[random.choice(gid)][1]} {random.choice(imb)} {gamechat[random.choice(gid)][2]} {gamechat[random.choice(gid)][3]}"
                            sen(idroom, token, disp)
                        else:
                            tex = "Hanya adminku yang boleh"
                            sen(idroom, token, tex)

                    elif udata['utex'].startswith("add "):
                        dgame = texx.replace("add ", "")
                        dgames = dgame.split("-")
                        if len(dgames) == 4:
                            gamechat[udata["uid"]] = dgames
                            if udata["uid"] not in gid:
                                gid.append(udata["uid"])
                            tex = "Sudah ditambah"
                            sen(idroom, token, tex)
                        else:
                            tex = "contoh nama-ekspresi-nama-ekspresi"
                            sen(idroom, token, tex)
                            tex = "contoh budi-terkejut-rudi-tertawa"
                            sen(idroom, token, tex)
            except Exception as e:
                print(e)

            if utex.lower().startswith("taro "):
                texx = utex.lower().replace("taro ", "")
                udata["utex"] = texx
                try:
                    if lepel[udata["ulvl"]] >= dat["minimumlvl"] or udata["uid"] in dat["admin"]:
                        if udata['utex'].startswith("tr "):
                            trans(udata)
                        elif udata['utex'].startswith("cariakun "):
                            udata["utex"]=utex.replace("taro ", "")
                            cariviwer(udata)
                        elif udata['utex'].startswith("cek koin "):
                            udata["utex"]=utex.replace("taro cek koin", "")
                            if udata["uid"] in dat["admin"] or udata["ulvl"] in host:
                                cekkoin(udata["utex"])
                            else:
                                tex = "Hanya adminku yang boleh"
                                sen(idroom, token, tex)
                        elif udata['utex'].startswith("changelvl "):
                            if udata["uid"] in dat["admin"] or udata["ulvl"] in host:
                                clvl(udata)
                            else:
                                tex = "Hanya adminku yang boleh"
                                sen(idroom, token, tex)

                        if udata['utex'] == "siapa aku?":
                            if udata["uid"] in dat["admin"]:
                                tex = "kamu itu adminku"
                                sen(idroom, token, tex)
                            elif udata["ulvl"] in host:
                                tex = "kamu itu Host"
                                sen(idroom, token, tex)
                            else:
                                tex = "kamu viwer biasa"
                                sen(idroom, token, tex)
                        elif udata['utex'] == "bisa apa aja?":
                            texs = [
                                "-> taro siapa aku?",
                                "-> taro cariakun [nama]",
                                "-> taro tr [bahasa] [text]",
                                "-> taro jumlah host",
                            ]
                            for tex in texs:
                                sen(idroom, token, tex)
                                time.sleep(2)
                        elif udata['utex'] == "jumlah host":
                            dats = jumhost()
                            sen(idroom, token, f'{dats["game"]} host game')
                            sen(idroom, token,
                                f'{dats["indo"]} host adorable')
                            sen(idroom, token, f'{dats["sexy"]} host sexy')
                    else:
                        tex = f"Hanya dapat di gunakan oleh LVL {str(dat['minimumlvl'])} keatas"
                        sen(idroom, token, tex)
                except Exception as e:
                    print(f"Error : {e}")

            print(
                f" > [{udata['uid']}][{lepel[udata['ulvl']]}] {udata['uname']}\t: {udata['utex']}")
    except Exception as e:
        print(f"Error : {e}")


while True:
    tz = pytz.timezone("Asia/Jakarta")
    now = datetime.now(tz)
    detik=now.strftime("%S")
    if int(detik)==14:

        while True:
            if datroom["isexit"] == True:
                break
            print(c("blue","is EXIT??? : ",0)+f' {datroom["isexit"]}       ')
            try:
                async def test():
                    uri = uriweb
                    async with websockets.connect(uri, ssl=ssl_context) as websocket:
                        await websocket.send(datan)
                        print("> test")
                        while True:
                            response = await websocket.recv()
                            xrespon(response)

                asyncio.get_event_loop().run_until_complete(test())
            except:
                time.sleep(1)
                pass
    else:
        sys.stdout.write(f"Waiting time [{detik}]/14     \r")
        sys.stdout.flush()
    time.sleep(1)
# input("exit")

