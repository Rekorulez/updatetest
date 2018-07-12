import os
import glob
import time
import requests
import json

def build():
    os.system('sudo git clone https://Rekorulez:Kurosaki13@github.com/pastre/bs-tmp.git /home/pi/Update/home')       
    os.system('sudo mv /home/pi/Update/home/control /home/pi/Update/DEBIAN/')
    os.system('sudo dpkg -b /home/pi/Update')
def clean():
    os.system('sudo rm -r /home/pi/Update/home')
    os.system('sudo rm /home/pi/Update/DEDIAN/control')
    os.system('sudo dpkg -r dod-main')
def install():
    os.system('sudo dpkg -i /home/pi/Update.deb')
    os.system('sudo rm /home/pi/Update.deb')
def check():
    rr = requests.get("https://raw.githubusercontent.com/pastre/bs-tmp/master/ver.json?token=AnAQB-uISRLdxn5chbg-LY9lWajSKoHZks5bUOWdwA%3D%3D")
    nn = rr.text
    nm = json.loads(nn)

    dd = open("/home/pi/Update/home/ver.json", "r").read()
    dc = json.loads(dd)

    
    print('nuvem:')
    print(nm)
    print('disco')
    print(dc)


clean()
build()
install()

while 1:    
    rq = requests.get("https://raw.githubusercontent.com/pastre/bs-tmp/master/ver.json?token=AnAQB-uISRLdxn5chbg-LY9lWajSKoHZks5bUOWdwA%3D%3D")
    n = rq.text
    nuvem = json.loads(n)

    d = open("/home/pi/Update/home/ver.json", "r").read()
    disco = json.loads(d)

    
    print('nuvem:')
    print(nuvem)
    print('disco:')
    print(disco)
    if disco == nuvem:
        print("Up to Date")
    else:
        print("NOT up to Date")
        clean()
        build()
        install()
        check()
    time.sleep(300)




