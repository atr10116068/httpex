import getapi
import pyrebase
config = {
    "apiKey": "AIzaSyATkiylea79HwAQNoJHDa5XLCK6b7kK1Ys",
    "authDomain": "bling-1b0b0.firebaseapp.com",
    "databaseURL": "https://bling-1b0b0-default-rtdb.asia-southeast1.firebasedatabase.app",
    "projectId": "bling-1b0b0",
    "storageBucket": "bling-1b0b0.appspot.com",
    "messagingSenderId": "489126684041",
    "appId": "1:489126684041:web:0f6978ddf5f9b9929bed58"
}


firebase = pyrebase.initialize_app(config)
db = firebase.database()


while True:
    # dbb = {"results": []}
    # req = db.child('yoha').child('akun').child("results").get()
    # acc = req.val()
    # for tott in acc:
    #     dbb["results"].append(tott)

    # tet = 1
    # for ppp in dbb["results"]:
    #     print(f'  {tet}. {ppp["no"]}')
    #     tet += 1
    # print(f"  total uid : {len(dbb['results'])}")
    inpp=input("input? q to exit")
    nomer = input("\tnomor send code : ")
    if nomer.startswith("0"):
        print("auto change 0 to 62")
        nomer = "62"+nomer[1:]
    print(nomer)
    
    if inpp!="q":
        getapi.sendcode(nomer)
        
    passwd = "Hanzo123"
    vcode = input("code : ")
    getapi.registernodb(nomer, passwd, vcode)

    # passwd = "t4ufiq654321"
    # vcode = input("code : ")
    # print(getapi.register(nomer, passwd, vcode))
