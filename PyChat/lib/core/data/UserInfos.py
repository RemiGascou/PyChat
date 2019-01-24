#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
PyChat -> UserInfos

Author: Remi GASCOU
Last edited: July 2018
"""

class UserInfos(object):
    """docstring for UserInfos."""
    def __init__(self):
        super(UserInfos, self).__init__()
        self.username = """"""
        self.update_data()

    def update_data(self):
        self.data = {
            "username": self.username
        }

    def gen_header(self, human_readable=False):
        if human_readable == True:
            header = json.dumps(self.data, encoding="utf-8", sort_keys=True, indent=4, separators=(',', ': '))
        else:
            header = json.dumps(self.data, encoding="utf-8", sort_keys=True, separators=(',', ': '))
        return header

    def __str__(self):
        out = """[INFO] Infos for user : """ + self.username
        for e in self.data:
            out += """\n   | """ + e + """ : """ + str(self.data[e])
        out +="""\n"""
        return out
