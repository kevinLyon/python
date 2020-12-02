#####################################
# Developed for studies             #
# Developed by: Lyon kevin          #
#####################################

#Developed and tested on kali linux 2020.3

#import os
import logging

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

def main():
    # Instantiate a dummy authorizer for managing 'virtual' users
    authorizer = DummyAuthorizer()

    # Define a new user having full r/w permissions and a read-only
    authorizer.add_user('black', 'kali', '/home/black', perm='elradfmwMT')
                         #User,   Pass,   local,         Permissions
#===============================================================================
    #Anonymous user
    #authorizer.add_anonymous(os.getcwd())

    # Instantiate FTP handler class
    handler = FTPHandler
    handler.authorizer = authorizer

    # Define the message sent when connecting
    handler.banner = "FTP ready for connection."

    #Which ftpd ports will use for your passive data transfers
    handler.passive_ports = range(60000, 65535)

    #Listen to the arrival of any ip == 0.0.0.0 port 666
    address = ('', 666)
    server = FTPServer(address, handler)

    # Maximum number of simultaneous connections
    server.max_cons = 256
    #Maximum connection for IP
    server.max_cons_per_ip = 5

    #Save log to a file
    #logging.basicConfig(filename='/home/black/Desktop/login_ftp.log', level=logging.INFO)

    # start ftp server
    server.serve_forever()

if __name__ == '__main__':
    main()