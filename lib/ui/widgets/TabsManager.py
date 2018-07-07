import os, sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from lib.ui.widgets import *

class App(QMainWindow):
    def __init__(self):
        super(App, self).__init__()
        self.title = 'TabsManager'
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
        self.tabsmanager = TabsManager(self)
        self.setCentralWidget(self.tabsmanager)
        self.show()

class TabsManager(QWidget):
    def __init__(self, parent):
        super(TabsManager, self).__init__(parent)
        self.layout = QVBoxLayout(self)
        # Initialize tab screen
        self.tabs = QTabWidget()
        self.tabs.resize(300,200)
        #Load Stylesheet from "TabsManager.css"
        f = open("lib/ui/widgets/styles/TabsManager.css",'r')
        stylesheet = "".join(f.readlines())
        f.close()
        #EndLoad
        self.tabs.setStyleSheet(stylesheet)
        # Add tabs
        self._init_home_tab()
        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

    def _init_home_tab(self):
        self.hometab = QWidget()
        self.hometab.layout = QVBoxLayout(self.hometab)
        self.pushButton1 = QPushButton("PyQt5 button")
        self.pushButton1.clicked.connect(self.on_click)
        self.hometab.layout.addWidget(self.pushButton1)
        self._init_tabbar(0)
        self.hometab.setLayout(self.hometab.layout)
        self.tabs.addTab(self.hometab,"Home")

    def _init_tabbar(self, k):
        tabBar = self.tabs.tabBar()
        closeButton = QPushButton()
        closeButton.setGeometry(0,0,20,20)
        closeButton.setIcon(QIcon('./cross.png'))
        closeButton.setIconSize(QSize(15,15))
        closeButton.clicked.connect(self.tabCloseRequest)
        tabBar.setTabButton(k, QTabBar.RightSide, closeButton)

    def _init_chat_tab(self):
        self.chattab = QWidget()
        self.chattab.layout = QGridLayout()
        self.chattab.layout.setSpacing(5)
        chatBox = ChatBoxWidget(self.chattab)
        inputBox = InputBoxWidget(self.chattab)
        self.chattab.layout.addWidget(chatBox, 1, 0)
        self.chattab.layout.addWidget(inputBox, 2, 0)
        
        tabBar = self.tabs.tabBar()
        closeButton = QPushButton()
        closeButton.setGeometry(0,0,20,20)
        closeButton.setIcon(QIcon('./cross.png'))
        closeButton.setIconSize(QSize(15,15))
        closeButton.clicked.connect(self.tabCloseRequest)
        tabBar.setTabButton(0, QTabBar.RightSide, closeButton)
        self.chattab.setLayout(self.chattab.layout)
        self.tabs.addTab(self.chattab,"Chat")

    def _init_blank_tab(self):
        self.blanktab = QWidget()
        self.tabs.addTab(self.blanktab,"Blank")

    def _init_closable_tab(self):
        self.blanktab = QWidget()
        tabBar = self.tabs.tabBar()
        closeButton = QPushButton()
        closeButton.setGeometry(0,0,20,20)
        closeButton.setIcon(QIcon('./cross.png'))
        closeButton.setIconSize(QSize(15,15))
        closeButton.clicked.connect(self.tabCloseRequest)
        tabBar.setTabButton(0, QTabBar.RightSide, closeButton)

    def deteteTabById(self, id):
        pass

    @pyqtSlot()
    def on_click(self):
        print("Clicked !")
        self._init_home_tab()
        

    @pyqtSlot()
    def tabCloseRequest(self):
        print("tabCloseRequest !")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
