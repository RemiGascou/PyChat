import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class App(QMainWindow):
    def __init__(self, parent=None):
        QFrame.__init__(self, parent=parent)
        self.logger = QPlainTextEdit(parent=self)
        self.logger.setReadOnly(True)
        self.logger.setLineWrapMode(QPlainTextEdit.NoWrap)
        self.logger.setMinimumWidth(1100)
        self.buffer = ''
        
        self.clear_button = QPushButton('Clear Log', parent=self)
        self.save_button = QPushButton('Save Log As...', parent=self)
        
        self.lay = QVBoxLayout(self)
        self.lay.addWidget(self.logger)
        self.lay.addWidget(self.clear_button)
        self.lay.addWidget(self.save_button) 
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())