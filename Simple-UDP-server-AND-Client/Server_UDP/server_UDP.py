import socket


def data_processing():
    while True:
        (msg, address) = serv.recvfrom(1024)
        print(f"[{address[0]}]: {msg.decode()}")

        try:
            serv.sendto(b"Received", address)
        except:
            print('Erro to Send data!')


if __name__ == "__main__":

    serv = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ('127.0.0.1', 777)
    serv.bind(server_address)

    data_processing()
