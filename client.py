from socket import *
import sys

HOST = 'localhost'
BUFSIZE = 1024
PORT = 5556

def client_socket():
    ADDR = (HOST, PORT)
    csock = socket(AF_INET, SOCK_STREAM)
    csock.connect(ADDR)

    while True:
        data = raw_input('>')
        if not data:
            break
        csock.send(data)
        data = csock.recv(BUFSIZE)

        if not data:
            break
        print data

    csock.close()
if __name__ == '__main__':
    client_socket()

__author__ = 'vishket.shriwas'
