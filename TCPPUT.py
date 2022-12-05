import os
import socket
import threading
import tqdm

#nm = input("Enter nickname: ")

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096


host = "192.168.1.101"
# the port, let's use 5001
port = 5001

filename = 'dir/indextwo.html'

filesize = os.path.getsize(filename)

client = socket.socket()

client.connect((host, port))
print(f"[+] Connecting to {host}:{port}")

client.send(f"{filename}{SEPARATOR}{filesize}".encode())

progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024)

with open(filename, "rb") as f:
    while True:
        # read the bytes from the file
        bytes_read = f.read(BUFFER_SIZE)
        if not bytes_read:
            # file transmitting is done
            break
        # we use sendall to assure transimission in
        # busy networks
        client.sendall(bytes_read)
        # update the progress bar
        progress.update(len(bytes_read))
client.close()
