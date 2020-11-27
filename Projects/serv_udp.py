#####################################
# Developed for studies             #
# Developed by: Lyon kevin          #
#####################################

import socket

#socket
serv = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#local
ip = '0.0.0.0'
port = 666

#bind
serv.bind((ip, port))

#msg received
(msg, address) = serv.recvfrom(1024)
print(f"Message: {msg.decode()}\nReceived from: {address}")

#send msg
serv.sendto(b"Received", address)

#close session
serv.close()