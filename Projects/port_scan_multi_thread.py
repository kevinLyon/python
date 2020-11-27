#####################################
# Developed for studies             #
# Developed by: Lyon kevin          #
#####################################

from threading import Thread
from time import sleep
import socket
import sys

argment = sys.argv
ports_list = [1]
target = 'ip alvo'

#creat port--
while len(ports_list) < 65535:
    ports_list.append(int(1 + ports_list[-1]))

sleep(3)

#check door open:
def scan(n1, n2):
    for port in ports_list[n1:n2]:
        boot = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        boot.settimeout(0.8)
        code = boot.connect_ex((target, port))
        #print(f"scanner {port}")
        if code == 0:
            print(f"\033[41mporta {port} aberta\033[m")
        else:
            None

#O final da thread de cima é o inicio da thread de baixo!!!
#creat Threads
Thread1 = Thread(target=scan, args=[0, 4369])
Thread2 = Thread(target=scan, args=[4369, 8738 ])
Thread3 = Thread(target=scan, args=[8738, 13107])
Thread4 = Thread(target=scan, args=[13107, 17476])
Thread5 = Thread(target=scan, args=[17476, 21845])
Thread6 = Thread(target=scan, args=[21845, 26214])
Thread7 = Thread(target=scan, args=[26214, 30583])
Thread8 = Thread(target=scan, args=[30583, 34952])
Thread9 = Thread(target=scan, args=[34952, 39321])
Thread10 = Thread(target=scan, args=[39321, 43690])
Thread11 = Thread(target=scan, args=[43690, 48059])
Thread12 = Thread(target=scan, args=[48059, 52428])
Thread13 = Thread(target=scan, args=[52428, 56797])
Thread14 = Thread(target=scan, args=[56797, 61166])
Thread15 = Thread(target=scan, args=[61166, 65535])

#start
Thread1.start()
Thread2.start()
Thread3.start()
Thread4.start()
Thread5.start()
Thread6.start()
Thread7.start()
Thread8.start()
Thread9.start()
Thread10.start()
Thread11.start()
Thread12.start()
Thread13.start()
Thread14.start()
Thread15.start()