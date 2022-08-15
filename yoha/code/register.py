import getapi
while True:
    nomer=f'62{input("nomor : 62")}'
    getapi.sendcode(nomer)
    passwd="t4ufiq654321"
    getapi.register(nomer,passwd)

