from tkinter import W
import websocket
import json
import time
import requests
import sys
import getlive
import ambil
import translatepy as trs

dat = {"result": []}


def sen(id, x, msg):
    uri = "https://wjxwd01mwyo.dt01showxx02.com/App/Live/SendMsg"
    headers = {
        "user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.171019.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36",
        "bundleidentifier": "user",
        "x-token": x,
        "accept-encoding": "identity",
        "host": "wjxwd01mwyo.dt01showxx02.com",
        "connection": "keep-alive"
    }
    para = {"live_id": id, "content": msg}

    req = requests.get(uri, params=para, headers=headers)
    ress = json.loads(req.text)
    print(ress)


room = getlive.roomall()
x = 1
for i in room:
    print("{}. {}".format(str(x), i["nickname"]))
    x += 1

inp = input("room nomor : ")
idroom = room[int(inp)-1]["live_id"]
print("\nTarget Room : "+room[int(inp)-1]["nickname"])

tokk = ambil.token()
token = tokk[1]

dat["result"].reverse()


datan = b"ping"
uriweb = "wss://dt001wsgew.qrdnk.cn/?token="+token

param = {
    "upgrade": "websocket",
    "connection": "Upgrade",
    "Accept-Encoding": "gzip",
    "host": "yoogs01wltb.dt01showxx03.com",
    "user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.171019.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36",
}


def lagi():
    try:
        import thread
    except ImportError:
        import _thread as thread

    def on_message(ws, message):
        datadadu = json.loads(message)
        try:
            # [{
            #     'type': 'broadcast',
            #     'action': 'live_timing_message',
            #     'data': {
            #         'msg_body': {
            #             'content': 'Betting Every Day, CashBack Every Day!'}}}]
            if datadadu[0]["action"] == "live_timing_message":
                prom = datadadu[0]["data"]["msg_body"]["content"]
                prom = trs.tpy(prom, "id")[1]
                print(prom)
                if len(prom) != 0:
                    if len(prom) < 50:
                        sen(idroom, token, prom)
                        # pass
                    else:
                        sen(idroom, token, prom[0:50])
                        print("more then 50")

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
