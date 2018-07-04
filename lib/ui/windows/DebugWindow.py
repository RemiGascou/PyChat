#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
PyChat -> DebugWindow

Author: Remi GASCOU
Last edited: July 2018
"""

import sys
from lib.core import PyChatInfos
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class DebugWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self._initUI()
        self.show()

    def _initUI(self):
        #self.label.setStyleSheet("QLabel {background-color: red;}")
        self.layout = QGridLayout()
        self.layout.addWidget(self.label, 0, 0)
        self.setLayout(self.layout)
        self.setGeometry(300, 300, 300, 100)
        self.setWindowTitle('Debug')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DebugWindow()
    sys.exit(app.exec_())
