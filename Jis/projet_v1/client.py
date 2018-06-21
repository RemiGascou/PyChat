#!/usr/bin/env python
# coding: utf-8

import socket
import time
from threading import *

class BroadcastListener(Thread):
    def __init__(self, ip:str, port:int):
        Thread.__init__(self)
        self.ip         = ip
        self.port       = port
        self.listening  = False
        self.socket     = None
        print("[LOG] Listening thread %s %s" % (self.ip, self.port, ))

    def run(self):
        self.listening = True
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.ip, self.port)) #try catch
        print("Connected to",self.ip)
        while(self.listening):
            r = self.socket.recv(2048)
            if len(r) != 0 : print("[IN] : ",str(r.decode("utf-8")), sep="")

    def send(self, strin:str):
        self.socket.send(bytes(strin, 'utf-8'))

    def stop(self):
        self.listening = False
        self.socket.close()


print("Broadcast from server :")
b = BroadcastListener("localhost", 1111)
b.start()
s = ""
while s != "*":
    s = input(">>> ")
    b.send(s)
b.stop()