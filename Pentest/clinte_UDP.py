#####################################
# Developed for studies             #
# Developed by: Lyon kevin          #
#####################################

import socket

#sock
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#Control not to generate DOS
som = 0

while True:

    #Send only one message
    if som < 1:
        data = 'hello :)'.encode()
        som += 1
        client.sendto(data, ("127.0.0.1", 666))
    
    #Received
    rec = client.recv(1024)
    print (f"\nAnswer: {rec.decode()}\n")
    
    #Stop
    break

#Close session
client.close()