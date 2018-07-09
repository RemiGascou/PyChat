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
        # Add tabs
        self._init_home_tab()
        self._updatetabs()
        # Add tabs to widget
        self.layout.addWidget(self.tabsWidget)
        self.setLayout(self.layout)

    def _init_home_tab(self):
        self.hometab = QWidget()
        title = "Home"
        self.hometab.layout = QVBoxLayout(self.hometab)
        self.pushButton1 = QPushButton("PyQt5 button")
        self.pushButton1.clicked.connect(self.on_click)
        self.hometab.layout.addWidget(self.pushButton1)
        self.hometab.setLayout(self.hometab.layout)
        #self.tabsWidget.addTab(self.hometab,"Home")
        tabdata = {
            "object": self.hometab,
            "title": title
        }
        self.tabs.append(tabdata)

    def _updatetabs(self):
        for tab in self.tabs:
            self.tabsWidget.addTab(tab["object"],tab["title"])
        pass

    def deteteTabById(self, id):
        pass

    def addTabById(self, id):
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
