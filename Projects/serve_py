#####################################
# Developed for studies             #
# Developed by: Lyon kevin          #
#####################################

import socket

#server created
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = "0.0.0.0"
port = 666

def listen():
    #listening
    serv.bind((ip,port))
    serv.listen(5)
    print(f"Listening in: {ip}: {str(port)}")

def recv():

    #connection accepted!
    (client_socket, address) = serv.accept()
    print(f"\n{address}:connected!\n")
    print(f"\nReceived from: {address[0]}: {client_socket.recv(1024).decode()}\n")
    #Sending confirmation
    client_socket.send("Received connection".encode())
    serv.close()

def main():
    
    listen()

    try:
        recv()
    except Exception as erro:
        print(f"Error: {str(erro)}")
        serv.close()

#RUN!
main()