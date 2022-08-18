import getapi
import wnrapi
import time
import os
import pyrebase
from tinydb import *
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
tini = TinyDB("wnrotp.json")


# data wnr
API_KEY = "bb70dfdd-bc0b-5066-a985-66dbed98ad3a"
profil = wnrapi.profil(API_KEY)
mybalance = profil["balance"]
print("\n_______________________________________")
print("\t\t[ Profile WNR ]")
for pwnr in profil:
    disp = ""
    disp += pwnr+"\t"
    # print(len(disp))
    if len(disp) <= 8:
        disp += "\t"
    disp += ": "
    disp += str(profil[pwnr])
    print(disp)
print("_______________________________________\n")

dboprator = wnrapi.oprator(API_KEY)
dbproduk = wnrapi.produk(API_KEY)
while True:
    print(f"Balance : {mybalance}")
    idxop = 1
    for dop in dboprator:
        print(f"{idxop}. {dop['name']}")
        idxop += 1
    idopra = dboprator[int(input("Oprator ke : "))-1]["id"]
    idxprod = 1
    for dpr in dbproduk:
        print(f"{idxprod}. [{dpr['price']}] {dpr['name']}")
        idxprod += 1

    idxprodinp = int(input("Produk ke : "))-1
    lup = input("ulangi hingga : ")
    idproduk = dbproduk[idxprodinp]["id"]
    print(idopra)
    print(idproduk)
    harga = dbproduk[idxprodinp]["price"]
    for lupp in range(int(lup), 0, -1):
        psn = wnrapi.pesan(API_KEY, idproduk, idopra)
        if psn["success"] == True:
            idnum = psn["data"]["id"]
            nomer = psn["data"]["phone_number"]
            print(f"phone : {nomer}")
            getcod = getapi.sendcode(nomer)
            print(getcod)
            tini.insert({"nomer":  nomer})
            mybalance -= harga
        time.sleep(20)
