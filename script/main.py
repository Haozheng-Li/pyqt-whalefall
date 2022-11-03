import sys
import find_package

from PySide6.QtWidgets import QApplication
from widgets import main_window, splash_panel_widget
from define import *


app = QApplication(sys.argv)


if USE_SPLASH_PANEL:
    splash_screen = splash_panel_widget.getSplashPanel(use_gif=True)
    splash_screen.show()
    app.processEvents()

    main_window = main_window.MainWindow()
    main_window.show()
    splash_screen.finish(main_window)
    splash_screen.deleteLater()
else:
    main_window = main_window.MainWindow()
    main_window.show()


sys.exit(app.exec())
