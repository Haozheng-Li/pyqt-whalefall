from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt

from define import *


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.dragPos = None

        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(APP_TITLE)
        self.setWindowIcon(QIcon(APP_ICON))

    def mousePressEvent(self, event):
        self.dragPos = event.globalPosition()

        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')