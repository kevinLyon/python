import socket
import os

def data_processing():

    os.system('cls') or None #Set for windows
    print('Type "exit." to exit')
    while True:
        
        data_raw = input('\nSend a message to the server: ')
        if data_raw == 'exit.':
            client.close()
            break

        date_byte = bytes(data_raw, 'utf-8')
        client.send(date_byte)

        pacotes_recebidos = client.recv(1024).decode()
        print(pacotes_recebidos)


if __name__ == '__main__':

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(1)

    try:
        client.connect(("127.0.0.1", 666))
    except Exception as error:
        client.close()
        print(f'Connection failed\n{error}')
        print(erro)
    
    try:
        data_processing()
    except Exception as error:
        print(f'Error in "data_processing"\n{error}')
