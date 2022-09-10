import requests
import json,random
import threading

dat = {"idx": 1, "result": [], "rapihkanjson": [], "terfilter": []}


def roomindo(dat):
    def doreq1():
        uriweb = "https://wjxwd01mwyo.dt01showxx02.com/App/Live/Index?category_id=2&page=1"
        headers = {
            "user-agent": f"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.{random.randint(100000,999999)}.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.{random.randint(1000,9999)}.{random.randint(100,999)} Mobile Safari/537.36",
            "bundleidentifier": "user",
            "accept-encoding": "identity",
            "host": "wjxwd01mwyo.dt01showxx02.com",
            "connection": "keep-alive",
        }
        res = requests.get(uriweb, headers=headers)
        res = json.loads(res.text)
        dat["result"].append(res["result"])

    def doreq2():
        uriweb = "https://wjxwd01mwyo.dt01showxx02.com/App/Live/Index?category_id=2&page=2"
        headers = {
            "user-agent": f"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.{random.randint(100000,999999)}.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.{random.randint(1000,9999)}.{random.randint(100,999)} Mobile Safari/537.36",
            "bundleidentifier": "user",
            "accept-encoding": "identity",
            "host": "wjxwd01mwyo.dt01showxx02.com",
            "connection": "keep-alive",
        }
        res = requests.get(uriweb, headers=headers)
        res = json.loads(res.text)
        dat["result"].append(res["result"])

    def doreq3():
        uriweb = "https://wjxwd01mwyo.dt01showxx02.com/App/Live/Index?category_id=2&page=3"
        headers = {
            "user-agent": f"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.{random.randint(100000,999999)}.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.{random.randint(1000,9999)}.{random.randint(100,999)} Mobile Safari/537.36",
            "bundleidentifier": "user",
            "accept-encoding": "identity",
            "host": "wjxwd01mwyo.dt01showxx02.com",
            "connection": "keep-alive",
        }
        res = requests.get(uriweb, headers=headers)
        res = json.loads(res.text)
        dat["result"].append(res["result"])

    def doreq4():
        uriweb = "https://wjxwd01mwyo.dt01showxx02.com/App/Live/Index?category_id=2&page=4"
        headers = {
            "user-agent": f"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.{random.randint(100000,999999)}.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.{random.randint(1000,9999)}.{random.randint(100,999)} Mobile Safari/537.36",
            "bundleidentifier": "user",
            "accept-encoding": "identity",
            "host": "wjxwd01mwyo.dt01showxx02.com",
            "connection": "keep-alive",
        }
        res = requests.get(uriweb, headers=headers)
        res = json.loads(res.text)
        dat["result"].append(res["result"])

    # def doreq5():
    #     uriweb = "https://wjxwd01mwyo.dt01showxx02.com/App/Live/Index?category_id=2&page=5"
    #     headers = {
    #         "user-agent": f"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.{random.randint(100000,999999)}.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.{random.randint(1000,9999)}.{random.randint(100,999)} Mobile Safari/537.36",
    #         "bundleidentifier": "user",
    #         "accept-encoding": "identity",
    #         "host": "wjxwd01mwyo.dt01showxx02.com",
    #         "connection": "keep-alive",
    #     }
    #     res = requests.get(uriweb, headers=headers)
    #     res = json.loads(res.text)
    #     dat["result"].append(res["result"])

    # def doreq6():
    #     uriweb = "https://wjxwd01mwyo.dt01showxx02.com/App/Live/Index?category_id=2&page=6"
    #     headers = {
    #         "user-agent": f"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.{random.randint(100000,999999)}.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.{random.randint(1000,9999)}.{random.randint(100,999)} Mobile Safari/537.36",
    #         "bundleidentifier": "user",
    #         "accept-encoding": "identity",
    #         "host": "wjxwd01mwyo.dt01showxx02.com",
    #         "connection": "keep-alive",
    #     }
    #     res = requests.get(uriweb, headers=headers)
    #     res = json.loads(res.text)
    #     dat["result"].append(res["result"])

    threads = []

    t1 = threading.Thread(target=doreq1)
    t1.daemon = True
    t2 = threading.Thread(target=doreq2)
    t2.daemon = True
    t3 = threading.Thread(target=doreq3)
    t3.daemon = True
    t4 = threading.Thread(target=doreq4)
    t4.daemon = True
    # t5 = threading.Thread(target=doreq5)
    # t5.daemon = True
    # t6 = threading.Thread(target=doreq6)
    # t6.daemon = True
    threads.append(t1)
    threads.append(t2)
    threads.append(t3)
    threads.append(t4)
    # threads.append(t5)
    # threads.append(t6)

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


def roomgame(dat):
    def doreq1():
        uriweb = "https://wjxwd01mwyo.dt01showxx02.com/App/Live/Index?category_id=3&page=1"
        headers = {
            "user-agent": f"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.{random.randint(100000,999999)}.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.{random.randint(1000,9999)}.{random.randint(100,999)} Mobile Safari/537.36",
            "bundleidentifier": "user",
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
            "user-agent": f"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.{random.randint(100000,999999)}.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.{random.randint(1000,9999)}.{random.randint(100,999)} Mobile Safari/537.36",
            "bundleidentifier": "user",
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
            "user-agent": f"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.{random.randint(100000,999999)}.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.{random.randint(1000,9999)}.{random.randint(100,999)} Mobile Safari/537.36",
            "bundleidentifier": "user",
            "accept-encoding": "identity",
            "host": "wjxwd01mwyo.dt01showxx02.com",
            "connection": "keep-alive",
        }
        res = requests.get(uriweb, headers=headers)
        res = json.loads(res.text)
        dat["result"].append(res["result"])

    # def doreq4():
    #     uriweb = "https://wjxwd01mwyo.dt01showxx02.com/App/Live/Index?category_id=3&page=4"
    #     headers = {
    #         "user-agent": f"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.{random.randint(100000,999999)}.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.{random.randint(1000,9999)}.{random.randint(100,999)} Mobile Safari/537.36",
    #         "bundleidentifier": "user",
    #         "accept-encoding": "identity",
    #         "host": "wjxwd01mwyo.dt01showxx02.com",
    #         "connection": "keep-alive",
    #     }
    #     res = requests.get(uriweb, headers=headers)
    #     res = json.loads(res.text)
    #     dat["result"].append(res["result"])

    # def doreq5():
    #     uriweb = "https://wjxwd01mwyo.dt01showxx02.com/App/Live/Index?category_id=3&page=5"
    #     headers = {
    #         "user-agent": f"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.{random.randint(100000,999999)}.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.{random.randint(1000,9999)}.{random.randint(100,999)} Mobile Safari/537.36",
    #         "bundleidentifier": "user",
    #         "accept-encoding": "identity",
    #         "host": "wjxwd01mwyo.dt01showxx02.com",
    #         "connection": "keep-alive",
    #     }
    #     res = requests.get(uriweb, headers=headers)
    #     res = json.loads(res.text)
    #     dat["result"].append(res["result"])

    threads = []

    t1 = threading.Thread(target=doreq1)
    t1.daemon = True
    t2 = threading.Thread(target=doreq2)
    t2.daemon = True
    t3 = threading.Thread(target=doreq3)
    t3.daemon = True
    # t4 = threading.Thread(target=doreq4)
    # t4.daemon = True
    # t5 = threading.Thread(target=doreq5)
    # t5.daemon = True
    threads.append(t1)
    threads.append(t2)
    threads.append(t3)
    # threads.append(t4)
    # threads.append(t5)

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

def roomseduc(dat):
    def doreq1():
        uriweb = "https://wjxwd01mwyo.dt01showxx02.com/App/Live/Index?category_id=7&page=1"
        headers = {
            "user-agent": f"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.{random.randint(100000,999999)}.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.{random.randint(1000,9999)}.{random.randint(100,999)} Mobile Safari/537.36",
            "bundleidentifier": "user",
            "accept-encoding": "identity",
            "host": "wjxwd01mwyo.dt01showxx02.com",
            "connection": "keep-alive",
        }
        res = requests.get(uriweb, headers=headers)
        res = json.loads(res.text)
        dat["result"].append(res["result"])

    # def doreq2():
    #     uriweb = "https://wjxwd01mwyo.dt01showxx02.com/App/Live/Index?category_id=3&page=2"
    #     headers = {
    #         "user-agent": f"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.{random.randint(100000,999999)}.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.{random.randint(1000,9999)}.{random.randint(100,999)} Mobile Safari/537.36",
    #         "bundleidentifier": "user",
    #         "accept-encoding": "identity",
    #         "host": "wjxwd01mwyo.dt01showxx02.com",
    #         "connection": "keep-alive",
    #     }
    #     res = requests.get(uriweb, headers=headers)
    #     res = json.loads(res.text)
    #     dat["result"].append(res["result"])

    # def doreq3():
    #     uriweb = "https://wjxwd01mwyo.dt01showxx02.com/App/Live/Index?category_id=3&page=3"
    #     headers = {
    #         "user-agent": f"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.{random.randint(100000,999999)}.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.{random.randint(1000,9999)}.{random.randint(100,999)} Mobile Safari/537.36",
    #         "bundleidentifier": "user",
    #         "accept-encoding": "identity",
    #         "host": "wjxwd01mwyo.dt01showxx02.com",
    #         "connection": "keep-alive",
    #     }
    #     res = requests.get(uriweb, headers=headers)
    #     res = json.loads(res.text)
    #     dat["result"].append(res["result"])

    # def doreq4():
    #     uriweb = "https://wjxwd01mwyo.dt01showxx02.com/App/Live/Index?category_id=3&page=4"
    #     headers = {
    #         "user-agent": f"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.{random.randint(100000,999999)}.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.{random.randint(1000,9999)}.{random.randint(100,999)} Mobile Safari/537.36",
    #         "bundleidentifier": "user",
    #         "accept-encoding": "identity",
    #         "host": "wjxwd01mwyo.dt01showxx02.com",
    #         "connection": "keep-alive",
    #     }
    #     res = requests.get(uriweb, headers=headers)
    #     res = json.loads(res.text)
    #     dat["result"].append(res["result"])

    # def doreq5():
    #     uriweb = "https://wjxwd01mwyo.dt01showxx02.com/App/Live/Index?category_id=3&page=5"
    #     headers = {
    #         "user-agent": f"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.{random.randint(100000,999999)}.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.{random.randint(1000,9999)}.{random.randint(100,999)} Mobile Safari/537.36",
    #         "bundleidentifier": "user",
    #         "accept-encoding": "identity",
    #         "host": "wjxwd01mwyo.dt01showxx02.com",
    #         "connection": "keep-alive",
    #     }
    #     res = requests.get(uriweb, headers=headers)
    #     res = json.loads(res.text)
    #     dat["result"].append(res["result"])

    threads = []

    t1 = threading.Thread(target=doreq1)
    t1.daemon = True
    # t2 = threading.Thread(target=doreq2)
    # t2.daemon = True
    # t3 = threading.Thread(target=doreq3)
    # t3.daemon = True
    # t4 = threading.Thread(target=doreq4)
    # t4.daemon = True
    # t5 = threading.Thread(target=doreq5)
    # t5.daemon = True
    threads.append(t1)
    # threads.append(t2)
    # threads.append(t3)
    # threads.append(t4)
    # threads.append(t5)

    for i in range(1):
        threads[i].start()

    for i in range(1):
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
            "user-agent": f"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.{random.randint(100000,999999)}.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.{random.randint(1000,9999)}.{random.randint(100,999)} Mobile Safari/537.36",
            "bundleidentifier": "user",
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
            "user-agent": f"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.{random.randint(100000,999999)}.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.{random.randint(1000,9999)}.{random.randint(100,999)} Mobile Safari/537.36",
            "bundleidentifier": "user",
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
            "user-agent": f"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.{random.randint(100000,999999)}.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.{random.randint(1000,9999)}.{random.randint(100,999)} Mobile Safari/537.36",
            "bundleidentifier": "user",
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
            "user-agent": f"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.{random.randint(100000,999999)}.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.{random.randint(1000,9999)}.{random.randint(100,999)} Mobile Safari/537.36",
            "bundleidentifier": "user",
            "accept-encoding": "identity",
            "host": "wjxwd01mwyo.dt01showxx02.com",
            "connection": "keep-alive",
        }
        res = requests.get(uriweb, headers=headers)
        res = json.loads(res.text)
        dat["result"].append(res["result"])

    def doreq5():
        uriweb = "https://wjxwd01mwyo.dt01showxx02.com/App/Live/Index?category_id=4&page=5"
        headers = {
            "user-agent": f"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.{random.randint(100000,999999)}.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.{random.randint(1000,9999)}.{random.randint(100,999)} Mobile Safari/537.36",
            "bundleidentifier": "user",
            "accept-encoding": "identity",
            "host": "wjxwd01mwyo.dt01showxx02.com",
            "connection": "keep-alive",
        }
        res = requests.get(uriweb, headers=headers)
        res = json.loads(res.text)
        dat["result"].append(res["result"])

    def doreq6():
        uriweb = "https://wjxwd01mwyo.dt01showxx02.com/App/Live/Index?category_id=4&page=6"
        headers = {
            "user-agent": f"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.{random.randint(100000,999999)}.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.{random.randint(1000,9999)}.{random.randint(100,999)} Mobile Safari/537.36",
            "bundleidentifier": "user",
            "accept-encoding": "identity",
            "host": "wjxwd01mwyo.dt01showxx02.com",
            "connection": "keep-alive",
        }
        res = requests.get(uriweb, headers=headers)
        res = json.loads(res.text)
        dat["result"].append(res["result"])

    def doreq7():
        uriweb = "https://wjxwd01mwyo.dt01showxx02.com/App/Live/Index?category_id=4&page=7"
        headers = {
            "user-agent": f"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.{random.randint(100000,999999)}.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.{random.randint(1000,9999)}.{random.randint(100,999)} Mobile Safari/537.36",
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


def roomhot(dat):
    def doreq1():
        uriweb = "https://wjxwd01mwyo.dt01showxx02.com/App/Live/RecommendList?page=1"
        headers = {
            "user-agent": f"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.{random.randint(100000,999999)}.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.{random.randint(1000,9999)}.{random.randint(100,999)} Mobile Safari/537.36",
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
            "user-agent": f"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.{random.randint(100000,999999)}.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.{random.randint(1000,9999)}.{random.randint(100,999)} Mobile Safari/537.36",
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
            "user-agent": f"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.{random.randint(100000,999999)}.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.{random.randint(1000,9999)}.{random.randint(100,999)} Mobile Safari/537.36",
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
            "user-agent": f"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.{random.randint(100000,999999)}.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.{random.randint(1000,9999)}.{random.randint(100,999)} Mobile Safari/537.36",
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
            "user-agent": f"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.{random.randint(100000,999999)}.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.{random.randint(1000,9999)}.{random.randint(100,999)} Mobile Safari/537.36",
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
            "user-agent": f"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.{random.randint(100000,999999)}.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.{random.randint(1000,9999)}.{random.randint(100,999)} Mobile Safari/537.36",
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
            "user-agent": f"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.{random.randint(100000,999999)}.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.{random.randint(1000,9999)}.{random.randint(100,999)} Mobile Safari/537.36",
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


def roomall():
    datt = {"idx": 1, "result": [], "rapihkanjson": [], "terfilter": []}
    rindo = roomindo(datt)
    rgame = roomgame(datt)
    rsexy = roomsexy(datt)
    rseduc = roomseduc(datt)
    # rhot = roomhot(datt)

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
    # for t in rhot:
    #     if t["nickname"] not in rname:
    #         if "6688" in t["nickname"]:
    #             pass
    #         elif "bling" in t["nickname"]:
    #             pass
    #         else:
    #             rname.append(t["nickname"])
    #             rall.append(t)
    return rall
