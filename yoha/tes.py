from datetime import datetime
import pytz
import time

tz = pytz.timezone("Asia/Jakarta")
now = datetime.now(tz)
print(now.strftime("%M"))
