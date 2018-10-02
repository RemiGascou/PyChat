#!/usr/bin/env python
# coding: utf-8 

import socket
from threading import *

class ClientThread(Thread):
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

tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpsock.bind(("",1111))

while True:
    tcpsock.listen(10)
    print("En écoute...")
    (clientsocket, (ip, port)) = tcpsock.accept()
    newthread = ClientThread(ip, port, clientsocket)
    newthread.start()