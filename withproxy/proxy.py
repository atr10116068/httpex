import requests
import json

proxies = {
    "https": "8.219.97.248:80"
}


try:
    print(proxies)
    r = requests.get('https://httpbin.org/ip', proxies=proxies)
    x = r.text
    print(x)
except:
    print("gagal")
