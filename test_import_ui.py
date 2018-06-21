import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtGui import QIcon

basepath = "/home/tux/Documents/git_projects/PyChat/"

class App(QMainWindow):
    def __init__(self):
        super(App, self).__init__()
        uic.loadUi(basepath + 'ui/MainWindow.ui', self)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())