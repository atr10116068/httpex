import ambil
import pytz
import random
from datetime import datetime
from bs4 import BeautifulSoup
import requests
import threading
import sys
import time
import json
import seting
import pyrebase
config = {
    "apiKey": "AIzaSyDo7m9xUXkOiCVjuS6kKwkLchejkUNl5IY",
    "authDomain": "attools-cc537.firebaseapp.com",
    "databaseURL": "https://attools-cc537-default-rtdb.asia-southeast1.firebasedatabase.app/",
    "projectId": "attools-cc537",
    "storageBucket": "attools-cc537.appspot.com",
    "messagingSenderId": "181490859838",
    "appId": "1:181490859838:web:426c0a2f365cec8206f66f",
    "measurementId": "G-DY46HYTHT6"
}


firebase = pyrebase.initialize_app(config)
db = firebase.database()


def getprox():
    link = "https://www.sslproxies.org/"
    req = requests.get(link)
    soup = BeautifulSoup(req.text, "lxml")

    rows = soup.find("table").find_all("tr")
    p = []
    for tr in rows:
        td = tr.find_all("td")
        rau = [str(tr.string).strip() for tr in td]
        p.append(rau)

    p.pop(0)

    allprox = []
    for y in p:
        allprox.append(f"{y[0]}:{y[1]}")
    return allprox


# constant vars
link = "https://wjxwd01mwyo.dt01showxx02.com/App/Live/RecommendList?page=1"  # URL goes here
agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"

# dynamic vars
threadLock = threading.Lock()
threads = []
num = 0


class myThread (threading.Thread):
    def __init__(self, threadID, name, counter, proxy):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.proxy = proxy

    def run(self):
        # print("Starting " + self.name)
        spam(self.name, proxy)

# Each thread runs this function once


def spam(threadName, proxy):
    try:
        headers = {
            "user-agent": agent
        }
        req = requests.get(url=link, headers=headers,
                           proxies=proxy, timeout=100)
        status = req.status_code
        req.close()
        if status == 200:
            print(f"{threadName}: Working request with proxy: {proxy}")
            db.child("proxy").push({"ip": str(proxy["https"])})
        else:
            print(f"{threadName}: Connection Code Status Error:{status}")
    except IOError:
        print(f"{threadName}: Connection error - Bad Proxy")


def getjam():
    now = datetime.now(pytz.timezone("Asia/Jakarta"))
    pj0 = now.strftime("%H")
    pj1 = now.strftime("%M")
    pj2 = now.strftime("%S")
    return [pj0, pj1, pj2]


while True:
    try:
        pj = getjam()
        sys.stdout.write(f"\t{pj[0]}:{pj[1]}:{pj[2]} \r")
        sys.stdout.flush()
        jam, menit, detik = pj[0], pj[1], pj[2]
        if detik == "00":
            if int(menit) % 1 == 0:
                proxies = getprox()[0:50]
                db.child("proxy").remove()
                for x in proxies:
                    thread = str(num)
                    num += 1
                    proxy = {
                        "https": x.strip()
                    }
                    thread = myThread(thread, "Thread-" + thread, num, proxy)
                    thread.start()

                # Wait for all threads to complete
                for t in threads:
                    t.join()

        time.sleep(1)
    except Exception as e:
        print(str(e))
        for t in range(10):
            time.sleep(1)
