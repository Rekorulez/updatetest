import time
import os


while true:
    os.system('sudo rm /home/pi/ver')
    os.system('sudo wget https://raw.githubusercontent.com/Rekorulez/updatetest/master/ver')
    handle = open("ver", "r")
    data = handle.read()
    handle2 = open("/home/pi/ver", "r")
    data2 = handle2.read()

    if data == data2:
        print("atualizado")
    else:
        print("desatualizado")
        os.system('sudo python3 /home/pi/teste.py')
        break

    handle.close
    handle2.close
    time.sleep(60)
