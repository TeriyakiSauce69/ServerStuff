import socket
import tqdm

SERVER_HOST = socket.gethostname()
SERVER_PORT = 5001

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096


serverSocket = socket.socket()


serverSocket.bind((SERVER_HOST, SERVER_PORT))
serverSocket.listen(1)
print('The server is ready to receive')
print(f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}")

#while True:
connectionSocket, addr = serverSocket.accept()
print(f"[+] {addr} is connected.")

recieved_file = connectionSocket.recv(BUFFER_SIZE).decode()

filename, filesize = recieved_file.split(SEPARATOR)

filesize = int(filesize)
progress = tqdm.tqdm(range(filesize), f"Receiving {filename}", unit="B", unit_scale=True, unit_divisor=1024)

with open(filename, "wb") as f:
    while True:
            # read 1024 bytes from the socket (receive)
        bytes_read = serverSocket.recv(BUFFER_SIZE)
        if not bytes_read:
                # nothing is received
                # file transmitting is done
            break
            # write to the file the bytes we just received
        f.write(bytes_read)
            # update the progress bar
        progress.update(len(bytes_read))


    # capitalizedSentence = sentence.upper()
    # connectionSocket.send(capitalizedSentence.
    # encode())
connectionSocket.close()
