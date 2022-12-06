import socket

SIZE = 1024
FORMAT = "utf-8"

def server_program():
    # get the hostname
    host = socket.gethostname()
    port = 5000  # initiate port no above 1024

    server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(2)

    while True:
        conn, address = server_socket.accept()  # accept new connection

        print("Connection from: " + str(address))
        # receive data stream. it won't accept data packet greater than 1024 bytes
        filename = conn.recv(SIZE).decode(FORMAT)
        print(f"[RECV] Receiving the filename.")

        file = open(filename, "w")
        conn.send("Filename received.".encode(FORMAT))

        """ Receiving the file data from the client. """
        data = conn.recv(SIZE).decode(FORMAT)
        print(f"[RECV] Receiving the file data.")
        file.write(data)
        conn.send("File data received".encode(FORMAT))

        file.close()
        conn.close()

        print(f"[DISCONNECTED] {address} disconnected.")

def server_send_file_program():
    port = 60000  # Reserve a port for your service.
    s = socket.socket()  # Create a socket object
    host = socket.gethostname()  # Get local machine name
    s.bind((host, port))  # Bind to the port
    s.listen(5)  # Now wait for client connection.

    print('Server listening....')

    while True:
        conn, addr = s.accept()  # Establish connection with client.
        print('Got connection from', addr)
        data = conn.recv(1024)
        print('Server received', repr(data))

        filename = 'textexample.txt'
        f = open(filename, 'rb')
        l = f.read(1024)
        while (l):
            conn.send(l)
            print('Sent ', repr(l))
            l = f.read(1024)
        f.close()

        print('Done sending')
        conn.send(b'Thank you for connecting')
        conn.close()



if __name__ == '__main__':
    server_program()

    #server_program_two()



# def server_program_two():
#     host = socket.gethostname()
#     port = 5000  # initiate port no above 1024
#
#     server_socket = socket.socket()  # get instance
#     # look closely. The bind() function takes tuple as argument
#     server_socket.bind((host, port))  # bind host address and port together
#
#     # configure how many client the server can listen simultaneously
#     server_socket.listen(2)
#
#
#
#     filetosend = open("dir/indextwo.html", "r")
#     data = filetosend.read()
#     # Sending file to server-
#     # Send file name
#     server_socket.send("index69.html".encode(FORMAT))
#     # Recieved file name confirmation from server
#     msg = server_socket.recv(SIZE).decode(FORMAT)
#     print(f"[SERVER]: {msg}")
#     # Send file data
#     server_socket.send(data.encode(FORMAT))
#     # Recieved file data confirmation from server
#     msg = server_socket.recv(SIZE).decode(FORMAT)
#     print(f"[SERVER]: {msg}")
#
#     filetosend.close()
#     server_socket.close()  # close the connection
