# -*- coding: utf-8 -*-

import socket
from threading import *
from lib.core.data import *


class Server(Thread):
    """docstring for Server."""
    def __init__(self, data:ServerInfos):
        Thread.__init__(self)
        if type(data) == "ServerInfos":
            #super(Server, self).__init__()
            pass
        self.data    = data
        self.running = True
        self.clients = []
        self.socket  = None

    def run(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind(("",1111))
        while self.running:
            self.socket.listen(10)
            print("En écoute...")
            (clientsocket, (ip, port)) = self.socket.accept()
            newthread = ClientThread(self, ip, port, clientsocket)
            newthread.start()
            self.data.clients_connected += 1
            self.clients.append(newthread)

    def requestStop(self):
        self.running = False



class ClientThread(Thread):
    """docstring for ClientThread."""
    def __init__(self, parent_server:Server, ip, port, clientsocket):
        Thread.__init__(self)
        self.parent_server  = parent_server
        self.ip             = ip
        self.port           = port
        self.clientsocket   = clientsocket
        self.motd           = "Welcome to this server\n"
        print("[+] Nouveau thread pour %s %s" % (self.ip, self.port, ))

    def run(self):
        print("Connection de %s %s" % (self.ip, self.port, ))
        r = bytes("", 'utf-8')
        self.clientsocket.send(bytes(self.motd, 'utf-8'))
        while (r != bytes("[_DisconnectRequest_]", 'utf-8')):
            r = self.clientsocket.recv(2048)
            #if len(r) != 0 :
            if len(r) != 0 : #self.clientsocket.send(r)
                for c in self.parent_server.clients: #Of Server
                    c.clientsocket.send(r)
               # self.clientsocket.send(bytes(r, 'utf-8'))
        print("Client déconnecté...")
    #
    # def orun(self):
    #     print("Connection de %s %s" % (self.ip, self.port, ))
    #     mystring = "Hello <3"
    #     print("Sending welcome")
    #     self.clientsocket.send(bytes(mystring, 'utf-8'))
    #     print("Client déconnecté...")


if __name__ == """__main__""":
    si = ServerInfos()
    serverthread = Server(si)
    print(si)
    serverthread.start()
