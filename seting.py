import requests,json,random,time,sys


def seting():
    uriweb="https://wjxwd01mwyo.dt01showxx02.com/App/Setting/Global"
    headers={
    "x-ws-apm-id":"C0A24009-062E-4AA1-9950-0023510E1A63-16",
    "user-agent":f"HS-Android Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.17{random.randint(1000,9999)}.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.{random.randint(1000,9999)}.82 Mobile Safari/537.36",
    "bundleidentifier":"user",
    "accept-encoding":"identity",
    "host":"wjxwd01mwyo.dt01showxx02.com",
    "x-version":"2.10.4",
    "connection":"keep-alive"
    }
    f=requests.get(uriweb,headers=headers)
    try:
        if f.status_code==200:
            return [f.status_code,json.loads(f.text)]
        else:
            return [f.status_code,f.text]
    except Exception as e:
        print(f"Error : {e}")

def disp(x):
    sys.stdout.write(f"\t{x}\r")
    sys.stdout.flush()

ress={"stat":999,"sett":""}
titik="."
while ress["stat"]!=200:
    disp(f"Getting Version{titik}")
    titik+="."
    ff=seting()
    try:
        ress["stat"]=ff[0]
        ress["sett"]=ff[1]
    except:
        pass
    time.sleep(1)
  
def versi():
    # return(ress["sett"]["result"]["android_user_version"])
    return "2.10.4"

def sensitif():
    return(ress["sett"]["result"]["sensitive_words"].split("#"))