import sys
from lib.core import PyChatInfos
from lib.ui.windows import *
from lib.ui.widgets import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class PyChatApp(QMainWindow):
    def __init__(self, parent=None):
        print("[LOG] Parent of PyChatApp", parent)
        super(PyChatApp, self).__init__()
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
        #Trick to center window
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())
        #EndTrick
        self._init_menu()
        self._init_tabs()
        self.show()

    def _init_tabs(self):
        self.tabsmanager = TabsManager(self)
        self.setCentralWidget(self.tabsmanager)

    def _init_menu(self):
        mainMenu      = self.menuBar()
        appMenu       = mainMenu.addMenu(PyChatInfos.get_name())
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
        connectButton.triggered.connect(self.start_ClientConnectWindow)
        clientMenu.addAction(connectButton)

        #serverMenu buttons
        createServerButton = QAction('Create Server', self)
        createServerButton.triggered.connect(self.start_ServerCreateWindow)
        serverMenu.addAction(createServerButton)

        #settingsMenu buttons
        viewButton = QAction('View', self)
        viewButton.triggered.connect(self.close)
        settingsMenu.addAction(exitButton)

        #helpMenu buttons
        aboutButton = QAction('About', self)
        aboutButton.triggered.connect(self.start_AboutWindow)
        helpMenu.addAction(aboutButton)
        helpMenu.addSeparator()
        debugButton = QAction('Debug', self)
        debugButton.triggered.connect(self.start_DebugWindow)
        helpMenu.addAction(debugButton)

    def start_AboutWindow(self):
        self.wAboutWindow = AboutWindow(self)
        self.wAboutWindow.show()

    def start_DebugWindow(self):
        self.wDebugWindow = DebugWindow(self)
        self.wDebugWindow.show()

    def start_ClientConnectWindow(self):
        self.wClientConnectWindow = ClientConnectWindow(self)
        self.wClientConnectWindow.show()

    def start_ServerCreateWindow(self):
        self.wServerCreateWindow = ServerCreateWindow(self)
        self.wServerCreateWindow.show()

    def closeEvent(self, event):
        quit_msg = "Are you sure you want to exit the program?"
        reply = QMessageBox.question(self, 'Exit Confirmation',
                        quit_msg, QMessageBox.Yes, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    @pyqtSlot()
    def testEvent(self):
        self.tabsmanager.on_click_close_tab()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PyChatApp()
    sys.exit(app.exec_())
