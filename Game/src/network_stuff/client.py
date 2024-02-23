import socket
import pickle

HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 5555)) #trzeba będzie później zmienić IP


while True:


    full_msg = b""
    new_msg = True
    while True:
        msg = s.recv(16)
        if new_msg:
            print(f"New msg length {msg[:HEADERSIZE]}")
            msg_len = int(msg[:HEADERSIZE])
            new_msg = False
            
        full_msg += msg

        if len(full_msg) - HEADERSIZE == msg_len:
            print("Full msg recived")

            d = pickle.loads(full_msg[HEADERSIZE:])
            print(d)

            new_msg = True
            full_msg = b""