from datetime import datetime
import pytz,time,sys

while True:
    tz = pytz.timezone("Asia/Jakarta")
    now = datetime.now(tz)
    xx=now.strftime("%d%b%Y-%H:%M:%S")
    sys.stdout.write(f"'\t{xx} \r")
    sys.stdout.flush()
    time.sleep(0.3)