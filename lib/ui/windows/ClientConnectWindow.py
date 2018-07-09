#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
PyChat -> ClientConnectWindow

Author: Remi GASCOU
Last edited: July 2018
"""

import sys
from lib.core import PyChatInfos
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class ClientConnectWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self._initUI()
        self.show()

    def _initUI(self):
        self.layout = QGridLayout()
        #begin form
        self.formWidget = QWidget(self)
        self.formlayout = QFormLayout()
        self.entry_pseudo = QLineEdit()
        self.formlayout.addRow("Pseudonyme", self.entry_pseudo)
        self.entry_serverip = QLineEdit()
        self.entry_serverip.setInputMask('999.999.999.999')
        self.formlayout.addRow("Server IP", self.entry_serverip)
        self.entry_serverport = QLineEdit()
        self.entry_serverport.setInputMask('99999')
        self.formlayout.addRow("Server Port", self.entry_serverport)
        self.formWidget.setLayout(self.formlayout)
        #end form
        self.submitbutton = QPushButton("Connect to Server", self)
        self.submitbutton.clicked.connect(self.submitConnect)
        self.layout.addWidget(self.formWidget, 0, 0)
        self.layout.addWidget(self.submitbutton, 1, 0)
        self.setLayout(self.layout)
        self.setGeometry(300, 300, 300, 125)
        self.setWindowTitle('Connect')

    @pyqtSlot()
    def submitConnect(self):
        data = {
            "pseudo" : self.entry_pseudo.text(),
            "server_ip" : self.entry_serverip.text(),
            "server_port" : self.entry_serverport.text(),
        }
        print(data)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ClientConnectWindow()
    sys.exit(app.exec_())
