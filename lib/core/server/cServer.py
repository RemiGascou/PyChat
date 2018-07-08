import socket
from threading import *
from lib.core.data import *

class ClientThread(Thread):
    """docstring for Server."""
    def __init__(self, ip, port, clientsocket):
        Thread.__init__(self)
        self.ip     = ip
        self.port   = port
        self.clientsocket = clientsocket
        print("[+] Nouveau thread pour %s %s" % (self.ip, self.port, ))

    def run(self):
        print("Connection de %s %s" % (self.ip, self.port, ))
        #r = self.clientsocket.recv(2048)
        mystring = "Hello <3"
        print("Sending welcome")
        self.clientsocket.send(bytes(mystring, 'utf-8'))
        print("Client déconnecté...")


class Server(Thread):
    """docstring for Server."""
    def __init__(self, data:ServerInfos):
        if type(data) == "<class ServerInfos>":
            Thread.__init__(self)
            #super(Server, self).__init__()
            self.arg = arg
        return -1

    def run(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind(("",1111))

        while True:
            sock.listen(10)
            print("En écoute...")
            (clientsocket, (ip, port)) = sock.accept()
            newthread = ClientThread(ip, port, clientsocket)
            newthread.start()

if __name__ == """__main__""":
    s = Server()
    print(s)