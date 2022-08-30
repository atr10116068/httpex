# Query().field.matches(regex)

from tinydb import *
tini = TinyDB("adminbot.json")
db = Query()
print(tini.contains(db.uid == 123))
