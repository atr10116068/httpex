import websockets
import asyncio
import json
import random as rd
import requests

dat = {"result": []}


def roomss(tkn, x):
    uriweb = "https://wjxwd01mwyo.dt01showxx02.com/App/Live/index?category_id=3&page=" + \
        str(x)
    headers = {
        "user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.171019.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36",
        "bundleidentifier": "user",
        "x-token": tkn,
        "accept-encoding": "identity",
        "x-version": "2.9.12",
        "host": "wjxwd01mwyo.dt01showxx02.com",
        "connection": "keep-alive"
    }
    f = requests.get(uriweb, headers=headers)
    lol = json.loads(f.text)
    return lol


token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJuYmYiOjE2NTk3MDQxMTYuODQ5OTk5LCJpYXQiOjE2NTk3MDQxMTYuODQ5OTk5LCJleHAiOjE2NjA5MTM3MTYuODQ5OTk5LCJpZCI6NzA5MDA4NCwic2hvd19pZCI6IjE3MDg0MzQ0NjciLCJzdGF0dXMiOiIxIiwidHlwZSI6IjIiLCJsZXZlbCI6IjEiLCJ2aXAiOjEsImxhc3RfYWN0aXZlX2RldmljZSI6MX0.HjeOXZ3d_yl_Jt-FLWCoWj60BdmdOZiAjiRDEICOk88"


datan = b"ping"
uriweb = "wss://yoogs01wltb.dt01showxx03.com/?token="+token
param = {
    "X-Ws-APM-Id": "F751DAEA-8719-4468-B46F-A77B4D266C7B-80 ",
    "Upgrade": "websocket ",
    "Connection": "Upgrade ",
    "Sec-WebSocket-Key": "h8/MDbq2tOqS0Xy5f7vsGQ== ",
    "Sec-WebSocket-Version": " 13 ",
    "Sec-WebSocket-Extensions": "permessage-deflate ",
    "Host": "yoogs01wltb.dt01showxx03.com ",
    "Accept-Encoding": "gzip ",
    "User-Agent": "Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.171019.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36",
}


async def test():
    async with websockets.connect(uriweb) as websocket:
        await websocket.send(datan)
        while True:
            response = await websocket.recv()
            print(response)

asyncio.get_event_loop().run_until_complete(test())
