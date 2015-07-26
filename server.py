from socket import *
from time import ctime
import threading

HOST = ''
PORT = 5555
BUFSIZE = 1024
ADDR = (HOST, PORT)

def server(address, size):
    ssock = socket(AF_INET, SOCK_STREAM)
    ssock.bind(address)
    ssock.listen(5)

    while True:
        print("Server is up!")
        csock, addr = ssock.accept()
        print('Connected to', addr)

        while True:
            data = csock.recv(size)
            if not data:
	        break

            print data, 'from', addr
            #csock.send('[%s] %s' % (ctime(), data))
            data = raw_input('>')
            csock.send(data)
        csock.close()
    ssock.close()

if __name__ == '__main__':
    threads = []

    for i in range(5):
        ADDR = (HOST, PORT + i)

	t = threading.Thread(target = server, args = (ADDR, BUFSIZE))
	threads.append(t)
	t.start()


__author__ = 'vishket.shriwas'
