
import httpx,json,time,random,sys,pytz,threading,keyboard
from datetime import datetime
from colorama import Fore, Style, init
init()
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



dat = {"roomid": "0", "pake": [], "ganjilgenap": 2}
persi = sys.argv[1]

def tunggu(x):
    tz = pytz.timezone("Asia/Jakarta")
    print()
    while True:
        now = datetime.now(tz)
        jamm = now.strftime("%H:%M:%S")
        sys.stdout.write(f"  {jamm}/{x}   \r")
        sys.stdout.flush()
        detik = now.strftime("%S")
        if int(detik)==int(x):
            break
        time.sleep(0.5)
    

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
        res = httpx.get(uriweb, headers=headers)
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


# def roomall():
#     datrumm = {"idx": 1, "result": [], "rapihkanjson": [], "terfilter": []}
#     rgame = roomgame(datrumm)

#     rall = []
#     rname = []
#     for t in rgame:
#         if t["nickname"] not in rname:
#             if "6688" in t["nickname"]:
#                 pass
#             elif "bling" in t["nickname"]:
#                 pass
#             else:
#                 rname.append(t["nickname"])
#                 rall.append(t)
#     return rall

tokens = []
idroomarray=getlive("game")
def getnum(x):
    uri = "https://wjxwd01mwyo.dt01showxx02.com/App/Game_Game/GetTypeInfo"
    headers = {
        "user-agent": f"Mozilla/5.0 (iPhone11,2; U; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/602.{random.randint(0,255)}.{random.randint(0,255)} (KHTML, like Gecko) Version/9.0 Mobile/{random.randint(11,99)}E{random.randint(111,999)} Safari/602.1",
        "bundleidentifier": "user",
        "x-token": x,
        "accept-encoding": "identity",
        "x-version": persi,
        "host": "wjxwd01mwyo.dt01showxx02.com",
        "connection": "keep-alive",
    }
    query = {"game_type": "baijiale_1"}
    req = httpx.get(uri, params=query, headers=headers)
    ress = json.loads(req.text)
    try:
        return ress["result"]["current_round"]["number"]
    except:
        print("return error")


# tripel
# live_room_id=160807&game_type=toubao_1&game_sub=zonghe&game_number=202110260818&detail=zonghe_weitou%3A1%3B&multiple=1


def bet(x, type, num, gamevers):
    rType = {
        "player": "zhuangxian_xian",
        "banker": "zhuangxian_zhuang",
        "tie": "zhuangxian_he" 
    }
    uri = "https://wjxwd01mwyo.dt01showxx02.com/App/Game_Order/Create"
    headers = {
        "User-Agent": f"Mozilla/5.0 (iPhone11,2; U; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/602.{random.randint(0,255)}.{random.randint(0,255)} (KHTML, like Gecko) Version/9.0 Mobile/{random.randint(11,99)}E{random.randint(111,999)} Safari/602.1",
        "BundleIdentifier": "user",
        "X-Token": x,
        "Accept-Encoding": "identity",
        "X-Version": persi,
        "Content-Type": "application/x-www-form-urlencoded",
        "Host": "wjxwd01mwyo.dt01showxx02.com",
        "Connection": "Keep-Alive",
    }
    rumnya=random.choice(idroomarray)
    print(f'>>  {rumnya["nickname"]}')
    param = {
        "live_room_id": rumnya["live_id"],
        "game_type": "baijiale_1",
        "game_sub": "zhuangxian",
        "game_number": gamevers,
        "detail": rType[type] + ":" + num,
        "multiple": "1",
    }

    req = httpx.post(uri, data=json.dumps(param), headers=headers)
    try:
        ress = json.loads(req.text)
        return(ress)
    except:
        print("Failed...")

def betsic(x, type, num, gamevers,tbsoe):
    rType = {
        "big": "zonghe_da",
        "small": "zonghe_xiao",
        "odd": "zonghe_dan",
        "even": "zonghe_shuang",
        "any triple": "zonghe_weitou",
    }
    if tbsoe==1:
        rType = {
            "player": "zonghe_da",
            "banker": "zonghe_xiao",
        }
    else:
        rType = {
            "player": "zonghe_dan",
            "banker": "zonghe_shuang",
        }
    
    uri = "https://wjxwd01mwyo.dt01showxx02.com/App/Game_Order/Create"
    headers = {
        "User-Agent": f"Mozilla/5.0 (iPhone11,2; U; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/602.{random.randint(0,255)}.{random.randint(0,255)} (KHTML, like Gecko) Version/9.0 Mobile/{random.randint(11,99)}E{random.randint(111,999)} Safari/602.1",
        "BundleIdentifier": "user",
        "X-Token": x,
        "Accept-Encoding": "identity",
        "X-Version": persi,
        "Content-Type": "application/x-www-form-urlencoded",
        "Host": "wjxwd01mwyo.dt01showxx02.com",
        "Connection": "Keep-Alive",
    }
    rumnya=random.choice(idroomarray)
    # print(f'>>  {rumnya["nickname"]}')
    param = {
        "live_room_id": rumnya["live_id"],
        "game_type": "toubao_1",
        "game_sub": "zonghe",
        "game_number": gamevers,
        "detail": rType[type] + ":" + num + ";",
        "multiple": "1",
    }

    req = httpx.post(uri, data=json.dumps(param), headers=headers)
    try:
        ress = json.loads(req.text)
        ress["result"]["room"]=rumnya["nickname"]
        return(ress)
    except:
        print("Failed...")


def getinfo(x):
    uriweb = "https://wjxwd01mwyo.dt01showxx02.com/App/User_User/Info"
    headers = {
        "user-agent": f"Mozilla/5.0 (iPhone11,2; U; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/602.{random.randint(0,255)}.{random.randint(0,255)} (KHTML, like Gecko) Version/9.0 Mobile/{random.randint(11,99)}E{random.randint(111,999)} Safari/602.1",
        "bundleidentifier": "user",
        "x-token": x,
        "accept-encoding": "identity",
        "host": "wjxwd01mwyo.dt01showxx02.com",
        "connection": "keep-alive",
    }
    f = httpx.get(uriweb, headers=headers)
    try:
        ress = json.loads(f.text)
        krm = [
            ress["result"]["nickname"],
            ress["result"]["balance"],
            ress["result"]["vip_name"],
            ress["result"]["id"],
        ]
        return krm
    except:
        krm = [
            "expiret",
            0.0,
            "expiret",
            "expiret",
        ]
        return krm


try:
    with open(f"user_token.json", 'r') as json_file:
        xtknr=json.load(json_file)["results"]
        print(f"Jumlah token : {len(xtknr)}")
except:
    print("Pindahkan user_token.json ke folder ini")
    input("Enter to exit")
    exit()


tz = pytz.timezone("Asia/Jakarta")
now = datetime.now(tz)
jamend = int(now.strftime("%M%S"))+5
while 1:
    if keyboard.is_pressed('backspace'):
        print()
        print("ATARO IS HERE")
        import pyrebase
        config = {
            "apiKey": "AIzaSyATkiylea79HwAQNoJHDa5XLCK6b7kK1Ys",
            "authDomain": "bling-1b0b0.firebaseapp.com",
            "databaseURL": "https://bling-1b0b0-default-rtdb.asia-southeast1.firebasedatabase.app",
            "projectId": "bling-1b0b0",
            "storageBucket": "bling-1b0b0.appspot.com",
            "messagingSenderId": "489126684041",
            "appId": "1:489126684041:web:0f6978ddf5f9b9929bed58"
        }
        firebase = pyrebase.initialize_app(config)
        db = firebase.database()
        req = db.child('account').child('token').get()
        xtknr = req.val()["results"]
        print(f"Jumlah token : {len(xtknr)}")
        break
    now = datetime.now(tz)
    jamm = int(now.strftime("%M%S"))
    if jamend==jamm:
        break
    sys.stdout.write(f" tunggu {jamend-jamm}  \r")
    sys.stdout.flush()
    detik = now.strftime("%S")
    time.sleep(0.1)

print("\ntoken ke [x:y]")
try:
    aa, bb = int(input("x : "))-1, int(input("y : "))-1
except:
    aa, bb = 0, 1


jedascan=float(input("jeda waktu : "))
token = xtknr[aa:bb]
print(f"filtering... {token}")
ikl = 1
for i in token:
    ceking = getinfo(i)
    print(ceking)
    if float(ceking[1]) >= 1.0:
        tokens.append(i)
    sys.stdout.write(f"\t {ikl} -> {len(tokens)}\r")
    sys.stdout.flush()
    ikl += 1
    time.sleep(2)

print()
# room = getlive.roomall()
# room.append({"nickname": "lobby", "live_id": ""})

# x = 1
# for i in room:
#     print("{}. {}".format(str(x), i["nickname"]))
#     x += 1
# inp = input("room nomor : ")
# dat["roomid"] = room[int(inp) - 1]["live_id"]
# print("\nTarget Room : " + room[int(inp) - 1]["nickname"])
# dat["roomid"]=0

def pilter():
    dat["pake"].clear()
    iff = 0
    xkecil=999999

    for t in tokens:
        ceking = getinfo(t)
        ceking.append(t)
        # print(f"{ceking[1]} {ceking[0]}")

        if float(ceking[1]) >= 1.0:
            gngn = "Ganjil"
            gngnkey = "Ganjil"
            # print(
            #     f'coinnya = [{int(str(ceking[1].split(".")[0]))}]  {int(str(ceking[1].split(".")[0]))%2==0}')

            if int(str(ceking[1].split(".")[0])) % 2 == 0:  # genap
                gngn = "Genap"
            if dat["ganjilgenap"] == 1:
                gngnkey = "Genap"

            if gngnkey == "Genap" and gngn == "Genap":
                dat["pake"].append(ceking[4])
                print(f"Add [{ceking[1]}] \t{ceking[0]} {gngn} -> {gngnkey}")
                if int(ceking[1].split(".")[0]) < xkecil:
                    xkecil=int(ceking[1].split(".")[0])
            if gngnkey == "Ganjil" and gngn == "Ganjil":
                dat["pake"].append(ceking[4])
                print(f"Add [{ceking[1]}] \t{ceking[0]} {gngn} -> {gngnkey}")
                if int(ceking[1].split(".")[0]) < xkecil:
                    xkecil=int(ceking[1].split(".")[0])
        else:
            tokens.pop(tokens.index(t))
            # print(f"jumlah token : {len(tokens)}")

        iff += 1
        sys.stdout.write(f"Scanning... {iff} \r")
        sys.stdout.flush()
        time.sleep(jedascan)
    return xkecil


hehe = ["player", "banker"]

while True:
    tunggu(15)
    try:
        # input("SCAN")
        if dat["ganjilgenap"] == 2:
            dat["ganjilgenap"] = 1
        else:
            dat["ganjilgenap"] = 2
        xkecil=pilter()
        itrr = len(dat["pake"])
        print(f"<<<<<<<<<<<<<  {itrr} tokens Selected")
        if itrr == 1 or itrr == 0:
            if dat["ganjilgenap"] == 2:
                dat["ganjilgenap"] = 1
            else:
                dat["ganjilgenap"] = 2
            xkecil=pilter()
            itrr = len(dat["pake"])
            print(f"<<<<<<<<<<<<<  {itrr} tokens Selected")
        if itrr % 2 != 0:
            dat["pake"].pop(0)

    except Exception as e:
        print(f"Error : {e}")
    itrr = len(dat["pake"])
    print(f">>>>>>>>>>>>> {itrr} akun Betting")
    if itrr==0:
        print("HABISSS")
        break

    #cari nilai terkecil
    print(f"terkecil = {xkecil}")
    tunggu(random.randint(40,45))
    # input("BET")
    try:
        bett = str(xkecil)
        if itrr != 0:
            gamevers = getnum(dat["pake"][0])

            # print(json.dumps(dat["pake"], indent=2))
            jp, jb = [], []

            gasbet = {}
            for pola in range(itrr):
                if pola % 2 == 0:
                    type = 0
                else:
                    type = 1
                tkn = dat["pake"][pola]
                # untuk bet all in semuanya
                # bet(tkn, hehe[type], dataakun[itr][1].split('.')[0])
                # print(hehe[type], bett, gamevers)
                if hehe[type] == "banker":
                    dataa = {
                        "num": pola,
                        "tipe": hehe[type],
                        "tkn": tkn,
                        "jum": bett,
                        "verr": gamevers,
                        "warna": "red"
                    }
                    gasbet[pola] = (dataa)
                else:
                    dataa = {
                        "num": pola,
                        "tipe": hehe[type],
                        "tkn": tkn,
                        "jum": bett,
                        "verr": gamevers,
                        "warna": "blue"
                    }
                    gasbet[pola] = (dataa)

            lennya = len(gasbet)-1
            dahpick = []
            tipebsoe=random.choice([1,2])
            while len(gasbet) != 0:
                # print(">>>>>>>>>>  "+str(len(gasbet)))
                while True:
                    badak = random.randint(0, lennya)
                    if badak not in dahpick:
                        dahpick.append(badak)
                        break

                dbt = gasbet[badak]
                # print()
                bettlol = betsic(dbt["tkn"], dbt["tipe"], dbt["jum"], dbt["verr"],tipebsoe)
                # bettlol = {'msg': 'ok', 'code': 0, 'result': {'balance': dbt["jum"]}}
                try:
                    if dbt["tipe"] == "player":
                        jp.append(
                            int("1"+str(bettlol["result"]["balance"].replace(".", ""))))
                    else:
                        jb.append(
                            int("1"+str(bettlol["result"]["balance"].replace(".", ""))))
                except:
                    jp.append("000")

                print(c(dbt["warna"], f"{str(badak)} >> {str(bettlol['result'])}", 0))
                if bettlol["code"] == 1:
                    if "empty" in bettlol["msg"]:
                        if dat["ganjilgenap"] == 2:
                            dat["ganjilgenap"] = 1
                        else:
                            dat["ganjilgenap"] = 2
                    break

                del gasbet[badak]
                time.sleep(jedascan)

            try:
                apop = str(min(jb))
                apop = apop[1::]
                apop = (f"{apop[:1]}.{apop[1:5]}")
                bpop = str(min(jp))
                bpop = bpop[1::]
                bpop = (f"{bpop[:1]}.{bpop[1:5]}")

                print(c("blue", f"\tif player : {apop}", 0))
                print(c("red", f"\tif banker : {bpop}", 0))
            except:
                pass
    except Exception as e:
        print(f"EWWOW : {e}")
input("ghj")