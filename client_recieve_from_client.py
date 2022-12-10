import socket                   # Import socket module
import sys

def recieve_from_server(port_number):
    s = socket.socket()             # Create a socket object
    host = socket.gethostname()     # Get local machine name
    #port = 60000                    # Reserve a port for your service.

    port = int(port_number)

    #Connect via host and port
    s.connect((host, port))

    #Send Get as a binary. This will tell server we want a file.
    s.send(b"GET")

    #Create a new file named ______ .
    #We recieve data 1024b at a time
    #We write what to the new file.
    with open('FILE_TO_BE_RECIEVED.txt', 'wb') as f: #We will recieve
        print('file opened')
        while True:
            print('receiving data...')
            data = s.recv(1024)
            print('data=%s', (data))
            #Break while loop when we stop recieving data.
            if not data:
                break
            f.write(data)

    #Closing file and socket.

    f.close()
    print('Successfully get the file')
    s.close()
    print('connection closed')

if __name__ == '__main__':

    #recieve_from_server(sys.argv[1],sys.argv[2])
    #recieve_from_server('textexample.txt')
    #server_program()
    recieve_from_server(sys.argv[1])