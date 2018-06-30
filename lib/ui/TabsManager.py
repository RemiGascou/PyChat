from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class TabsManager(QWidget):        
    def __init__(self, parent):   
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)
        # Initialize tab screen
        self.tabs = QTabWidget()
        self.tabs.resize(300,200) 
        # Add tabs
        self._init_home_tab()
        #self._init_closable_tab()
        #self._init_chatbox_tab()
        # Add tabs to widget        
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)
 
    def _init_home_tab(self):
        self.hometab = QWidget()
        self.tabs.addTab(self.hometab,"Home")
        self.hometab.layout = QVBoxLayout(self)
        self.pushButton1 = QPushButton("PyQt5 button")
        self.pushButton1.clicked.connect(self.on_click)
        self.hometab.layout.addWidget(self.pushButton1)
        self.hometab.setLayout(self.hometab.layout)
        
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
        closeButton.setStyleSheet("float:right;")
        tabBar.setTabButton(0, QTabBar.RightSide, closeButton)
        self.tabs.addTab(self.blanktab,"Closable")
        
    def _init_chatbox_tab(self):
        self.blanktab = QWidget()
        self.tabs.addTab(self.blanktab,"Conv01")
        
    def deteteTabById(self, id:int):
        pass
        
    @pyqtSlot()
    def on_click(self):
        print("Clicked !")