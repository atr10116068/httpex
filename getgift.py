import requests
import json
import ambil


gip = {}


def getgift(x):
    uriweb = "https://wjxwd01mwyo.dt01showxx02.com/App/Gift/List"
    headers = {
        "user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.171019.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36",
        "bundleidentifier": "user",
        "x-token": x,
        "accept-encoding": "identity",
        "host": "wjxwd01mwyo.dt01showxx02.com",
        "connection": "keep-alive",
    }
    f = requests.get(uriweb, headers=headers)
    ress = json.loads(f.text)
    gip["result"] = ress["result"]


token = ambil.token()
if len(gip) == 0:
    getgift(token[0])

json_data = []
for gipacak in gip["result"]:
    json_data.append(gipacak)
newlist = sorted(json_data, key=lambda k: float(k["price"]))

print()
print("_________________________________________________________")
tt = []
for g in newlist:
    harga = g["price"]
    nama = g["name"]
    aidi = g["id"]
    if len(nama) < 9:
        nama += "       "
    print("{}\t{}\t[{}]".format(harga, nama, aidi))
print("_________________________________________________________")
input("")
