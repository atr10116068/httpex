import getapi,ambil,time

token=ambil.token()

mode = input("[no-no] : ")
if "-" in mode:
    ittkn = mode
    tkn1 = int(ittkn.split("-")[0])
    tkn2 = int(ittkn.split("-")[1])
    tokenlup = token[tkn1-1:tkn2-1]
    for tkn in tokenlup:
        kk=getapi.updaterandom(tkn)
        time.sleep(3)