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

    # conn, address = server_socket.accept()  # accept new connection
    #
    #
    # print("Connection from: " + str(address))

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

def server_program_two():
    host = socket.gethostname()
    port = 5000  # initiate port no above 1024

    server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(2)



    filetosend = open("dir/indextwo.html", "r")
    data = filetosend.read()
    # Sending file to server-
    # Send file name
    server_socket.send("index69.html".encode(FORMAT))
    # Recieved file name confirmation from server
    msg = server_socket.recv(SIZE).decode(FORMAT)
    print(f"[SERVER]: {msg}")
    # Send file data
    server_socket.send(data.encode(FORMAT))
    # Recieved file data confirmation from server
    msg = server_socket.recv(SIZE).decode(FORMAT)
    print(f"[SERVER]: {msg}")

    filetosend.close()
    server_socket.close()  # close the connection


if __name__ == '__main__':
    #server_program()
    server_program_two()