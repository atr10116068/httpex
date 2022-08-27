import getapi,json,time

def art():
    tkn="Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOi8vYXBpLnlvaGEucHJvL2FwaS9hdXRoL2xvZ2luIiwiaWF0IjoxNjYxMzY0MTkwLCJleHAiOjE2NjE5Njg5OTAsIm5iZiI6MTY2MTM2NDE5MCwianRpIjoicjFXTUY2ZkJlNHh2ekE4YSIsInN1YiI6MjYyMzY3MSwicHJ2IjoiMjNiZDVjODk0OWY2MDBhZGIzOWU3MDFjNDAwODcyZGI3YTU5NzZmNyJ9.pMF7_to8LwK56gY3Qj9njURk_q1XaeoZvklwLG_d9-0"

    cet="""
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
    getapi.send(tkn,idroom,cet)
    time.sleep(1)

art()