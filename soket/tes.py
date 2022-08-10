import ambil
import getlive
import seting
import json
import requests


host = "https://wjxwd01mwyo.dt01showxx02.com/"


def sen(id, tok, tex):
    uri = host + "App/Live/SendMsg"
    headers = {
        "user-agent": "HS-Android Mozilla/5.0 (Linux; Android 8.5.0; Redmi 2 Plus Build/OPM1.171019.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4638.50 Mobile Safari/537.36",
        "bundleidentifier": "user",
        "x-token": tok,
        "accept-encoding": "identity",
        "x-version": persi,
        "connection": "keep-alive",
    }
    para = {"live_id": id, "content": tex}

    req = requests.get(uri, params=para, headers=headers)
    ress = json.loads(req.text)
    return ress


persi = seting.versi()
tokk = ambil.token()
token = tokk[int(input("token no : "))]
room = getlive.roomall()
for id in room:
    print(f'{id["live_id"]}-->{id["nickname"]}')
    sen()
