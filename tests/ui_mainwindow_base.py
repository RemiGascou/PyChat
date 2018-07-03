#https://pythonspot.com/pyqt5-tabs/

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'TabManager'
        self.left   = 0
        self.top    = 0
        self.width  = 300
        self.height = 200
        self.setWindowTitle(self.title)
        self.setAttribute(Qt.WA_DeleteOnClose)  #Kill application on close
        self.setGeometry(self.left, self.top, self.width, self.height)
        #Trick to center window
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())
        #EndTrick
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
