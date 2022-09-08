import httpx,random,json,seting

def getsmscode():
    uri = "https://wjxwd01mwyo.dt01showxx02.com/App/User_User/GetSmsCode"
    headers = {
        "User-Agent": f"HS-Android Mozilla/5.0 (Linux; Android 8.1.0; SM-J730F Build/{random.randint(1000,9999)}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.{random.randint(1000,9999)}.129 Mobile Safari/537.36",
        "BundleIdentifier": "user",
        "Accept-Encoding": "identity",
        "X-Version": seting.persi,
        "Content-Type": "application/x-www-form-urlencoded",
        "Host": "wjxwd01mwyo.dt01showxx02.com",
        "Connection": "Keep-Alive"
    }
    param = {
        "area_code":"+62",
        "type":"3",
        "phone":"85692063033",
        "sign":"3326e8611973acb61d4caafee2ef82d7",
        "token":"6644",
    }
    try:
        req = httpx.post(uri, data=json.dumps(param), headers=headers,proxies=proxx)
        ress = json.loads(req.text)
        return ress
    except Exception as e:
        print("Failed : "+str(e))
        return 0


print(getsmscode())
input("enter to exit")
