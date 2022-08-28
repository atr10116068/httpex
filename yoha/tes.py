import getapi
import json
import time


def art():
    tkn = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOi8vYXBpLnlvaGEucHJvL2FwaS9hdXRoL2xvZ2luIiwiaWF0IjoxNjYxNjg2NzMxLCJleHAiOjE2NjIyOTE1MzEsIm5iZiI6MTY2MTY4NjczMSwianRpIjoibU9WeHJGMkYwT3hnSWh0VyIsInN1YiI6MjU2MTc0NiwicHJ2IjoiMjNiZDVjODk0OWY2MDBhZGIzOWU3MDFjNDAwODcyZGI3YTU5NzZmNyJ9.6mRPCyYweZU4HPAiqUqXoK4-eSoiGO1apFiAdrYW1Kw"

    cet = """
       ▀      ▄▄  ▄███▄
    ▄▀▀▀▄   ▄█████████▀
    █    █  ▄██████  █▀
    █    █  ▀██████████▄
    ▀▄   ▀▀▀▀▀▀▀▀█▀▀██▀
      █  ▀▄▄    ▄▄▀   ██▀
    █▄▄▄▄▄▄▄█    ███▄▄

    """
    # cet="""
    # ─────█─▄▀█──█▀▄─█─────
    # ────▐▌──────────▐▌────
    # ────█▌▀▄──▄▄──▄▀▐█────
    # ───▐██──▀▀──▀▀──██▌───
    # ──▄████▄──▐▌──▄████▄──
    # Good Night :)
    # """
    getidroom = getapi.getroom(tkn)
    x = 1
    for idr in getidroom:
        print(f"{x}. {idr['user_nicename']}")
        x += 1
    idroom = getidroom[int(input("room no : "))-1]["stream"]
    # while True:
    getapi.send(tkn, idroom, cet)
    time.sleep(1)


art()
