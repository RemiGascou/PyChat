#!/usr/bin/env python
# coding: utf-8

import socket
import time
from threading import *

class BroadcastListener(Thread):
    def __init__(self, ip:str, port:int):
        Thread.__init__(self)
        self.ip      = ip
        self.port    = port
        self.listening = False
        print("[LOG] Listening thread %s %s" % (self.ip, self.port, ))

    def run(self):
        self.listening = True
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.ip, self.port)) #try catch
        print("Connected to",self.ip)
        while(self.listening):
            r = s.recv(2048)
            if len(r) != 0 : print("[IN] : ",str(r.decode("utf-8")), sep="")
        print()
        print("Exit... :p")

    def request_stop(self):
        self.listening = False



print("Broadcast from server :")
b = BroadcastListener("localhost", 1111)
b.start()
time.sleep(2)
b.request_stop()
b.join()
