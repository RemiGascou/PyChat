#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
PyChat -> ServerCreateWindow

Author: Remi GASCOU
Last edited: July 2018
"""

import sys
from lib.core import PyChatInfos
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class ServerCreateWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.setWindowTitle('Create Server')
        self.setGeometry(300, 300, 300, 175)
        self._initUI()
        self.show()

    def _initUI(self):
        
        #form
        self.formWidget = QWidget(self)
        self.formlayout = QFormLayout()
        self.entry_servername = QLineEdit()
        self.formlayout.addRow("Server Name", self.entry_servername)
        self.entry_serverport = QLineEdit()
        self.entry_serverport.setInputMask('99999')
        self.formlayout.addRow("Server Port", self.entry_serverport)
        self.checkbox_password = QCheckBox()
        self.checkbox_password.clicked.connect(self._checkbox_password_Event)
        self.formlayout.addRow("Define Password", self.checkbox_password)
        self.entry_password = QLineEdit()
        self.entry_password.setEnabled(False)
        self.formlayout.addRow("Password", self.entry_password)
        self.formWidget.setLayout(self.formlayout)
        #end form

        self.submitbutton = QPushButton("Create Server", self)
        self.layout = QGridLayout()
        self.layout.addWidget(self.formWidget, 0, 0)
        self.layout.addWidget(self.submitbutton, 1, 0)
        self.setLayout(self.layout)
        
    @pyqtSlot()
    def submitCreate(self):
        data = {
            "server_name":,
            "server_port":,
            "server_password":
        }
        print(data)
    
    @pyqtSlot()
    def _checkbox_password_Event(self):
        print("Toggle", self.checkbox_password.isChecked())
        if self.checkbox_password.isChecked() :
            self.entry_password.setEnabled(True)
        else:
            self.entry_password.setEnabled(False)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ServerCreateWindow()
    sys.exit(app.exec_())
