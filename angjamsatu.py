from datetime import datetime
import pytz,sys,httpx,time,ambil,json,seting,random


# constant vars
claim = "https://wjxwd01mwyo.dt01showxx02.com/App/RedPacket/SystemReceive"  # URL goes here


def tunggu(x):
    tz = pytz.timezone("Asia/Jakarta")
    print()
    while True:
        now = datetime.now(tz)
        jamm = now.strftime("%H:%M:%S")
        sys.stdout.write(f"  {jamm}       \r")
        sys.stdout.flush()
        menit = now.strftime("%M")
        detik = now.strftime("%S")
        if int(detik) == 10:
            if int(menit)==int(x):
                break
        time.sleep(0.5)
dat={}
while True:
    tunggu("00")
    print("\tClaim Pao")
    tokk = ambil.token()
    dat["versi"]=seting.versi()
    itr=0
    for tkn in tokk:
        headers= {
            "User-Agent": f"Mozilla/5.0 (iPhone11,2; U; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/602.{random.randint(0,255)}.{random.randint(0,255)} (KHTML, like Gecko) Version/9.0 Mobile/{random.randint(11,99)}E{random.randint(111,999)} Safari/602.1",
            "BundleIdentifier": "user",
            "X-Token": tkn,
            "Accept-Encoding": "identity",
            "X-Version": dat["versi"],
            "Content-Type": "application/x-www-form-urlencoded",
            "Host": "wjxwd01mwyo.dt01showxx02.com",
            "Connection": "Keep-Alive",
        }
        param = {"type": "1", "live_room_id": ""}
        try:
            req = httpx.post(claim, data=json.dumps(param),headers=headers,  timeout=100)
            ress=req.text
            print(f"\t{itr}. {ress}")
        except:
            print("Gagal")
        itr+=1
        time.sleep(2)
    time.sleep(60)