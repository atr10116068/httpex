import time
import random
import pytz
from datetime import datetime
import ambil
import sys
import getapi


def proses():
    vtkn = ambil.token()
    if tkn2!=0:
        vtkn=vtkn[tkn1:tkn2]
    xx = 1
    for t in vtkn:
        # for tp in range(1, 7, 1):
        tpp = getapi.claim(t, 1)
        # if tpp["code"] in [500, 4001]:
        #     break
        # time.sleep(2)

        xx += 1
        print("•>> ======================")
        for rdd in range(random.randint(ant1, ant2), 0, -1):
            sys.stdout.write(f" token {xx+tkn1}/{len(vtkn)+tkn1} Wait.. {rdd}   \r")
            sys.stdout.flush()
            time.sleep(1)
        print()


tes = False
jamar = []

try:
    print("Test Mode...")
    sys.argv[3]
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
    if minut == "0630" and jamm not in jamar:
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
        print("•>> Melakukan Claim")
        proses()
        tz = pytz.timezone("Asia/Jakarta")
        now = datetime.now(tz)
        waktu = now.strftime("%m/%d/%Y, %H:%M")
        print(f"•>> Selesai Claim")
        print(f"•>> Mulai   : {jamm}")
        print(f"•>> Selesai : {waktu}")
        print(f"•>> Jeda : {ant1} sampai {ant2} detik")
    time.sleep(1)