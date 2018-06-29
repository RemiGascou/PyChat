import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot, Qt

class Second(QMainWindow):
    def __init__(self, parent=None):
        print("Parent of Second", parent)
        super(Second, self).__init__(parent)


class First(QMainWindow):
    def __init__(self, parent=None):
        print("Parent of First", parent)
        super(First, self).__init__(parent)
        self.setGeometry(10,10,250,250)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.pushButton = QPushButton("click me")
        self.setCentralWidget(self.pushButton)
        self.pushButton.clicked.connect(self.on_pushButton_clicked)
        self.dialog = Second(self)

    def on_pushButton_clicked(self):
        self.dialog.show()


def main():
    app = QApplication(sys.argv)
    main = First()
    main.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()