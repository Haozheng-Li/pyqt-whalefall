from PySide6.QtWidgets import QMainWindow
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt, QPropertyAnimation, QEasingCurve

from define import *
from ui import ui_main_window

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.dragPos = None
        self.m_ui = ui_main_window.Ui_MainWindow()
        self.m_ui.setupUi(self)
        self.initUI()
        self.initCB()
    
    def initUI(self):
        self.setWindowTitle(APP_TITLE)
        self.setWindowIcon(QIcon(APP_ICON))

        # self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
    
    def initCB(self):
        self.m_ui.toggleButton.clicked.connect(self.toggleButtonCB)
    
    def toggleButtonCB(self):
        
        if self.m_ui.leftMenu.width() == LEFT_MENU_STANDARD_WIDTH:
            targetWidth = LEFT_MENU_MAXTEND_WIDTH
        else:
            targetWidth = LEFT_MENU_STANDARD_WIDTH

        self.animation = QPropertyAnimation(self.m_ui.leftMenu, b"minimumWidth")
        self.animation.setDuration(500)
        self.animation.setStartValue(self.m_ui.leftMenu.width())
        self.animation.setEndValue(targetWidth)
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.animation.start()

    def mousePressEvent(self, event):
        self.dragPos = event.globalPosition()

        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')