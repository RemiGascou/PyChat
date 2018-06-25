#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
PyChat -> AboutWindow

Author: Remi GASCOU
Last edited: July 2018
"""

import sys
from PyQt5.QtWidgets import (QWidget, QToolTip, 
    QPushButton, QApplication)
from PyQt5.QtGui import (QFont, QIcon)



class AboutWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        
        self.setWindowIcon(QIcon('../src/ico.png'))  
        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('About')    
        self.show()
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = AboutWindow()
    sys.exit(app.exec_())