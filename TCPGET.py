import socket

#from socket import *
#import socket
import sys

#serverPort = 80
def client_program():
    serverPort = 80

    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print ("Socket successfully created")

    host_ip = socket.gethostbyname('www.google.com')

    serverSocket.connect((host_ip, serverPort))

    serverSocket.send(b"GET / HTTP/1.1\r\nHost:www.google.com\r\n\r\n")

    response = serverSocket.recv(4096)
    print(response.decode())
    serverSocket.close()

def client_program_local():
    # serverPort = 5000
    #
    # serverSocket = socket.socket()
    # print ("Socket successfully created")
    #
    # #host_ip = socket.gethostbyname('www.google.com')
    # host_ip = socket.gethostname()
    #
    # serverSocket.connect((host_ip, serverPort))
    #
    # #serverSocket.send(b"GET / HTTP/1.1\r\nHost:www.google.com\r\n\r\n")
    # serverSocket.send(b"GET / HTTP/1.1\r\nHost:DESKTOP-DEASSRC\r\n\r\n")
    #
    # response = serverSocket.recv(4096)
    # print(response.decode())
    # serverSocket.close()

    s = socket.socket()  # Create a socket object
    host = socket.gethostname()  # Get local machine name
    port = 5000  # Reserve a port for your service.

    s.connect((host, port))


    with open('received_file.txt', 'wb') as f:
        print('file opened')
        while True:
            print('receiving data...')
            data = s.recv(1024)
            print('data=%s', (data))
            if not data:
                break
            # write data to a file
            f.write(data)

    f.close()
    print('Successfully get the file')
    s.close()
    print('connection closed')

if __name__ == '__main__':
    #client_program()
    client_program_local()