import json,time,sys
import getapi,ambil,random

token=ambil.token()

itkn=input("Token [no] [no-no] : ")
if "-" in itkn:
    tkn1,tkn2=int(itkn.split("-")[0]),int(itkn.split("-")[1])
    luptkn=token[tkn1:tkn2]
else:
    luptkn=token[int(itkn)-1:int(itkn)]


getidroom = getapi.getroom(luptkn[0])
while True:
    rum=random.choice(getidroom)
    if "Yoha" not in rum["user_nicename"]:
        break
idstream = rum["stream"]
aidir = rum["uid"]
jeda=int(input(" Jeda out : "))

itr=0
for tok in luptkn:
    itr+=1
    vmasuk=getapi.enter(tok, aidir)
    vtimer=getapi.startwatch(tok,idstream)
    try:
        print(f'  {itr}/{len(luptkn)} {vmasuk["data"]["anchor"]["nick"]}')
        if vtimer["message"]!="OK":
            print(json.dumps(vtimer,indent=2))
    except Exception as e:
        print(f"  Error : {e}")
    time.sleep(2)

for jed in range(jeda,0,-1):
    sys.stdout.write(f"{jed}    \r")
    sys.stdout.flush()
    time.sleep(1)

for tok in luptkn:
    vquit=getapi.kuit(tok, aidir)
    print(vtimer["message"])
    time.sleep(2)