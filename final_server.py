import socket

SIZE = 1024
FORMAT = "utf-8"


def server_program():
    # get the hostname
    host = socket.gethostname()
    port = 5000  # initiate port no above 1024
    #port = 60000  # Reserve a port for your service.

    server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(2)
    print('Server listening....')


    while True:
        conn, address = server_socket.accept()  # accept new connection

        print("Connection from: " + str(address))
            # receive data stream. it won't accept data packet greater than 1024 bytes

        data = conn.recv(1024)

        if data == b"GET":
            print("DOGECOIN!")
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
        else:
            filename = conn.recv(SIZE).decode(FORMAT)
            print(f"[RECV] Receiving the filename.")

            file = open(filename, "w")
            conn.send("Filename received.".encode(FORMAT))

            " Receiving the file data from the client."
            data = conn.recv(SIZE).decode(FORMAT)
            print(f"[RECV] Receiving the file data.")
            file.write(data)
            conn.send("File data received".encode(FORMAT))

            file.close()
            conn.close()

            print(f"[DISCONNECTED] {address} disconnected.")

if __name__ == '__main__':
    server_program()
