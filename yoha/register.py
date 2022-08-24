import getapi
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

    nomer = input("\tnomor : ")
    if nomer.startswith("0"):
        print("auto change 0 to 62")
        nomer = "62"+nomer[1:]
    print(nomer)
    getapi.sendcode(nomer)


    # passwd = "Hanzo123"
    # vcode = input("code : ")
    # getapi.registernodb(nomer, passwd, vcode)

    passwd = "t4ufiq654321"
    vcode = input("code : ")
    print(getapi.register(nomer, passwd, vcode))
