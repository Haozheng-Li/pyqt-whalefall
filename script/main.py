import sys

from PySide6.QtWidgets import QApplication
from widgets import main_widget, splash_panel_widget
from define import *


app = QApplication(sys.argv)


if USE_SPLASH_PANEL:
    splash_screen = splash_panel_widget.getSplashPanel(use_gif=True)
    splash_screen.show()
    app.processEvents()

    main_widget = main_widget.MainWindow()
    main_widget.show()
    splash_screen.finish(main_widget)
    splash_screen.deleteLater()
else:
    main_widget = main_widget.MainWindow()
    main_widget.show()


sys.exit(app.exec())
