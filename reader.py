import time
import os
import requests
import json

while 1:
    req = requests.get("https://raw.githubusercontent.com/Rekorulez/updatetest/master/ver.json")
    nuvem = req.text
    n = json.loads(nuvem)
    disco = open("/home/pi/updatetest/ver.json", "r").read()
    d = json.loads(disco)
    
    print(n)
    print(d)
    
    
    if  disco == nuvem:
        print("atualizado")
    else:
        print("desatualizado")
        os.system('sudo python3 /home/pi/teste.py')
        break


    time.sleep(60)
