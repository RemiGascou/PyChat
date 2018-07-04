import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'InputBoxWidget'
        self.left   = 0
        self.top    = 0
        self.width  = 300
        self.height = 200
        self.setWindowTitle(self.title)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setGeometry(self.left, self.top, self.width, self.height)
        #Trick to center window
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())
        #EndTrick
        self.chatwidget = InputBoxWidget(self)
        self.setCentralWidget(self.chatwidget)
        self.show()

class InputBoxWidget(QWidget):
    def __init__(self, parent):
        super(InputBoxWidget, self).__init__(parent)
        #Load Stylesheet from "InputBoxWidget.css"
        f = open("lib/ui/widgets/styles/InputBoxWidget.css",'r')
        stylesheet = "".join(f.readlines())
        f.close()
        self.setStyleSheet(stylesheet)
        #EndLoad
        self._initUI()
        self.show()

    def _initUI(self):
        self.layout = QGridLayout()
        self.layout.setSpacing(5)
        inputBox = QLineEdit()
        submitButton = QPushButton("Submit")
        submitButton.setStyleSheet("QPushButton {padding:10px; padding-top:3px; padding-bottom:3px;}")
        self.layout.addWidget(inputBox, 0, 0)
        self.layout.addWidget(submitButton, 0, 1)
        self.setLayout(self.layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
