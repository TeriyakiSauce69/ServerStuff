import socket

FORMAT = "utf-8"
SIZE = 1024

def client_program():
    host = socket.gethostname()  # as both code is running on same pc
    print(host)
    port = 3500  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server
    print("Connected!")

    client_socket.send(b"PUT")

    #filename = 'indextwo.html'
    filetosend = open("dir/indextwo.html", "r")
    data = filetosend.read()
    #Sending file to server-
    #Send file name
    client_socket.send("indexdix.html".encode(FORMAT))
    #Recieved file name confirmation from server

    #Recieve confirmation from server.
    #msg = client_socket.recv(1024).decode(FORMAT)

    #print(f"[SERVER]: {msg}")

    #Send file data
    client_socket.send(data.encode(FORMAT))
    # Recieved file data confirmation from server

    #msg = client_socket.recv(SIZE).decode(FORMAT)
    #msg = client_socket.recv(1024).decode(FORMAT)

    #print(f"[SERVER]: {msg}")


    filetosend.close()
    client_socket.close()  # close the connection


if __name__ == '__main__':
    client_program()