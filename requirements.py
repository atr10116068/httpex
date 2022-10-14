import os,pkg_resources
os.system(f'start cmd /c python -m pip install --upgrade pip')

def cekpkg():
    needtoinstall={}
    vreq={
        "httpx":"0.13.3",
        "tinydb":"4.7.0",
        "requests":"2.27.1",
        "pytz":"2022.1",
        "pyrebase4":"4.4.1",
        "colorama":"0.4.4",
        "psutil":"5.9.1",
        "websocket-client":"1.3.1",
        "websockets":"10.3",
        "orderedset":"2.0.3",
    }
    installed_packages = pkg_resources.working_set
    pkginstalled={}
    for ipin in installed_packages:
        pkginstalled[ipin.key]=ipin.version
    
    for upin in vreq:
        if upin in pkginstalled:
            print(f"installed {upin}")
        else:
            print(f"not installed {upin}")
            needtoinstall[upin]=vreq[upin]
    return(needtoinstall)

def installing(dicc):
    for poi in dicc:
        os.system(f'start cmd /c python -m pip install {poi}=={dicc[poi]}')

vcek=cekpkg()
installing(vcek)