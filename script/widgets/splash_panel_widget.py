from PySide6.QtWidgets import QSplashScreen
from PySide6.QtCore import QSize
from PySide6.QtGui import QMouseEvent, QMovie, QEnterEvent, QPixmap
from define import *


g_SplashPanel = None


def getSplashPanel(bg_path=None, use_gif=False):
    global g_SplashPanel
    if not g_SplashPanel:
        g_SplashPanel = SplashPanelWidget(bg_path, use_gif)

    return g_SplashPanel



class SplashPanelWidget(QSplashScreen):
    def __init__(self, bg_path=None, use_gif=False):
        QSplashScreen.__init__(self)

        self.setFixedSize(QSize(SPLASH_PANEL_SIZE))

        if not bg_path:
            bg_path = 'resources/gif/astronaut.gif'

        if use_gif:
            self.m_Movie = QMovie(bg_path)
            self.m_Movie.frameChanged.connect(lambda: self.setPixmap(self.m_Movie.currentPixmap()))
            self.m_Movie.start()
        else:
            self.setPixmap(QPixmap(bg_path))
    
    def mousePressEvent(self, event: QMouseEvent) -> None:
        pass

    def mouseDoubleClickEvent(self, event: QMouseEvent) -> None:
        pass

    def enterEvent(self, event:QEnterEvent) -> None:
        pass

    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        pass



if __name__ == '__main__':
    import sys
    from PySide6.QtWidgets import QApplication
    app = QApplication(sys.argv)

    splash_screen = getSplashPanel(use_gif=True)
    splash_screen.show()

    sys.exit(app.exec())