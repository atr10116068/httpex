import httpx,json,random
acc = {
    'appsflyer_id': '1658503928919-7127305829489203126', 
    'check_type': '0', 
    'device_id': 'Android_Redmi5Plus_com.dt01usera.ghjb_57C9F210788C30C76E1BB53694D712C4', 
    'force_new': '2', 
    'invite_code': '', 
    'registration_id': '18071adc03cc524e255', 
    'sign': '16226387a6bec9f806c2d6feec195303'
    }

def loginid(x):
    uri = "https://wjxwd01mwyo.dt01showxx02.com/App/User_LoginRegister/Login"
    headers = {
        "User-Agent": f"HS-Android Mozilla/5.0 (Linux; Android 8.1.0; SM-J730F Build/{random.randint(1000,9999)}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.{random.randint(1000,9999)}.129 Mobile Safari/537.36",
        "BundleIdentifier": "user",
        "Accept-Encoding": "identity",
        "X-Version": "2.10.4",
        "Content-Type": "application/json; charset=UTF-8",
        "Host": "wjxwd01mwyo.dt01showxx02.com",
        "Connection": "Keep-Alive"
    }
    param = x
    # kalau mau reset v1
    # param['force_new'] = '1'
    # print(param)
    # exit()

    try:
        req = httpx.post(uri, data=json.dumps(param), headers=headers)
        ress = json.loads(req.text)
        return ress
    except Exception as e:
        print("Failed : "+str(e))
        return 0