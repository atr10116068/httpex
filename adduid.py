
import subprocess
import pyrebase
import json
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
patt = input("path packages : ")
patt = patt.replace("\\", "/")


while True:
    dbb = {"results": []}
    req = db.child('account').child('uid').child("results").get()
    acc = req.val()
    for tott in acc:
        dbb["results"].append(tott)

    # dbb["results"][1] = {"appsflyer_id": "1659116438820-1239098700765885385", "check_type": "0", "device_id": "Android_SM-J730F_com.dt01usera.ghjb_742E71268039A76A2011F34A2144F132",
    #                      "force_new": "2", "invite_code": "", "registration_id": "18071adc03cc524e255", "sign": "bf19ff6a5789fcd53fd2f8c9d2146098"}
    tet = 1
    for ppp in dbb["results"]:
        print(f'{tet}. {ppp["sign"]}')
        tet += 1

    print(f"total uid : {len(dbb['results'])}")

    nuid = json.loads(input("insert UID : "))
    dbb["results"].append(nuid)
    print(f"total uid : {len(dbb['results'])}")

    # print(json.dumps(dbb, indent=2))
    db.child("account").child("uid").update(dbb)
    input("Press Enter to Delete Packages")
    process = subprocess.Popen(['rm', '-rf', f'{patt}/packages'])
