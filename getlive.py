import requests,random
import json,ambil,seting
import threading

dat = {"idx": 1, "result": [], "rapihkanjson": [], "terfilter": []}
token=random.choice(ambil.token())
# print(token)
persi=seting.versi()
def roomindo(dat):
    def doreq1():
        uriweb = "https://wjxwd01mwyo.dt01showxx02.com/App/Live/Index?category_id=2&page=1"
        headers = {
            "user-agent": f"HS-IOS_iOSLV1/{persi} (iPhone; iOS 15.1; Scale/3.00)",
            "bundleidentifier": "user",
            "x-token": token,
            "x-version": persi,
            "accept-encoding": "identity",
            "host": "wjxwd01mwyo.dt01showxx02.com",
            "connection": "keep-alive",
        }
        res = requests.get(uriweb, headers=headers)
        res = json.loads(res.text)
        dat["result"].append(res["result"])
    doreq1()
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


def roomgame(dat):
    def doreq1():
        uriweb = "https://wjxwd01mwyo.dt01showxx02.com/App/Live/Index?category_id=3&page=1"
        headers = {
            "user-agent": f"HS-IOS_iOSLV2/{persi} (iPhone; iOS 15.1; Scale/3.00)",
            "bundleidentifier": "user",
            "x-token": token,
            "x-version": persi,
            "accept-encoding": "identity",
            "host": "wjxwd01mwyo.dt01showxx02.com",
            "connection": "keep-alive",
        }
        res = requests.get(uriweb, headers=headers)
        res = json.loads(res.text)
        dat["result"].append(res["result"])

    def doreq2():
        uriweb = "https://wjxwd01mwyo.dt01showxx02.com/App/Live/Index?category_id=3&page=2"
        headers = {
            "user-agent": f"HS-IOS_iOSLV2/{persi} (iPhone; iOS 15.1; Scale/3.00)",
            "bundleidentifier": "user",
            "x-token": token,
            "x-version": persi,
            "accept-encoding": "identity",
            "host": "wjxwd01mwyo.dt01showxx02.com",
            "connection": "keep-alive",
        }
        res = requests.get(uriweb, headers=headers)
        res = json.loads(res.text)
        dat["result"].append(res["result"])

    def doreq3():
        uriweb = "https://wjxwd01mwyo.dt01showxx02.com/App/Live/Index?category_id=3&page=3"
        headers = {
            "user-agent": f"HS-IOS_iOSLV2/{persi} (iPhone; iOS 15.1; Scale/3.00)",
            "bundleidentifier": "user",
            "x-token": token,
            "x-version": persi,
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
    threads.append(t1)
    threads.append(t2)
    threads.append(t3)

    for i in range(3):
        threads[i].start()

    for i in range(3):
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


def roomsexy(dat):
    def doreq1():
        uriweb = "https://wjxwd01mwyo.dt01showxx02.com/App/Live/Index?category_id=4&page=1"
        headers = {
            "user-agent": f"HS-IOS_iOSLV2/{persi} (iPhone; iOS 15.1; Scale/3.00)",
            "bundleidentifier": "user",
            "x-token": token,
            "x-version": persi,
            "accept-encoding": "identity",
            "host": "wjxwd01mwyo.dt01showxx02.com",
            "connection": "keep-alive",
        }
        res = requests.get(uriweb, headers=headers)
        res = json.loads(res.text)
        dat["result"].append(res["result"])

    def doreq2():
        uriweb = "https://wjxwd01mwyo.dt01showxx02.com/App/Live/Index?category_id=4&page=2"
        headers = {
            "user-agent": f"HS-IOS_iOSLV2/{persi} (iPhone; iOS 15.1; Scale/3.00)",
            "bundleidentifier": "user",
            "x-token": token,
            "x-version": persi,
            "accept-encoding": "identity",
            "host": "wjxwd01mwyo.dt01showxx02.com",
            "connection": "keep-alive",
        }
        res = requests.get(uriweb, headers=headers)
        res = json.loads(res.text)
        dat["result"].append(res["result"])

    def doreq3():
        uriweb = "https://wjxwd01mwyo.dt01showxx02.com/App/Live/Index?category_id=4&page=3"
        headers = {
            "user-agent": f"HS-IOS_iOSLV2/{persi} (iPhone; iOS 15.1; Scale/3.00)",
            "bundleidentifier": "user",
            "x-token": token,
            "x-version": persi,
            "accept-encoding": "identity",
            "host": "wjxwd01mwyo.dt01showxx02.com",
            "connection": "keep-alive",
        }
        res = requests.get(uriweb, headers=headers)
        res = json.loads(res.text)
        dat["result"].append(res["result"])

    def doreq4():
        uriweb = "https://wjxwd01mwyo.dt01showxx02.com/App/Live/Index?category_id=4&page=4"
        headers = {
            "user-agent": f"HS-IOS_iOSLV2/{persi} (iPhone; iOS 15.1; Scale/3.00)",
            "bundleidentifier": "user",
            "x-token": token,
            "x-version": persi,
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
    threads.append(t1)
    threads.append(t2)
    threads.append(t3)
    threads.append(t4)

    for i in range(4):
        threads[i].start()

    for i in range(4):
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


def roomhot(dat):
    def doreq1():
        uriweb = "https://wjxwd01mwyo.dt01showxx02.com/App/Live/RecommendList?page=1"
        headers = {
            "user-agent": f"HS-IOS_iOSLV2/{persi} (iPhone; iOS 15.1; Scale/3.00)",
            "bundleidentifier": "user",
            "x-token": token,
            "x-version": persi,
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
            "user-agent": f"HS-IOS_iOSLV2/{persi} (iPhone; iOS 15.1; Scale/3.00)",
            "bundleidentifier": "user",
            "x-token": token,
            "x-version": persi,
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
            "user-agent": f"HS-IOS_iOSLV2/{persi} (iPhone; iOS 15.1; Scale/3.00)",
            "bundleidentifier": "user",
            "x-token": token,
            "x-version": persi,
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
            "user-agent": f"HS-IOS_iOSLV2/{persi} (iPhone; iOS 15.1; Scale/3.00)",
            "bundleidentifier": "user",
            "x-token": token,
            "x-version": persi,
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
    threads.append(t1)
    threads.append(t2)
    threads.append(t3)
    threads.append(t4)

    for i in range(4):
        threads[i].start()

    for i in range(4):
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


def roomseduc(dat):
    def doreq1():
        uriweb = "https://wjxwd01mwyo.dt01showxx02.com/App/Live/Index?category_id=7&page=1"
        headers = {
            "user-agent": f"HS-IOS_iOSLV2/{persi} (iPhone; iOS 15.1; Scale/3.00)",
            "bundleidentifier": "user",
            "x-token": token,
            "x-version": persi,
            "accept-encoding": "identity",
            "host": "wjxwd01mwyo.dt01showxx02.com",
            "connection": "keep-alive",
        }
        res = requests.get(uriweb, headers=headers)
        res = json.loads(res.text)
        dat["result"].append(res["result"])

    def doreq2():
        uriweb = "https://wjxwd01mwyo.dt01showxx02.com/App/Live/Index?category_id=7&page=2"
        headers = {
            "user-agent": f"HS-IOS_iOSLV2/{persi} (iPhone; iOS 15.1; Scale/3.00)",
            "bundleidentifier": "user",
            "x-token": token,
            "x-version": persi,
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
    threads.append(t1)
    threads.append(t2)

    for i in range(2):
        threads[i].start()

    for i in range(2):
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

def roomcos(dat):
    def doreq1():
        uriweb = "https://wjxwd01mwyo.dt01showxx02.com/App/Live/Index?category_id=8&page=1"
        headers = {
            "user-agent": f"HS-IOS_iOSLV2/{persi} (iPhone; iOS 15.1; Scale/3.00)",
            "bundleidentifier": "user",
            "x-token": token,
            "x-version": persi,
            "accept-encoding": "identity",
            "host": "wjxwd01mwyo.dt01showxx02.com",
            "connection": "keep-alive",
        }
        res = requests.get(uriweb, headers=headers)
        res = json.loads(res.text)
        dat["result"].append(res["result"])

    def doreq2():
        uriweb = "https://wjxwd01mwyo.dt01showxx02.com/App/Live/Index?category_id=8&page=2"
        headers = {
            "user-agent": f"HS-IOS_iOSLV2/{persi} (iPhone; iOS 15.1; Scale/3.00)",
            "bundleidentifier": "user",
            "x-token": token,
            "x-version": persi,
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
    threads.append(t1)
    threads.append(t2)

    for i in range(2):
        threads[i].start()

    for i in range(2):
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

def roomall():
    datt = {"idx": 1, "result": [], "rapihkanjson": [], "terfilter": []}
    rindo = roomindo(datt)
    rgame = roomgame(datt)
    rsexy = roomsexy(datt)
    rseduc = roomseduc(datt)
    rcos = roomcos(datt)
    rhot = roomhot(datt)

    rall = []
    rname = []
    for t in rindo:
        if t["nickname"] not in rname:
            if "6688" in t["nickname"]:
                pass
            elif "bling" in t["nickname"]:
                pass
            else:
                rname.append(t["nickname"])
                rall.append(t)
    for t in rgame:
        if t["nickname"] not in rname:
            if "6688" in t["nickname"]:
                pass
            elif "bling" in t["nickname"]:
                pass
            else:
                rname.append(t["nickname"])
                rall.append(t)
    for t in rsexy:
        if t["nickname"] not in rname:
            if "6688" in t["nickname"]:
                pass
            elif "bling" in t["nickname"]:
                pass
            else:
                rname.append(t["nickname"])
                rall.append(t)
    for t in rseduc:
        if t["nickname"] not in rname:
            if "6688" in t["nickname"]:
                pass
            elif "bling" in t["nickname"]:
                pass
            else:
                rname.append(t["nickname"])
                rall.append(t)
    for t in rcos:
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
