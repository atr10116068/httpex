import getlive



while True:
    rum=getlive.roomall()

    for t in rum:
        print(f'[{t["live_id"]}]  {t["nickname"]}')
    print(f'jumlah room : {len(rum)}')
    input(":")