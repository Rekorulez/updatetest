import time
import os

i = 1
while i == 1:
    os.system('sudo rm /home/pi/ver')
    os.system('sudo wget https://raw.githubusercontent.com/Rekorulez/updatetest/master/ver')
    handle = open("ver", "r")
    data = handle.read()
    handle2 = open("/home/pi/ver", "r")
    data2 = handle2.read()
    print(data)
    print(data2)
    time.sleep(5)

    if data == data2:
        print("atualizado")
    else:
        print("desatualizado")
        os.system('sudo python3 /home/pi/teste.py')
        i = 0

    handle.close
    handle2.close
    time.sleep(60)
