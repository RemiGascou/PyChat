#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import time
from threading import *

class BroadcastListener(Thread):
    def __init__(self, ip:str, port:int):
        Thread.__init__(self)
        self.ip      = ip
        self.port    = port
        self.listening = False
        self.socket  = None
        print("[LOG] Listening thread %s %s" % (self.ip, self.port, ))

    def run(self):
        self.listening = True
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.ip, self.port)) #try catch
        print("Connected to",self.ip)
        while(self.listening):
            r = self.socket.recv(2048)
            if len(r) != 0 : 
                if str(r.decode("utf-8")).split(" ")[1] == "/exit": self.listening = False
                else : print(str(r.decode("utf-8")), sep="")
        print("Disconnected.")

    def request_stop(self):
        self.listening = False
    
    def sendMessage(self, s):
        self.socket.send(bytes(s, 'utf-8'))


if __name__ == """__main__""":
    print("Broadcast from server :")
    b = BroadcastListener("localhost", 1111)
    b.start()
    running = True
    while running:
        rin = input("[>] ")
        b.sendMessage("[Client] " + rin)
        if rin == "/exit":
            running = False
            b.sendMessage("[_DisconnectRequest_]")
    b.join()
