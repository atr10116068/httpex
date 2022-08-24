import getapi
import wnrapi
import time
import pytz
import sys
from datetime import datetime
from tinydb import *

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
    arridopra=[]
    for dop in dboprator:
        print(f"{idxop}. {dop['name']}")
        arridopra.append(dop["id"])
        idxop += 1
    idxprod = 1
    ope = input("Oprator ke / loop : ")
    # for dpr in dbproduk:
    #     print(f"{idxprod}. [{dpr['price']}] {dpr['name']}")
    #     idxprod += 1

    idxprodinp = int(input("Produk ke : "))-1
    idproduk = dbproduk[idxprodinp]["id"]
    harga = dbproduk[idxprodinp]["price"]
    print(f"harga : {harga}         autoHitung : {mybalance}/{harga}={round(mybalance/harga)}")
    lup = input("ulangi hingga : ")
    
    inpjeda=input("jeda : ")
    if len(inpjeda)>1:
        jeda = int(inpjeda)
    else:
        jeda = 1
    itrx=0
    idxopra=0
    
    for lupp in range(int(lup), 0, -1):
        if ope =="loop":
            if idxopra<len(arridopra):
                idopra=arridopra[idxopra]
                idxopra+=1
            else:
                idxopra=0
        else:
            idopra=arridopra[int(ope)-1]

        try:
            psn = wnrapi.pesan(API_KEY, idproduk, idopra)
            # print(psn)
            if psn["success"] == True:
                itrx+=1
                idnum = psn["data"]["id"]
                nomer = psn["data"]["phone_number"]
                print(f"phone : {nomer}")
                getcod = getapi.sendcode(nomer)
                print(getcod)

                tz = pytz.timezone("Asia/Jakarta")
                now = datetime.now(tz)
                waktu = now.strftime("%Y-%m-%dT%H:%M:%S")

                tini.insert({"nomer":  nomer, "id": idnum, "waktu": waktu})
                mybalance -= harga
            else:
                print(psn["message"])

                if ope =="loop":
                    break
                else:
                    for rdd in range(300, 0, -1):
                        sys.stdout.write(f"Wait.. {rdd}   [{itrx}/{lup}]     \r")
                        sys.stdout.flush()
                        time.sleep(1)
        except Exception as e:
            print(f"Error : {e}")

        for rdd in range(jeda, 0, -1):
            sys.stdout.write(f"Wait.. {rdd}   [{itrx}/{lup}]     \r")
            sys.stdout.flush()
            time.sleep(1)