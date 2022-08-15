import time
import pytz
from datetime import datetime
import ambil,getapi

def proses():
    vtkn=ambil.token()
    for t in vtkn:
        getapi.claim(t,1)

tes = True
jamar = []

def jam():
    tz = pytz.timezone("Asia/Jakarta")
    now = datetime.now(tz)
    jamm = now.strftime("%m/%d/%Y, %H:%M")
    minut = now.strftime("%H%M")
    if minut == "0030" and jamm not in jamar:
        jamar.append(str(jamm))
        print("•>> "+str(jamm))
        return True
    else:
        # print(""+str(jamm))
        return False


resetdong = False
tz = pytz.timezone("Asia/Jakarta")
now = datetime.now(tz)
jamm = now.strftime("%m/%d/%Y, %H:%M")
print(jamm)
while True:
    jlk = jam()
    if tes == True:
        tes = False
        jlk = True
    if jlk == False:
        pass
    else:
        tz = pytz.timezone("Asia/Jakarta")
        now = datetime.now(tz)
        klj = now.strftime("%m/%d/%Y, %H:%M")

        resetdong = False
        print("•>> Melakukan Claim")
        proses()
        print("•>> Selesai Claim")

    time.sleep(1)
