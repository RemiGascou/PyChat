import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'ChatBoxWidget'
        self.left   = 0
        self.top    = 0
        self.width  = 300
        self.height = 200
        self.setWindowTitle(self.title)
        self.setAttribute(Qt.WA_DeleteOnClose)
        #self.setGeometry(self.left, self.top, self.width, self.height)
        self.chatwidget = ChatBoxWidget(self)
        self.setCentralWidget(self.chatwidget)
        self.show()

class InputBoxWidget(QWidget):
    def __init__(self, parent):
        super(InputBoxWidget, self).__init__(parent)
        self._initUI()
        self.show()

    def _initUI(self):
        self.horizontalGroupBox = QGroupBox("Grid")
        glayout = QGridLayout()
        glayout.setColumnStretch(1, 10)
        glayout.setColumnStretch(2, 1)

        self.textfield = QPlainTextEdit(self)
        glayout.addWidget(self.textfield, 1, 1)
        self.sendbutton = QPushButton('Send')
        
        glayout.addWidget(self.sendbutton,1,2)

        f = open("lib/ui/widgets/styles/InputBoxWidget.css",'r')
        stylesheet = "".join(f.readlines())
        f.close()
        self.setStyleSheet(stylesheet)
        self.setLayout(glayout)

    @pyqtSlot()
    def getText(self):
        self.textfield


class ChatBoxWidget(QWidget):
    def __init__(self, parent):
        super(ChatBoxWidget, self).__init__(parent)
        #Load Stylesheet from "ChatBoxWidget.css"
        f = open("lib/ui/widgets/styles/ChatBoxWidget.css",'r')
        stylesheet = "".join(f.readlines())
        f.close()
        self.setStyleSheet(stylesheet)
        #EndLoad
        self.chatbox = None
        self._initUI()
        self.show()

    def _initUI(self):
        self.horizontalGroupBox = QGroupBox("Grid")
        glayout = QGridLayout()
        glayout.setRowStretch(1, 15)
        glayout.setRowStretch(2, 1)
        self.chatbox = QPlainTextEdit(parent=self)
        self.messageinbox = InputBoxWidget(parent=self)

        glayout.addWidget(self.chatbox, 1, 1)
        glayout.addWidget(self.messageinbox,2,1)
        for _ in range(20):
            self.chatbox.appendHtml("<b>Heyyy ! Line : </b>" + str(_))
        self.chatbox.appendHtml("Smiley test ! &#9762; &#9749;")

        self.setLayout(glayout)


    @pyqtSlot()
    def addText(self):
        self.chatbox.appendHtml("Smiley test ! &#9762; &#9749;")

    def addHTML(self, htmltext):
        self.chatbox.appendHtml(htmltext)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
