import socket

SIZE = 1024
FORMAT = "utf-8"

def client_program():
    host = socket.gethostname()  # as both code is running on same pc
    print(host)
    port = 5000  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server
    # conn, address = server_socket.accept()  # accept new connection

    while True:


        # receive data stream. it won't accept data packet greater than 1024 bytes
        filename = client_socket.recv(SIZE).decode(FORMAT)
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