import time
import getapi
import pytz
import random as rdm
import sys
from datetime import datetime
import ambil

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




def reset():
    acc = ambil.uid()
    if tkn2!=0:
        acc=acc[tkn1:tkn2]
    token = ambil.token()
    itr = 0
    for id in acc:
        itr += 1
        while True:
            try:
                tkn = getapi.login(id["no"], id["pass"])

                if tkn == 500:
                    print()
                    print(f'  idx : {itr+tkn1-1} [{id["no"]}] Akun atau kata sandi salah')
                    db.child("yoha").child("akun").child("results").child(itr+tkn1-1).update({"no":"kosong","pass":"t4ufiq654321"})
                    try:
                        token[itr-1+tkn1]=""
                        print(f"  add idx {itr-1+tkn1}")
                    except:
                        token.append(tkn)
                elif tkn == 0:
                    print("gagal")
                else:
                    getapi.claim(tkn, 1)
                    try:
                        token[itr-1+tkn1]=tkn
                        print(f"  timpa token lama {itr+tkn1}")
                    except:
                        token.append(tkn)
            except:
                pass
            for rdd in range(rdm.randint(ant1,ant2), 0, -1):
                sys.stdout.write(f"Wait.. {rdd} [{itr+tkn1}/{len(acc)}]     \r")
                sys.stdout.flush()
                time.sleep(1)

            if len(str(tkn))>300 or tkn in [0,500]:
                break


    tokk = {"results": token}
    try:
        db.child("yoha").child("token").update(tokk)
    except Exception as e:
        print(f"Error : {e}")
    print("dah")



tes = False
jamar = []
try:
    sys.argv[3]
    print("Test Mode...")
    tkn1,tkn2=int(sys.argv[1])-1,int(sys.argv[2])
    tes = True
except:
    tkn1,tkn2=0,0
    tes = False



def jam():
    tz = pytz.timezone("Asia/Jakarta")
    now = datetime.now(tz)
    jamm = now.strftime("%m/%d/%Y, %H:%M:%S")
    minut = now.strftime("%H%M")
    if minut == "1638" and jamm not in jamar:
        jamar.append(str(jamm))
        print("•>> "+str(jamm))
        return True
    else:
        sys.stdout.write(f"{jamm}     \r")
        sys.stdout.flush()
        return False


resetdong = False
ant1,ant2=int(input("random time 1 : ")),int(input("random time 2 : "))
while True:
    jlk = jam()
    if tes == True:
        tes = False
        jlk = True
    if jlk == False:
        pass
    else:
        resetdong = False
        tz = pytz.timezone("Asia/Jakarta")
        now = datetime.now(tz)
        jamm = now.strftime("%m/%d/%Y, %H:%M")
        print("•>> Melakukan Reset Token")
        reset()
        tz = pytz.timezone("Asia/Jakarta")
        now = datetime.now(tz)
        waktu = now.strftime("%m/%d/%Y, %H:%M")
        print(f"•>> Selesai Login")
        print(f"•>> Mulai   : {jamm}")
        print(f"•>> Selesai : {waktu}")
        print(f"•>> Jeda : {ant1} sampai {ant2} detik")

    time.sleep(1)
