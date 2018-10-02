#!/usr/bin/python3
# -*- coding: utf-8 -*-
import json

"""
PyChat -> ServerInfo

Author: Remi GASCOU
Last edited: July 2018
"""

class ServerInfos():
    """docstring for ServerInfos."""
    def __init__(self):
        super(ServerInfos, self).__init__()
        self.name               = """Server01"""
        self.motd               = """A PyChat Server"""
        self.password             = """""" #md5
        self.ip                 = "127.0.0.1"
        self.port               = 1111
        self.max_clients        = 0
        self.clients_connected  = 0
        self.update_data()

    def update_data(self):
        self.data = {
            "name": self.name,
            "password": self.password,
            "ip": self.ip,
            "port": self.port,
            "max_clients": self.max_clients,
            "clients_connected": self.clients_connected
        }

    def gen_header(self, human_readable=False):
        if human_readable == True:
            header = json.dumps(self.data, encoding="utf-8", sort_keys=True, indent=4, separators=(',', ': '))
        else:
            header = json.dumps(self.data, encoding="utf-8", sort_keys=True, separators=(',', ': '))
        return header

    def importConf(self):
        pass

    def exportConf(self):
        pass

    #Get Set s
    def get_name(self):
    	return self.name

    def set_name(self,name):
    	self.name = name

    def get_password(self):
    	return self.password

    def set_password(self,password):
    	self.password = password

    def get_ip(self):
    	return self.ip

    def set_ip(self,ip):
    	self.ip = ip

    def get_port(self):
    	return self.port

    def set_port(self,port):
    	self.port = port

    def get_max_clients(self):
    	return self.max_clients

    def set_max_clients(self,max_clients):
    	self.max_clients = max_clients

    def get_clients_connected(self):
    	return self.clients_connected

    def set_clients_connected(self,clients_connected):
    	self.clients_connected = clients_connected

    def __str__(self):
        out = """[INFO] Infos for server : """ + self.name
        for e in self.data:
            out += """\n   | """ + e + """ : """ + str(self.data[e])
        out +="""\n"""
        return out
