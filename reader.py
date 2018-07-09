handle = open("ver", "r")
data = handle.read()
handle2 = open("/home/pi/ver", "r")
data2 = handle2.read()

if data == data2:
    print("atualizado")
else:
    print("desatualizado")

handle.close
handle2.close

