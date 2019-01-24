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

import socket
import time
from threading import *

class BroadcastListener(Thread):
    def __init__(self, output_w, ip:str, port:int):
        Thread.__init__(self)
        self.output_w = output_w
        self.ip      = ip
        self.port    = port
        self.listening = False
        self.socket  = None
        #output_w.appendPlainText("[LOG] Listening thread %s %s" % (self.ip, self.port, ))

    def run(self):
        self.listening = True
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.ip, self.port)) #try catch
        self.output_w.appendPlainText("Connected to : " + self.ip + "\n")
        while(self.listening):
            r = self.socket.recv(2048)
            if len(r) != 0 : 
                if str(r.decode("utf-8")).split(" ")[1] == "/exit": self.listening = False
                else : self.output_w.appendPlainText(str(r.decode("utf-8")))
        self.output_w.appendPlainText("Disconnected.")

    def request_stop(self):
        self.listening = False

class InputBoxWidget(QWidget):
    def __init__(self, parent):
        super(InputBoxWidget, self).__init__(parent)
        self.parent = parent
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
        self.sendbutton.clicked.connect(self.parent.sendMessage)
        
        glayout.addWidget(self.sendbutton,1,2)

        f = open("lib/ui/widgets/styles/InputBoxWidget.css",'r')
        stylesheet = "".join(f.readlines())
        f.close()
        self.setStyleSheet(stylesheet)
        self.setLayout(glayout)



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
        self._initConnect()
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
        self.setLayout(glayout)
        
    def _initConnect(self):
        self.b = BroadcastListener(self.chatbox, "localhost", 1111)
        self.b.start()

    @pyqtSlot()
    def sendMessage(self):
        msg = self.messageinbox.textfield.toPlainText()
        self.b.socket.send(bytes("[Client2] " + msg, 'utf-8'))
        print("Got :",msg)
        self.messageinbox.textfield.clear()

    @pyqtSlot()
    def addText(self, text):
        self.chatbox.appendPlainText(text)
    
    @pyqtSlot()
    def addHTML(self, htmltext):
        self.chatbox.appendHtml(htmltext)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
