import socket


def data_processing():

    server_address = ('127.0.0.1', 777)
    data_raw = 'Hello :)'.encode()

    try:
        client.sendto(data, server_address)
    except:
        print('Unexpected error!')
    
    try:
        data_recv = client.recv(1024)
    except:
        print('Error in [data_recv]!')
    
    if data_recv:
        print(data_recv.decode())


if __name__ == "__main__":

    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    data_processing()
