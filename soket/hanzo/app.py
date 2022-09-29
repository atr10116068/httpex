import os,pytz,json,httpx,sys,time,random,threading,psutil
from tinydb import *
from datetime import datetime
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

def bukacmd(persi,rdmnno,idrum,namanya):
    os.system(f'start cmd /k python b.bat {persi} {rdmnno} {idrum} {namanya}')
    time.sleep(1)
    
def waitingfor(x):
    for tipi in range(x,0,-1):
        sys.stdout.write(f"wait for {tipi} \r")
        sys.stdout.flush()
        time.sleep(1)
def getlive(mode):
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
            res = httpx.get(uriweb, headers=headers)
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
            res = httpx.get(uriweb, headers=headers)
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
            res = httpx.get(uriweb, headers=headers)
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
            res = httpx.get(uriweb, headers=headers)
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
        #     res = httpx.get(uriweb, headers=headers)
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
        #     res = httpx.get(uriweb, headers=headers)
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
            res = httpx.get(uriweb, headers=headers)
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
            res = httpx.get(uriweb, headers=headers)
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
            res = httpx.get(uriweb, headers=headers)
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
        #     res = httpx.get(uriweb, headers=headers)
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
        #     res = httpx.get(uriweb, headers=headers)
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
            res = httpx.get(uriweb, headers=headers)
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
            res = httpx.get(uriweb, headers=headers)
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
            res = httpx.get(uriweb, headers=headers)
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
            res = httpx.get(uriweb, headers=headers)
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
            res = httpx.get(uriweb, headers=headers)
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
            res = httpx.get(uriweb, headers=headers)
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
            res = httpx.get(uriweb, headers=headers)
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
            res = httpx.get(uriweb, headers=headers)
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
            res = httpx.get(uriweb, headers=headers)
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
            res = httpx.get(uriweb, headers=headers)
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
            res = httpx.get(uriweb, headers=headers)
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
            res = httpx.get(uriweb, headers=headers)
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
            res = httpx.get(uriweb, headers=headers)
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
            res = httpx.get(uriweb, headers=headers)
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
    
    if mode=="indo":
        return roomindo(dat)
    if mode=="game":
        return roomgame(dat)
    if mode=="sexy":
        return roomsexy(dat)
    if mode=="hot":
        return roomhot(dat)
    if mode=="all":
        return roomall()




























def seting(mode):
    def setingx():
        uriweb="https://wjxwd01mwyo.dt01showxx02.com/App/Setting/Global"
        headers={
        "x-ws-apm-id":"C0A24009-062E-4AA1-9950-0023510E1A63-16",
        "user-agent":f"HS-Android Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.17{random.randint(1000,9999)}.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.{random.randint(1000,9999)}.82 Mobile Safari/537.36",
        "bundleidentifier":"user",
        "accept-encoding":"identity",
        "host":"wjxwd01mwyo.dt01showxx02.com",
        "x-version":"2.10.4",
        "connection":"keep-alive"
        }
        f=httpx.get(uriweb,headers=headers)
        try:
            if f.status_code==200:
                return [f.status_code,json.loads(f.text)]
            else:
                return [f.status_code,f.text]
        except Exception as e:
            print(f"Error : {e}")

    def disp(x):
        sys.stdout.write(f"\t{x}\r")
        sys.stdout.flush()

    ress={"stat":999,"sett":""}
    titik="."
    while ress["stat"]!=200:
        disp(f"Getting Version{titik}")
        titik+="."
        ff=setingx()
        try:
            ress["stat"]=ff[0]
            ress["sett"]=ff[1]
        except:
            pass
        time.sleep(1)
    
    if mode=="versi":
        return(ress["sett"]["result"]["android_user_version"])

    
    if mode=="sensitif":
        return(ress["sett"]["result"]["sensitive_words"].split("#"))
        






















def openprofile():
    uric="https://raw.githubusercontent.com/atr10116068/httpex/master/soket/profile.py"
    sca=httpx.get(uric).text
    with open("profile.bat", 'w') as out:
        out.write(sca)
    os.system(f'start cmd /k python profile.bat')
    time.sleep(1)
    os.unlink("profile.bat")

def openall(persi):
    urib="https://raw.githubusercontent.com/atr10116068/httpex/master/soket/hanzo/sockethanzo.py"
    sca=httpx.get(urib).text
    with open("b.bat", 'w') as out:
        out.write(sca)
    db = TinyDB("datatokenroom.json")
    tbl = Query()
    db.truncate()


    dat = {"ittrr":0}

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

    def cekbug():
        print(dat["ittrr"])
        if dat["ittrr"]>130:
            db.truncate()
            kil()
            return 1
        return 0
    def buka(liveid, targetgame,namanya):
        rdmno = 0
        while True:
            rdmno = random.randint(0, 89)
            if len(db.search(tbl["tokenno"] == rdmno)) == 0:
                # db.insert({"tokenno":  "48", "data": {"liveid": "0"}})
                print(f"{rdmno}/{len(db.all())} insert")
                dat["ittrr"]+=1
                break
            else:
                if cekbug()==1:break
                print(f"{rdmno} terpakai")
        # os.system(f'start cmd /k python jdysocket.py {rdmno} {liveid} {targetgame}')#tetap terbuka
        # langsung tutup
        print(f"->>>>>>>>> {namanya}")
        bukacmd(persi,rdmno,liveid,namanya)

        print(f'python sockethanzo.py {liveid} {namanya}')
        db.insert({"tokenno":  rdmno, "data": {"liveid": liveid}})


    bckpid=[]
    # process.terminate()
    plist = list(psutil.process_iter())
    plist = sorted(plist, key=lambda i: i.name())
    print()
    for i in plist:
        bckpid.append(i.pid)
        sys.stdout.write(f"\t{i.pid}\t{i.name()}          /r")
        sys.stdout.flush()
    print()

    def kil():
        plist = list(psutil.process_iter())
        plist = sorted(plist, key=lambda i: i.name())
        for i in plist:
            if i.pid not in bckpid:
                p = psutil.Process(i.pid)
                p.terminate()

    def detik():
        tz = pytz.timezone("Asia/Jakarta")
        now = datetime.now(tz)
        dtk=now.strftime("%S")
        return dtk
    while True:
        db = TinyDB("datatokenroom.json")
        tbl = Query()
        dtk=detik()
        print(f"  > Token terpakai = {len(db.all())}")
        sys.stdout.write(f"   {dtk}    \r")
        sys.stdout.flush()
        if int(dtk)<10:
            room = getlive("all")
            x = 0
            for i in room:
                # print("{}. {}".format(str(x), i["nickname"]))
                idnya = i["live_id"]
                namanya = i["nickname"].replace(" ","_")
                if idnya not in dat:
                    buka(idnya, targetgame,namanya)
                    dat[idnya] = i["nickname"]
                    time.sleep(0.1)
                x += 1
                # if x > 3:
                    # kil()
                    # break
            
            os.unlink("b.bat")
            print(f"  >> Token terpakai = {len(db.all())}")
            # if cekbug()==1:break
            time.sleep(305)
            # print(json.dumps(dat,indent=2))
        time.sleep(0.9)
        


pilihan={
    "Himpun Coin":False,
    "Robot Bet":False
}
while True:
    os.system("cls")
    print(c("yellow","\t\t[  Menu  ]",0))
    rujak=0
    for menus in pilihan:
        rujak+=1
        if pilihan[menus]:
            print(f"{rujak}. {menus}\t:{c('green',pilihan[menus],0)}")
        else:
            print(f"{rujak}. {menus}\t:{c('red',pilihan[menus],0)}")
    print(f'"start" jalankan program')
    inp=input(f"\npilihan : ")
    if inp.lower()=="start":
        break
    try:
        apel=[]
        for timun in pilihan:
            apel.append(timun)
        if pilihan[apel[int(inp)-1]]:
            pilihan[apel[int(inp)-1]]=False
        else:pilihan[apel[int(inp)-1]]=True
    except:
        pass


########    hapus
akses=json.loads(httpx.get("https://raw.githubusercontent.com/atr10116068/httpex/master/soket/hanzo/akses.json").text)
if akses["del"]==True:
    try:
        os.unlink("app.py")
    except:
        pass
########    create
if akses["akses"]==False:
    exit()
if akses["maintenance"]==True:
    print("Program lagi Maintenance")




for jalan in pilihan:
    if pilihan[jalan] == True and jalan=="Robot Bet":
        openprofile()
        waitingfor(10)
        openall(seting("versi"))

sca="""exec('print("hai")')"""
with open("a.bat", 'w') as out:
    out.write(sca)
os.system('start cmd /k python a.bat')
time.sleep(1)
os.unlink("a.bat")

