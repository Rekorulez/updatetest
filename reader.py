import time
import os
import requests
import json

while 1:
    nuvem = requests.get("https://raw.githubusercontent.com/Rekorulez/updatetest/master/ver.json")
    disco = open("/home/pi/updatetest/ver.json", "r").read()
    d = json.loads(disco)
    
    print(nuvem.read())
    print(d)
    
    time.sleep(10)
    #if  disco == nuvem:
    #    print("atualizado")
    #else:
    #    print("desatualizado")
    #    os.system('sudo python3 /home/pi/teste.py')
    #    break


    #time.sleep(60)
