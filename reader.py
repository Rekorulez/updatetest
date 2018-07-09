import time
import os
import requests


while 1:
    nuvem = requests.get('https://raw.githubusercontent.com/Rekorulez/updatetest/master/ver.json')
    disco = open("ver.json")
    dd = disco.read()
    
    if  dd == nuvem:
        print("atualizado")
    else:
        print("desatualizado")
        os.system('sudo python3 /home/pi/teste.py')
        break


    time.sleep(60)
