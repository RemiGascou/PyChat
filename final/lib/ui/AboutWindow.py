#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
PyChat -> AboutWindow

Author: Remi GASCOU
Last edited: July 2018
"""

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *



class AboutWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.label = QLabel("<b>PyChat v1.0.1 </b><br><br>(c) Rémi GASCOU<br><br>(2016 - 2018)", self)
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