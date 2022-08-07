from tinydb import *
import time
import os


while True:
    try:
        os.system('cls')
        db = TinyDB("data.json")
        xs = db.all()
        for x in xs:
            print(f'________[ {x["game"]} ]_______')
            for xxx in x["data"]:
                print(f'{xxx}:{x["data"][xxx]}')
        time.sleep(0.3)
    except:
        print("error")
        time.sleep(1)
