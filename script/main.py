import sys
import utils

from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt

from define import *

widgets = None


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.dragPos = None

        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(APP_TITLE)
        self.setWindowIcon(QIcon(APP_ICON))
        self.show()

    def mousePressEvent(self, event):
        self.dragPos = event.globalPosition()

        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
