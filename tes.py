import getlive

while True:
    datt = {"idx": 1, "result": [], "rapihkanjson": [], "terfilter": []}
    sss=getlive.roomall()
    for t in sss:
        print(t["nickname"])
    input()