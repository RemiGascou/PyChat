#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
PyChat -> AboutWindow

Author: Remi GASCOU
Last edited: July 2018
"""

import sys
from lib.core import PyChatInfos
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class AboutWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.label = QLabel("<b>" + PyChatInfos.get_name() + " " + PyChatInfos.get_version() + " </b><br><br>" + PyChatInfos.get_credits(), self)
        self.label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.label.setAlignment(Qt.AlignCenter)
        #self.label.setStyleSheet("QLabel {background-color: red;}")

        self.layout = QGridLayout()
        self.layout.addWidget(self.label, 0, 0)
        self.setLayout(self.layout)
        self.setGeometry(300, 300, 300, 100)
        self.setWindowTitle('About')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AboutWindow()
    sys.exit(app.exec_())
