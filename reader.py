import time
import os
import requests
import json

while 1:
    nuvem = requests.get("https://raw.githubusercontent.com/Rekorulez/updatetest/master/ver.json")
    disco = json.loads("/home/pi/updatetest/ver.json")
    
    if  disco == nuvem:
        print("atualizado")
    else:
        print("desatualizado")
        os.system('sudo python3 /home/pi/teste.py')
        break


    time.sleep(60)
