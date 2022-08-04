import requests
import json
import sys
import threading
import time
import ambil

host = "https://wjxwd01mwyo.dt01showxx02.com/"
dat = {"idx": 1, "result": [], "rapihkanjson": [], "terfilter": []}


def getlive():
    def doreq1():
        uriweb = "https://wjxwd01mwyo.dt01showxx02.com/App/Live/RecommendList?page=1"
        headers = {
            "user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.171019.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36",
            "bundleidentifier": "user",
            "accept-encoding": "identity",
            "host": "wjxwd01mwyo.dt01showxx02.com",
            "connection": "keep-alive",
        }
        res = requests.get(uriweb, headers=headers)
        res = json.loads(res.text)
        dat["result"].append(res["result"])

    def doreq2():
        uriweb = "https://wjxwd01mwyo.dt01showxx02.com/App/Live/RecommendList?page=2"
        headers = {
            "user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.171019.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36",
            "bundleidentifier": "user",
            "accept-encoding": "identity",
            "host": "wjxwd01mwyo.dt01showxx02.com",
            "connection": "keep-alive",
        }
        res = requests.get(uriweb, headers=headers)
        res = json.loads(res.text)
        dat["result"].append(res["result"])

    def doreq3():
        uriweb = "https://wjxwd01mwyo.dt01showxx02.com/App/Live/RecommendList?page=3"
        headers = {
            "user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.171019.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36",
            "bundleidentifier": "user",
            "accept-encoding": "identity",
            "host": "wjxwd01mwyo.dt01showxx02.com",
            "connection": "keep-alive",
        }
        res = requests.get(uriweb, headers=headers)
        res = json.loads(res.text)
        dat["result"].append(res["result"])

    def doreq4():
        uriweb = "https://wjxwd01mwyo.dt01showxx02.com/App/Live/RecommendList?page=4"
        headers = {
            "user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.171019.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36",
            "bundleidentifier": "user",
            "accept-encoding": "identity",
            "host": "wjxwd01mwyo.dt01showxx02.com",
            "connection": "keep-alive",
        }
        res = requests.get(uriweb, headers=headers)
        res = json.loads(res.text)
        dat["result"].append(res["result"])

    def doreq5():
        uriweb = "https://wjxwd01mwyo.dt01showxx02.com/App/Live/RecommendList?page=5"
        headers = {
            "user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.171019.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36",
            "bundleidentifier": "user",
            "accept-encoding": "identity",
            "host": "wjxwd01mwyo.dt01showxx02.com",
            "connection": "keep-alive",
        }
        res = requests.get(uriweb, headers=headers)
        res = json.loads(res.text)
        dat["result"].append(res["result"])

    def doreq6():
        uriweb = "https://wjxwd01mwyo.dt01showxx02.com/App/Live/RecommendList?page=6"
        headers = {
            "user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.171019.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36",
            "bundleidentifier": "user",
            "accept-encoding": "identity",
            "host": "wjxwd01mwyo.dt01showxx02.com",
            "connection": "keep-alive",
        }
        res = requests.get(uriweb, headers=headers)
        res = json.loads(res.text)
        dat["result"].append(res["result"])

    def doreq7():
        uriweb = "https://wjxwd01mwyo.dt01showxx02.com/App/Live/RecommendList?page=7"
        headers = {
            "user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.171019.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36",
            "bundleidentifier": "user",
            "accept-encoding": "identity",
            "host": "wjxwd01mwyo.dt01showxx02.com",
            "connection": "keep-alive",
        }
        res = requests.get(uriweb, headers=headers)
        res = json.loads(res.text)
        dat["result"].append(res["result"])

    threads = []

    t1 = threading.Thread(target=doreq1)
    t1.daemon = True
    t2 = threading.Thread(target=doreq2)
    t2.daemon = True
    t3 = threading.Thread(target=doreq3)
    t3.daemon = True
    t4 = threading.Thread(target=doreq4)
    t4.daemon = True
    t5 = threading.Thread(target=doreq5)
    t5.daemon = True
    t6 = threading.Thread(target=doreq6)
    t6.daemon = True
    t7 = threading.Thread(target=doreq7)
    t7.daemon = True
    threads.append(t1)
    threads.append(t2)
    threads.append(t3)
    threads.append(t4)
    threads.append(t5)
    threads.append(t6)
    threads.append(t7)

    for i in range(7):
        threads[i].start()

    for i in range(7):
        threads[i].join()

    for i in dat["result"]:
        for x in i:
            dat["rapihkanjson"].append(x)

    bck = []
    for x in dat["rapihkanjson"]:
        if x["nickname"] not in bck:
            bck.append(x["nickname"])
            dat["terfilter"].append(x)

    # itr = 1
    # for x in dat["terfilter"]:
    #     print(f'{itr}. {x["nickname"]}')
    #     itr += 1

    return dat["terfilter"]


def sen(id, tok, tex):
    uri = host + "App/Live/SendMsg"
    headers = {
        "user-agent": "HS-Android Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.171019.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4638.50 Mobile Safari/537.36",
        "bundleidentifier": "user",
        "x-token": tok,
        "accept-encoding": "identity",
        "connection": "keep-alive",
    }
    para = {"live_id": id, "content": tex}

    req = requests.get(uri, params=para, headers=headers)
    ress = json.loads(req.text)
    return ress


typi = [
    ["🤖 Welcome buat yg baru datang", 4],
    ["Jgn lupa difollow n4mnya", 6]
]

idlive = []
namahost = []
hostnya = [
    "INDO : Baby_sayanng"
]

while True:
    token = ambil.token()[int(input("token ke : "))-1]
    print("-------------------")
    try:
        room = getlive()
        for rum in room:
            print(rum["nickname"])
            if rum["nickname"] in hostnya:
                print(rum["nickname"])
                if rum["live_id"] not in idlive:
                    idlive.append(rum["live_id"])
                    namahost.append(rum["nickname"])

        # print(idlive)
        print("----------------------------------------------------")
        if len(idlive) != 0:
            try:
                for tex in typi:
                    for aidi in range(len(idlive)):
                        text = tex[0]
                        nam = ""
                        if "INDO" in namahost[aidi]:
                            nam = namahost[aidi].replace("INDO : ", "")
                        else:
                            nam = namahost[aidi]
                        if "MALAY" in namahost[aidi]:
                            nam = namahost[aidi].replace("MALAY : ", "")
                        else:
                            nam = namahost[aidi]
                        print()
                        print(f"\tM0DERATOR di {nam}")
                        if "n4m" in tex[0]:
                            text = tex[0].replace("n4m", nam)
                        print(text)
                        kirimlah = sen(idlive[aidi], token, text)
                    # print(kirimlah)
                    # print(f'{text}')
                    for t in range(tex[1], 0, -1):
                        sys.stdout.write(f"{t}\r")
                        sys.stdout.flush()
                        time.sleep(1)
            except:
                pass
        for t in range(350, 0, -1):
            sys.stdout.write(f"{t}\r")
            sys.stdout.flush()
            time.sleep(1)
    except Exception as e:
        print(f"Error : {e} ")
        for t in range(60, 0, -1):
            sys.stdout.write(f"{t}\r")
            sys.stdout.flush()
            time.sleep(1)
