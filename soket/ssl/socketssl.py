import ambil
import asyncio
import ssl
import websockets
import certifi
import logging

#todo kluge
#HIGHLY INSECURE
ssl_context = ssl.SSLContext()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE
#HIGHLY INSECURE
#todo kluge

tokk = ambil.token()
token = tokk[int(input("token no : "))]
datan = b"ping"
uriweb = "wss://dt001wsgew.qrdnk.cn/?token="+token


logging.basicConfig(filename="client.log", level=logging.DEBUG)
ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
ssl_context.load_verify_locations(certifi.where())

async def test():
    uri = uriweb
    async with websockets.connect(
        uri, ssl=ssl_context
    ) as websocket:

        await websocket.send(datan)
        print("> test")

        response = await websocket.recv()
        print(f"< {response}")

asyncio.get_event_loop().run_until_complete(test())