import sys

from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6.QtCore import Qt

widgets = None


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.dragPos = None

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
