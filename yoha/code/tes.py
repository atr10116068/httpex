import ambil,getapi

tkns=ambil.token()
rrm=getapi.getroom(tkns[2])

x=1
print(f"\tvuid\tvroom_id\t\tvtiket\tvstream\t\t\tvnama")
if rrm != 0:
    for dtr in rrm:
        vnama= dtr["user_nicename"]
        vuid= dtr["uid"]
        vroom_id= dtr["room_id"]
        vtiket= dtr["ticket_id"]
        vstream= dtr["stream"]
        print(f"{x}. \t{vuid}\t{vroom_id}\t{vtiket}\t{vstream}\t{vnama}")
        x+=1


idrx=int(input("room nomor : "))
trgt=rrm[idrx-1]
sid=trgt["stream"]

tno=input("mode no/loop: ")
while True:
    if tno == "loop":
        for tkn in tkns:
            mmsg=input("Msg : ")
            print(getapi.send(tkn,sid,mmsg))
    else:
        tkn=tkns[int(tno)-1]
        mmsg=input("Msg : ")
        print(getapi.send(tkn,sid,mmsg))


