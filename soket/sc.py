from textwrap import indent
from tinydb import *

db = TinyDB("data.json")
db.all()
tbl = Query()
# db.truncate()
# db.insert(dat)

# db.insert({"game": "Si", "data": {"Big": 10}})
namgame, bet, coin = input("bet : "), "Small", 5
if len(db.search(tbl["game"] == namgame)) == 0:
    print("insert")
    db.insert({"game": namgame, "data": {bet: coin}})
else:
    print("update")
    x = db.get(tbl["game"] == namgame)
    if bet in x["data"]:
        print(f">>> {bet} ada")
        xxxx = db.get(tbl["game"] == namgame)["data"]
        print(xxxx)
        awalan = db.get(tbl["game"] == namgame)["data"][bet]
        xxxx[bet] += coin
        db.update({"data": xxxx}, tbl.game == namgame)
    else:
        print(f">>>  {bet} tidak ada")
        xxxx = db.get(tbl["game"] == namgame)["data"]
        xxxx[bet] = coin
        db.update({"data": xxxx}, tbl.game == namgame)
        print(xxxx)
print(f"All table {db.all()}")
