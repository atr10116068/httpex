import requests,json


def seting():
  uriweb="https://dt001piwfw.d9sph.cn/App/Setting/Global"
  headers={
    "x-ws-apm-id":"C0A24009-062E-4AA1-9950-0023510E1A63-16",
    "user-agent":"HS-Android Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.171019.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.87 Mobile Safari/537.36",
    "bundleidentifier":"user",
    "accept-encoding":"identity",
    "host":"dt001piwfw.d9sph.cn",
    "x-version":"2.10.2.4",
    "connection":"keep-alive"
  }
  f=requests.get(uriweb,headers=headers)
  return json.loads(f.text)

ress={"sett":seting()}
def versi():
  return(ress["sett"]["result"]["android_user_version"])

def sensitif():
  return(ress["sett"]["result"]["sensitive_words"].split("#"))
  
 