import getapi,json

def art():
    tkn="Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOi8vYXBpLnlvaGEucHJvL2FwaS9hdXRoL2xvZ2luIiwiaWF0IjoxNjYxMjIwNzkzLCJleHAiOjE2NjE4MjU1OTMsIm5iZiI6MTY2MTIyMDc5MywianRpIjoiRnVPYnVBNUhuSlk5NERSUiIsInN1YiI6MzE0NDY5NiwicHJ2IjoiMjNiZDVjODk0OWY2MDBhZGIzOWU3MDFjNDAwODcyZGI3YTU5NzZmNyJ9.1wrURQpyF_r8MuayOcxQRIpjzVJlDpPcVN-kjhSqOPM"

    cet="""
       ▀      ▄▄  ▄███▄
    ▄▀▀▀▄   ▄█████████▀
    █    █  ▄██████  █▀
    █    █  ▀██████████▄
    ▀▄   ▀▀▀▀▀▀▀▀█▀▀██▀
      █  ▀▄▄    ▄▄▀   ██▀
    █▄▄▄▄▄▄▄█    ███▄▄

    """
    cet="""
    ─────█─▄▀█──█▀▄─█─────
    ────▐▌──────────▐▌────
    ────█▌▀▄──▄▄──▄▀▐█────
    ───▐██──▀▀──▀▀──██▌───
    ──▄████▄──▐▌──▄████▄──
    """
    getidroom = getapi.getroom(tkn)
    x = 1
    for idr in getidroom:
        print(f"{x}. {idr['user_nicename']}")
        x += 1
    idroom = getidroom[int(input("room no : "))-1]["stream"]
    getapi.send(tkn,idroom,cet)

