from tinydb import *

db = TinyDB("database.json")
sett = db.table('setting')
q = Query()
sett.truncate()


sett.insert_multiple([
    {'profile': 'tkn', 'val': "0"},
    {'profile': 'pola', 'val': "terkecil"},
    {'profile': 'detik', 'val': "8"},
    {'profile': 'maxbet', 'val': "1"},
    {'profile': 'persenan', 'val': "0.3"},
    {'profile': 'roomid', 'val': "0"},
    {'profile': 'batas any', 'val': "0"},
])

menus="""
1. tkn
2. pola [terkecil/terbesar]
3. detik
4. maxbet
5. persenan
6. roomid
7. batas any
"""
pildat={
    "1":"tkn",
    "2":"pola",
    "3":"detik",
    "4":"maxbet",
    "5":"persenan",
    "6":"roomid",
    "7":"batas any",
}
while True:
    pil=input(f"{menus}pilihan : ")
    try:
        sett.update({'val': input(f"{pildat[pil]}\t:")}, where('profile') == pildat[pil])
    except:
        print("pilihan tidak ada")
    print("\t\t[ Settings ]")
    for tkk in sett:
        dips=tkk['profile']
        if len(tkk['profile'])<6:
            dips=tkk['profile']+"    "
        print(f"  {dips}\t:{tkk['val']}")

# find key
    # result = sett.search(q.profile == 'detik')[0]["val"]
    # print(result)


#update key
# sett.update_multiple([
#     ({'val': "turun"}, where('profile') == 'pola'),
#     ({'val': 8}, where('profile') == 'detik'),
#     ({'val': 0.2}, where('profile') == 'persenan'),
#     ({'val': 10}, where('profile') == 'maxbet'),
#     ])
