
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


while True:
    dbb = {"results": []}
    req = db.child('yoha').child('akun').child("results").get()
    acc = req.val()
    for tott in acc:
        dbb["results"].append(tott)

    tet = 1
    for ppp in dbb["results"]:
        print(f'{tet}. {ppp["no"]}')
        tet += 1

    print(f"total uid : {len(dbb['results'])}")

    nuid = input("insert No : ")
    nupass = input("insert Pass : ")
    nuall={"no":nuid,"pass":nupass}
    dbb["results"].append(nuall)
    print(f"total uid : {len(dbb['results'])}")

    # print(json.dumps(dbb, indent=2))
    db.child("yoha").child("akun").update(dbb)
