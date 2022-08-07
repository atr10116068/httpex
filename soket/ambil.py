
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


def token():
    req = db.child('account').child('token').get()
    acc = req.val()["results"]
    return acc


def tokenhost():
    req = db.child('account').child('host').get()
    acc = req.val()["token"]
    return acc


def proxy():
    req = db.child('proxy').get()
    acc = req.val()
    bckip = []
    for p in acc:
        bckip.append(acc[p]["ip"])

    wadah = []

    import requests
    import threading
    # constant vars
    link = "https://wjxwd01mwyo.dt01showxx02.com/App/Setting/Global"  # URL goes here

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
                "x-ws-apm-id": "C0A24009-062E-4AA1-9950-0023510E1A63-16",
                "user-agent": "HS-Android Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.171019.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.87 Mobile Safari/537.36",
                "bundleidentifier": "user",
                "accept-encoding": "identity",
                "host": "wjxwd01mwyo.dt01showxx02.com",
                "x-version": "2.10.2.4",
                "connection": "keep-alive"
            }
            req = requests.get(url=link, headers=headers,
                               proxies=proxy, timeout=10)
            status = req.status_code
            req.close()
            if status == 200:
                print(f"{threadName}: Working request with proxy: {proxy}")
                wadah.append(proxy)
            else:
                print(f"{threadName}: Connection Code Status Error:{status}")
        except IOError:
            print(f"{threadName}: Connection error - Bad Proxy")

    for x in bckip:
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

    return wadah


def uid():
    uid = db.child('account').child('uid').get()
    acc = uid.val()["results"]
    return acc
