import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'ChatWidget'
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
        self.chatwidget = ChatWidget(self)
        self.setCentralWidget(self.chatwidget)
        self.show()

class ChatWidget(QWidget):
    def __init__(self, parent):
        super(ChatWidget, self).__init__(parent)
        self._initUI()
        self.show()

    def _initUI(self):
        pass


    # def _initUI(self):
    #     hbox = QHBoxLayout(self)
    #     chatBox_frame = QFrame(self)
    #     chatBox_frame.setFrameShape(QFrame.StyledPanel)
    #     chatBox_text = QTextEdit(self)
    #     #chatBox_frame.setCentralWidget(chatBox_text)
    #
    #     inputBox_frame = QFrame(self)
    #     inputBox_frame.setFrameShape(QFrame.StyledPanel)
    #
    #     mainSplitter = QSplitter(Qt.Vertical)
    #     mainSplitter.addWidget(chatBox_frame)
    #     mainSplitter.addWidget(inputBox_frame)
    #     mainSplitter.setSizes([300,50])
    #
    #     inputBox_splitter = QSplitter(Qt.Horizontal)
    #     inputBox_text = QTextEdit(self)
    #     inputBox_splitter.addWidget(inputBox_text)
    #     submitButton = QPushButton('Submit')
    #     inputBox_splitter.addWidget(submitButton)
    #     #inputBox_splitter.setSizes([100,200])
    #
    #     hbox.addWidget(mainSplitter)
    #     self.setLayout(hbox)
    #     self.show()
    #     https://www.tutorialspoint.com/pyqt/pyqt_qboxlayout_class.htm

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
