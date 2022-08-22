import httpx,json

api="https://api.namefake.com/indonesian-indonesia/random"

def get():
    req=httpx.get(api)
    resp=req.text
    if req.status_code==200:
        dat=json.loads(resp)
        return dat
