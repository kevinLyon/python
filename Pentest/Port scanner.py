#####################################
# Developed for studies             #
# Developed by: Lyon kevin          #
#####################################

import socket


ip = input("Type the IP or address: ")

ports = [1]
count = 0

#Generates the 1024 main ports:
while count < 1023:
    ports.append(int(1 + ports[count]))
    count += 1

#Check the doors:
for port in ports:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(0.05)#Time: it depends on the speed of your network
    code = client.connect_ex((ip, port))

    if code == 0:
        print(f"{port} -> Open door:")
    else:
        ''
        #print(f"\033[31m{port} -> Closed door:\033[m")

print("\nScan Finished\n")
