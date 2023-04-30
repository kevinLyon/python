import socket
import os
from time import sleep


def data_processing():

    while True:
        os.system('cls') or None #Set for windows
        print('Waiting for a connection...')
        (client_socket, addres) = server.accept()

        if client_socket:
            os.system('cls') or None #Set for windows
            print(f'{addres[0]}: Connected!')
            while client_socket:
                
                try:
                    data = client_socket.recv(1024).decode()
                    print(f'\n[{addres[0]}]: {data}')
                except Exception as error:
                    print(f'\033[31mConnection error, or the user has been disconnected!\n{error}\033[m')
                    sleep(7)
                    break
                try:
                    client_socket.sendall(b'RECEIVED!')
                except Exception as error:
                    print(f'Error to send\n{error[0]}')


if __name__ == '__main__':

    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = ('127.0.0.1', 666)
        server.bind(server_address)
        print(f'\nListening in: ( {server_address[0]} - {str(server_address[1])} )')
        server.listen(2)
    except Exception as error:
        print(f'\033[31mError to start the server\n{error}\033[m')
    
    try:
        data_processing()
    except Exception as error:
        print(f'\033[31mError in "data_processing"\n{error}\033[m')
    