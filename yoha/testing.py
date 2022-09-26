import sys,time

idx=0
while True:
    time.sleep(1)
    sys.stdout.write(f"{idx} \r")
    sys.stdout.flush()
    idx+=1
    if idx>20:
        break