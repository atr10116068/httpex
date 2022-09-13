import requests
import random
import threading
import json
import time
import seting
import sys
import ambil
import random as rd

idrumnya=input("id Room : ")
def roomgame(datrum):
    for i in range(1,5):
        uriweb = f"https://wjxwd01mwyo.dt01showxx02.com/App/Live/Index?category_id=3&page={i}"
        headers = {
            "user-agent": f"HS-Android Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.17{random.randint(1000,9999)}.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.{random.randint(1000,9999)}.82 Mobile Safari/537.36",
            "bundleidentifier": "user",
            "accept-encoding": "identity",
            "host": "wjxwd01mwyo.dt01showxx02.com",
            "connection": "keep-alive",
        }
        res = requests.get(uriweb, headers=headers)
        res = json.loads(res.text)
        datrum["result"].append(res["result"])
        time.sleep(1)


    for i in datrum["result"]:
        for x in i:
            datrum["rapihkanjson"].append(x)

    bck = []
    for x in datrum["rapihkanjson"]:
        if x["nickname"] not in bck:
            bck.append(x["nickname"])
            datrum["terfilter"].append(x)

    itr = 1
    for x in datrum["terfilter"]:
        # print(f'{itr}. {x["nickname"]}')
        itr += 1

    return datrum["terfilter"]


def roomhot(datrum):
    for i in range(1,7):
        uriweb = f"https://wjxwd01mwyo.dt01showxx02.com/App/Live/RecommendList?page={i}"
        headers = {
            "user-agent": f"HS-Android Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.17{random.randint(1000,9999)}.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.{random.randint(1000,9999)}.82 Mobile Safari/537.36",
            "bundleidentifier": "user",
            "accept-encoding": "identity",
            "host": "wjxwd01mwyo.dt01showxx02.com",
            "connection": "keep-alive",
        }
        res = requests.get(uriweb, headers=headers)
        res = json.loads(res.text)
        datrum["result"].append(res["result"])
        time.sleep(1)

    for i in datrum["result"]:
        for x in i:
            datrum["rapihkanjson"].append(x)

    bck = []
    for x in datrum["rapihkanjson"]:
        if x["nickname"] not in bck:
            bck.append(x["nickname"])
            datrum["terfilter"].append(x)

    itr = 1
    for x in datrum["terfilter"]:
        # print(f'{itr}. {x["nickname"]}')
        itr += 1

    return datrum["terfilter"]


def roomall():
    datrumm = {"idx": 1, "result": [], "rapihkanjson": [], "terfilter": []}
    rgame = roomgame(datrumm)
    rhot = roomhot(datrumm)

    rall = []
    rname = []
    for t in rgame:
        if t["nickname"] not in rname:
            if "6688" in t["nickname"]:
                pass
            elif "bling" in t["nickname"]:
                pass
            else:
                rname.append(t["nickname"])
                rall.append(t)
    for t in rhot:
        if t["nickname"] not in rname:
            if "6688" in t["nickname"]:
                pass
            elif "bling" in t["nickname"]:
                pass
            else:
                rname.append(t["nickname"])
                rall.append(t)
    return rall


# if True:
habisclaim = False
persi = seting.versi()


dat = {
    "akundapat": [],
    "anounc": "",
    "stop": False,
    "lendapat": 0,
    "dapat": 0,
    "hasil": [],
    "room": [],
    "nick": [],
}


def main():

    if len(ghj) < 3:
        dat["anounc"] = "0"
    else:
        dat["anounc"] = ghj

    intervals = (
        ("weeks", 604800),  # 60 * 60 * 24 * 7
        ("days", 86400),  # 60 * 60 * 24
        ("hours", 3600),  # 60 * 60
        ("minutes", 60),
        ("seconds", 1),
    )

    def display_time(seconds, granularity=2):
        result = []

        for name, count in intervals:
            value = seconds // count
            if value:
                seconds -= value * count
                if value == 1:
                    name = name.rstrip("s")
                result.append("{} {}".format(value, name))
        return ", ".join(result[:granularity])

    def sen(id, tex, x):
        uri = "https://wjxwd01mwyo.dt01showxx02.com/App/Live/SendMsg"
        headers = {
            "User-Agent": f"HS-Android Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.17{random.randint(1000,9999)}.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.{random.randint(1000,9999)}.82 Mobile Safari/537.36",
            "BundleIdentifier": "user",
            "X-Token": x,
            "Accept-Encoding": "identity",
            "X-Version": persi,
            "Content-Type": "application/x-www-form-urlencoded",
            "Content-Length": "25",
            "Host": "wjxwd01mwyo.dt01showxx02.com",
            "Connection": "Keep-Alive",
        }
        param = {"content": tex, "live_id": id}

        try:
            req = requests.post(uri, data=json.dumps(param), headers=headers)
            ress = json.loads(req.text)
        except:
            print("Failed...")

    def nama(x):
        uriweb = "https://wjxwd01mwyo.dt01showxx02.com/App/User_User/Info"
        headers = {
            "user-agent": f"HS-Android Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.17{random.randint(1000,9999)}.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.{random.randint(1000,9999)}.82 Mobile Safari/537.36",
            "bundleidentifier": "user",
            "x-token": x,
            "accept-encoding": "identity",
            "X-Version": persi,
            "host": "wjxwd01mwyo.dt01showxx02.com",
            "connection": "keep-alive",
        }
        f = requests.get(uriweb, headers=headers)
        ress = json.loads(f.text)
        # print(ress)
        if len(ress["result"]) != 0:
            return ress["result"]["nickname"]
        else:
            return 0

    def cekpao(id, x):
        uriweb = (
            "https://wjxwd01mwyo.dt01showxx02.com/App/RedPacket/CommandInfo?live_room_id=" + id
        )
        headers = {
            "user-agent": f"HS-Android Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.17{random.randint(1000,9999)}.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.{random.randint(1000,9999)}.82 Mobile Safari/537.36",
            "bundleidentifier": "user",
            "x-token": x,
            "accept-encoding": "identity",
            "X-Version": persi,
            "host": "wjxwd01mwyo.dt01showxx02.com",
            "connection": "keep-alive",
        }
        try:
            f = requests.get(uriweb, headers=headers)
            ress = json.loads(f.text)
            return ress
        except:
            return {"code": 109}

    def claimang(id, x):
        uriweb = "https://wjxwd01mwyo.dt01showxx02.com/App/RedPacket/CommandReceive?live_room_id={}&type=2".format(
            id
        )
        headers = {
            "user-agent": f"HS-Android Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.17{random.randint(1000,9999)}.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.{random.randint(1000,9999)}.82 Mobile Safari/537.36",
            "bundleidentifier": "user",
            "x-token": x,
            "accept-encoding": "identity",
            "X-Version": persi,
            "content-type": "application/x-www-form-urlencoded",
        }

        f = requests.get(uriweb, headers=headers)
        ress = json.loads(f.text)
        try:
            # print(ress)
            return ress
        except Exception as e:
            print(str(e))
            return "error"

    def represh():
        print("    Refresh room...")
        dat["room"] = []
        filtname = []

        for p in roomall():
            if p["nickname"] not in filtname:
                dat["room"].append(p)
                filtname.append(p["nickname"])
        #print("========================")
        #for p in range(len(dat["room"])):
            #print(f'{p}. {dat["room"][p]["nickname"]}')

        #print("    done")
        if len(dat["room"]) > 1:
            return 0
        else:
            return 1

    dat["hasil"] = []
    dat["lendapat"] = 0
    represh()
    tokk = ambil.token()
    token = tokk[0:totalakun]

    # print(1)
    for ikl in token[0:2]:
        qimak = nama(ikl)
        if qimak != 0:
            sys.stdout.write(f"    Nama : {qimak}\r")
            sys.stdout.flush()
        else:
            print(f"\n    Token Expired")
            break
    print()
    # ================================================== CEK PAO
    roompao = []
    bckup = []

    def cekadapao():
        while True:
            i = random.randint(0, len(dat["room"]))
            try:
                sementara = dat["room"]
                live_id = sementara[i]["live_id"]
                nickname = sementara[i]["nickname"]
                paoo = cekpao(live_id, token[0])
                # print(paoo)
                if paoo["code"] == 0:
                    taim = paoo["result"]["start_countdown"]
                    if taim > 60:
                        if taim < 10000:  # menit
                            # == == == == == == == == == == == == == == == == == == = fokus id live
                            if live_id == idrumnya:
                                paoo["result"]["live_id"] = live_id
                                paoo["result"]["nickname"] = nickname
                                if nickname not in bckup:
                                    roompao.append(paoo)
                                    bckup.append(nickname)
                                    print(paoo)
                sementara.pop(i)
            except:
                break

            if len(sementara) == 0:
                # print(f"thread closed")
                break
            sys.stdout.write(f"\t{len(sementara)}     \r")
            sys.stdout.flush()

    for t in range(3):
        threadLock = threading.Lock()
        threads = []
        for i in range(20):
            try:
                t = threading.Thread(target=cekadapao)
                t.daemon = True
                threads.append(t)
                time.sleep(0.2)
            except:
                pass

        for i in range(20):
            threads[i].start()

        for i in range(20):
            threads[i].join()

    # jika ada pao
    if len(roompao) != 0:

        # menyusun
        rpaopao = sorted(
            roompao, key=lambda k: k["result"]["start_countdown"])
        print()
        for p in rpaopao:
            print("  id\t:" + p["result"]["live_id"])
            print("  nama\t:" + p["result"]["nickname"])
            print("  coin\t:" + p["result"]["total_issue_amount"])
            print("  untuk\t:" + p["result"]["total_number"])
            print("  cd\t:" +
                  str(display_time(p["result"]["start_countdown"])))
            print()
        print()
        # =====================================================================================================
        # proses
        habisclaim = True
        print(json.dumps(rpaopao, indent=2))
        for rpp in rpaopao:
            tex = f'AMPAO {display_time(int(rpp["result"]["start_countdown"]))}={rpp["result"]["nickname"]}'
            print(tex)
            sen(int(dat["anounc"]), tex, token[0])
            tex = f"silahkan ambil dulu... nanti kesini lagi guys"
            print(tex)
            sen(int(dat["anounc"]), tex, token[0])
            cmnd = rpp["result"]["command"]

            print("\tSend Chat : " + cmnd)
            tknsen = token
            for iip in range(len(token) - 1):
                jeda = 1
                if rpp["result"]["start_countdown"] < 100:  # 2:30 menit
                    jeda = random.randint(3, 6)
                    print("mode cepat < 2 menit")
                elif rpp["result"]["start_countdown"] > 100:  # 5 menit
                    jeda = random.randint(6, 8)

                ii = random.choice(tknsen)
                idxtknsen = tknsen.index(ii)
                tknsen.pop(idxtknsen)
                sen(rpp["result"]["live_id"], cmnd, ii)
                for x in range(jeda, 0, -1):
                    sys.stdout.write(f"  cd:{x}\tcount:{iip}   \r")
                    sys.stdout.flush()
                    time.sleep(1)

            data = cekpao(rpp["result"]["live_id"], token[0])
            tim = data["result"]["start_countdown"]
            print("\tkuldon : " + display_time(tim))
            for kul in range(int(tim) - 3, 1, -1):
                inh = [10, 20, 30, 40, 50]
                if kul in inh:
                    sys.stdout.write(f"\t{display_time(kul)}    \r")

                if kul < 2:
                    sys.stdout.write(f"\t{display_time(kul)}    \r")
                    time.sleep(0.4)
                else:
                    sys.stdout.write(f"\t{display_time(kul)}    \r")
                    time.sleep(1)
                sys.stdout.flush()

            def ambilpao():
                indicat = [
                    "Do not receive the same red bag more than once",
                    "Unable to get command red packet without conditions reached",
                    "Received, can not be received again",
                    "Failed to grab the red envelope",
                    "Token error",
                ]

                
                tokk = ambil.token()
                tknth = tokk[0:totalakun]
                while len(tknth) > 0:
                    tknfast = random.randint(0, len(token) - 1)
                    qmak = claimang(
                        rpp["result"]["live_id"], tknth[tknfast])
                    print(qmak)
                    if qmak["code"] == 99:
                        pass
                    else:
                        try:
                            belendpt = qmak["result"]["amount"]
                            dat["totjam"].append(float(belendpt))
                            dat["akundapat"].append(
                                {"akun": tknfast, "coin": belendpt}
                            )
                        except:
                            pass
                        # print(f'{len(tknth)}\t: {qmak["msg"]} ')
                        if qmak["msg"] in indicat:
                            # print(f"<<<<<<<<<<<<<<<<<<< {qmak['msg']}")
                            tknth.pop(tknfast)
                        elif qmak["msg"] == "":
                            print(f'dapat : {qmak["result"]["amount"]}')
                            dat["hasil"].append(qmak["result"]["amount"])
                            dat["lendapat"] += 1
                        else:
                            # print(f">>>>>>>>>>>>>>>>>>> {qmak['msg']}")
                            pass

            thrpao = []
            for i in range(totalakun):
                t = threading.Thread(target=ambilpao)
                t.daemon = True
                thrpao.append(t)

            for i in range(totalakun):
                thrpao[i].start()

            for i in range(totalakun):
                thrpao[i].join()

        print()
        print("hasil : " + str(sum(map(float, dat["hasil"]))))
        print(f'akun yang dapat : {dat["lendapat"]}')
    else:
        habisclaim = False
    # print(habisclaim)
    print("\nwaiting....")
    if habisclaim == False:
        for x in range(300, 1, -1):  # 10 menit
            sys.stdout.write(f"waiting for {x} \r")
            sys.stdout.flush()
            time.sleep(1)

    print("___________________")


ghj = input("anounc id (pengingat ampau):")
tta = input("total akun:")
totalakun = int(tta)

while True:
    try:
        print()
        main()

        for x in range(20, 1, -1):
            sys.stdout.write(f"waiting for {x} \r")
            sys.stdout.flush()
            time.sleep(1)
    except Exception as e:
        print()
        print(f"error : {e}")
        print()
        for x in range(20, 1, -1):
            sys.stdout.write(f"countdown error {x} \r")
            sys.stdout.flush()
            time.sleep(1)
