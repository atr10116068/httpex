import httpx
import json


def profil(API_KEY):
    param = {
        "api_key": API_KEY
    }
    uri = f'https://api.wnrstore.com/api/v1/user/data?secret_key={API_KEY}'
    try:
        r = httpx.get(uri, params=param, timeout=5)
        if r.status_code == 200:
            ressx = json.loads(r.text)
            return ressx['data']
    except Exception as error:
        print(error)
    return 0


def oprator(API_KEY):
    param = {
        "api_key": API_KEY
    }
    uri = f'https://api.wnrstore.com/api/v1/operator/data?secret_key={API_KEY}'
    try:
        r = httpx.get(uri, params=param, timeout=5)
        if r.status_code == 200:
            ressx = json.loads(r.text)
            return ressx['data']
    except Exception as error:
        print(error)
    return 0


def produk(API_KEY):
    param = {
        "api_key": API_KEY
    }
    uri = f'https://api.wnrstore.com/api/v1/product/data?secret_key={API_KEY}'
    try:
        r = httpx.get(uri, params=param, timeout=5)
        if r.status_code == 200:
            ressx = json.loads(r.text)
            return ressx['data']
    except Exception as error:
        print(error)
    return 0


def pesan(API_KEY, idprod, idopra):
    param = {
        "id_product": idprod,
        "id_operator": idopra,
    }
    uri = f'https://api.wnrstore.com/api/v1/order/create?secret_key={API_KEY}'
    try:
        r = httpx.post(uri, data=param, timeout=5)
        if r.status_code == 200:
            ressx = json.loads(r.text)
            return ressx
    except Exception as error:
        print(error)
    return 0


def otp(API_KEY):
    uri = f'https://api.wnrstore.com/api/v1/order/data?secret_key={API_KEY}'
    try:
        r = httpx.get(uri)
        if r.status_code == 200:
            ressx = json.loads(r.text)
            return ressx
    except Exception as error:
        print(error)
    return 0


def cancel(API_KEY, idnum):
    param = {
        "id": idnum,
    }
    uri = f'https://api.wnrstore.com/api/v1/order/cancel?secret_key={API_KEY}'
    try:
        r = httpx.post(uri, data=param, timeout=5)
        if r.status_code == 200:
            ressx = json.loads(r.text)
            return ressx
    except Exception as error:
        print(error)
    return 0
