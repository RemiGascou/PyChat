import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'TabManager'
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
        self.table_widget = ChatWidget(self)
        self.setCentralWidget(self.table_widget)
        self.show()

class ChatWidget(QWidget):
    def __init__(self, parent):
        super(ChatWidget, self).__init__(parent)
        self._initUI()

    def _initUI(self):
        hbox = QHBoxLayout(self)
        chatBox_frame = QFrame(self)
        chatBox_frame.setFrameShape(QFrame.StyledPanel)
        chatBox_text = QTextEdit(chatBox_frame)

        inputBox_frame = QFrame()
        inputBox_frame.setFrameShape(QFrame.StyledPanel)
        inputBox_text = QTextEdit()
        submitButton = QPushButton('Submit')

        mainSplitter = QSplitter(hbox, Qt.Vertical)
        mainSplitter.addWidget(chatBox_frame)
        mainSplitter.addWidget(inputBox_frame)
        mainSplitter.setSizes([100,200])

        inputBox_splitter = QSplitter(mainSplitter, Qt.Horizontal)
        inputBox_splitter.addWidget(inputBox_text)
        inputBox_splitter.addWidget(submitButton)
        inputBox_splitter.setSizes([100,200])

        hbox.addWidget(mainSplitter)
        self.setLayout(hbox)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
