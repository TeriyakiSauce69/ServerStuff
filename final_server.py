import socket
import sys



def server_program(port_name):

    # Get the hostname.
    # From what I gather this works because it runs in the local machine.
    host = socket.gethostname()

    #host = server_name
    print(host)

    #Working with port 5000.
    port = int(port_name)
    print(port)
    #port = 5000

    # Get instance of socket.
    server_socket = socket.socket()
    # Bind takes tuple as argument, host and port, to bind them together.
    server_socket.bind((host, port))

    # How many client the server can listen to at once, I think.
    server_socket.listen(2)

    #Server is listening confirmation.
    print('Server listening....')

    #While true, keeps server on.
    while True:
        conn, address = server_socket.accept()  # Accepts new connection

        #Connection confirmation.
        print("Connection from: " + str(address))

        #Get data 1024 bytes at a time.
        data = conn.recv(1024)
        print("we get", data)
        #If client sent, GET, we will run the following code to send a file/data to a client.
        if data == b"GET":

            print("The users wants to get a file from the server. Let's give it to them.")

            #Name of file we are going to give them.

            filename = 'dir/textexample.txt'
            #filename = file_name_recieved.decode()

            #Loop to get pieces of data at a time and send it to the client.
            f = open(filename, 'rb')
            l = f.read(1024)
            while (l):
                conn.send(l)
                print('Sent ', repr(l))
                l = f.read(1024)
            f.close()

            print('Done sending')

            #conn.send(b'Thank you for connecting')

            conn.close()

        #We will revieve a file/data from a client.

        else:
            #Recieved filename from client.

            filename = conn.recv(1024).decode("utf-8")

            print("We are receiving a file from the client and we just received the filename!")

            #Recieved the filename. Use file name to create new file.
            file = open(filename, "w")

            #Tell client we recieved file name.
            #conn.send("Filename received.".encode("utf-8"))

            #" Receiving the file data from the client."
            data = conn.recv(1024).decode("utf-8")

            print("Receiving the file data.")
            #Write data to file.
            file.write(data)

            #Tell client we recieved data.
            #conn.send("File data received".encode("utf-8"))

            #Close file and socket.
            file.close()
            conn.close()

            print(f"[DISCONNECTED] {address} disconnected.")

if __name__ == '__main__':

    server_program(sys.argv[1])
    #server_program(2500)

