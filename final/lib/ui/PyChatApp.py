import sys
from lib.core import PyChatInfos
from lib.ui import *
from lib.ui.TabsManager import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class PyChatApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title  = PyChatInfos.get_name() + " " + PyChatInfos.get_version()
        self.left   = 10
        self.top    = 10
        self.width  = 640
        self.height = 400
        self._initUI()

    def _initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self._init_menu()    
        self.table_widget = TabsManager(self)
        self.setCentralWidget(self.table_widget)    
        self.show()

    def _init_menu(self):
        mainMenu      = self.menuBar()
        appMenu       = mainMenu.addMenu('PyChat')
        clientMenu    = mainMenu.addMenu('Client')
        serverMenu    = mainMenu.addMenu('Server')
        settingsMenu  = mainMenu.addMenu('Settings')
        helpMenu      = mainMenu.addMenu('Help')

        #appMenu buttons
        exitButton = QAction(QIcon('exit24.png'), 'Exit', self)
        exitButton.setShortcut('Ctrl+Q')
        exitButton.setStatusTip('Exit application')
        exitButton.triggered.connect(self.close)
        appMenu.addAction(exitButton)

        #clientMenu buttons
        connectButton = QAction('Connect', self)
        connectButton.setShortcut('Ctrl+N')
        #connectButton.setStatusTip('Connect to a Server')
        connectButton.triggered.connect(self.close)
        clientMenu.addAction(connectButton)
        
        #serverMenu buttons
        
        #settingsMenu buttons
        
        #helpMenu buttons
        aboutButton = QAction('About', self)
        #aboutButton.triggered.connect(AboutWindow.AboutWindow()) #BUG
        helpMenu.addAction(aboutButton)

    def closeEvent(self, event):
        quit_msg = "Are you sure you want to exit the program?"
        reply = QMessageBox.question(self, 'Exit Confirmation', 
                        quit_msg, QMessageBox.Yes, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PyChatApp()
    sys.exit(app.exec_())
