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
        self.tabs = []
        self.tabsWidget = QTabWidget()
        self.tabsWidget.resize(300,200)
        #Load Stylesheet from "TabsManager.css"
        f = open("lib/ui/widgets/styles/TabsManager.css",'r')
        stylesheet = "".join(f.readlines())
        f.close()
        #EndLoad
        self.tabsWidget.setStyleSheet(stylesheet)
        self.tabsBarWidget = self.tabsWidget.tabBar()
        self.tabsBarWidget.setTabsClosable(True)
        self.tabsBarWidget.tabCloseRequested.connect(self.tabCloseRequested)

        # Add tabs
        self._init_home_tab()
        self._updatetabs()
        #self._listtabs()
        # Add tabs to widget
        self.layout.addWidget(self.tabsWidget)
        self.setLayout(self.layout)

    def _init_home_tab(self, title = "Home"):
        self.hometab = QWidget()
        self.hometab.layout = QVBoxLayout(self.hometab)
        self.closeTabPB = QPushButton("Close Tab")
        self.closeTabPB.clicked.connect(self.on_click_close_tab)
        self.hometab.layout.addWidget(self.closeTabPB)
        self.addTabPB = QPushButton("Add Tab")
        self.addTabPB.clicked.connect(self._addTab)
        self.hometab.layout.addWidget(self.addTabPB)
        self.hometab.setLayout(self.hometab.layout)
        tabdata = {
            "object": self.hometab,
            "title": title
        }
        self.tabs.append(tabdata)

    def _init_welcome_tab(self, title="Welcome"):
        self.welcometab = QWidget()
        tabdata = {
            "object": self.welcometab,
            "title": title
        }
        self.tabs.append(tabdata)

    def _updatetabs(self):
        self.tabsWidget.clear()
        for tab in self.tabs:
            self.tabsWidget.addTab(tab["object"],tab["title"])

    def _listtabs(self):
        _=0
        for tab in self.tabs:
            print("Tab @[id=" + str(_) + "] : " + tab["title"])
            _+=1

    def _deteteTabById(self, id):
        if id >= 0 and id < len(self.tabs):
            del self.tabs[id]
        else :
            return -1
        #self._listtabs()
        self._updatetabs()

    def _addTab(self):
        self._init_home_tab("Added "+str(len(self.tabs)))
        #self._listtabs()
        self._updatetabs()

    @pyqtSlot()
    def on_click_close_tab(self):
        print("Clicked !")
        self._deteteTabById(1)


    def tabCloseRequested(self,index):
        print("tabCloseRequested !")
        widget = self.tabsWidget.widget(index)
        if widget is not None:
            widget.deleteLater()
        self.tabsWidget.removeTab(index)
        self._deteteTabById(index)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
