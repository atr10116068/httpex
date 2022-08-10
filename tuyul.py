import json
import requests
import cekbank
import addbank
import withdraw
import getcodebind
import bindemail
import ambil

token = ambil.token()


def getinfo(x):
    uriweb = "https://wjxwd01mwyo.dt01showxx02.com/App/User_User/Info"
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
    try:
        return ress["result"]
    except:
        krm = [
            "expiret",
            0.0,
            "expiret",
            "expiret",
        ]
        return krm


menu = """---------- MENU
1. get info account
2. get info bank
3. get code email
4. bind email with code
5. add bank card
6. WD
"""
while True:
    print()
    print(menu)
    pil = input("menu ke : ")
    print()
    inp = input("token : ")

    try:
        itrr = int(inp.split(" ")[0])-1
        itrrr = int(inp.split(" ")[1])
    except:
        itrr = int(inp)-1
        itrrr = int(inp)
    if pil == "1":
        for itr in token[itrr:itrrr]:
            print(f"-----------------------------------------------")
            info = getinfo(itr)
            info["contacts"] = []
            info["achievement_icon"] = []
            for i in info:
                print(f"{i} : {info[i]}")
    elif pil == "2":
        for itr in token[itrr:itrrr]:
            info = cekbank.cek(itr)
            print(f"-----------------------------------------------")
            for ii in info['result']["card"]:
                print(json.dumps(ii, indent=2))
    elif pil == "3":
        for itr in token[itrr:itrrr]:
            email, sign = input("email : "), input("sign : ")
            binded = getcodebind.getcode(itr, email, sign)
            print(f"respon : {binded}")
    elif pil == "4":
        for itr in token[itrr:itrrr]:
            email, code = input("email : "), input("code : ")
            binded = bindemail.bind(itr, email, code)
            print(f"respon : {binded}")
    elif pil == "5":
        for itr in token[itrr:itrrr]:
            name, number = input("name : "), input("number : ")
            datatype = {
                "138": {
                    "kode": "138",
                    "nama": "gopay"
                },
                "40": {
                    "kode": "40",
                    "nama": "dana"
                },
                "272": {
                    "kode": "272",
                    "nama": "shopee pay"
                }
            }
            for i in datatype:
                print(f'--> {datatype[i]["kode"]}\t: {datatype[i]["nama"]}')

            typenya = input("kode : ")
            try:
                print(f'adding {datatype[typenya]["nama"]}')
                adding = addbank.add(itr, name, number, typenya)
                print(f"respon : {adding}")
            except:
                print("kode not found")
    elif pil == "6":
        for itr in token[itrr:itrrr]:
            money, cardid = input("money : "), input("card id : ")
            adding = withdraw.wd(itr, money, cardid)
            print(f"respon : {adding}")
