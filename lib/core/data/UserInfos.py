#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
PyChat -> UserInfos

Author: Remi GASCOU
Last edited: July 2018
"""

class UserInfos(object):
    """docstring for UserInfos."""
    def __init__(self, arg):
        super(UserInfos, self).__init__()
        self.arg = arg

    def gen_header(self, human_readable=False):
        if human_readable == True:
            header = json.dumps(self.data, encoding="utf-8", sort_keys=True, indent=4, separators=(',', ': '))
        else:
            header = json.dumps(self.data, encoding="utf-8", sort_keys=True, separators=(',', ': '))
        return header
