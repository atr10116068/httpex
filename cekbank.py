import requests
import json


def cek(x):
    uriweb = "https://wjxwd01mwyo.dt01showxx02.com/App/Pay_BankCard/Mine"
    headers = {
        "user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.171019.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36",
        "bundleidentifier": "user",
        "x-token": x,
        "accept-encoding": "identity",
        "host": "wjxwd01mwyo.dt01showxx02.com",
        "connection": "keep-alive"
    }
    f = requests.get(uriweb, headers=headers)
    ress = json.loads(f.text)
    try:
        return ress
    except:
        print("Token Expiret")
        return 0
