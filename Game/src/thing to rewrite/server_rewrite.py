import socket
import pickle
import threading
import time

class accept_conn:
    def __init__(self):
        self.look_for_connections = False
        self.first_run = True

    def run(self, server_socket, client_count):
        if self.first_run == False:
            server_socket.settimeout(1) #to robi lagi (DUŻE)
        while True:
            print("works")
            if self.look_for_connections:
                try:
                    print("Looking for connection!")
                    self.client_socket, self.adress = server_socket.accept()
                    self.clinet_count += 1
                except socket.timeout:
                    pass
    def start(self):
        self.look_for_connections = True
    
    def stop(self):
        self.look_for_connections = False


class server:
    def __init__(self):
        self.HEADERSIZE = 10
        self.adress = ""
        self.running = False
        self.clinet_count = 0
        self.accept_conn = accept_conn()
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #IPv4, TCP
        self.server_socket.bind((socket.gethostname(), 5555))
        self.server_socket.listen(5)
        self.connect = threading.Thread(target= self.accept_conn.run, args= (self.server_socket, ))

    def Run_server(self):
        self.connect.start()
        self.accept_conn.start()
        


        self.running = True
        while self.running:
            #print("running!")
            try:
                d = {1: "Hey", 2: "There"}
                msg = pickle.dumps(d)
                msg = bytes(f"{len(msg):<{self.HEADERSIZE}}", "utf-8") + msg

                self.client_socket.send(msg)
            except Exception as e:
                #print(f"Error {e}")
                pass

    def start(self):
        self.running = True
            
    def stop(self):
        self.accept_conn.stop()
        self.running = False
        self.server_socket.close()
