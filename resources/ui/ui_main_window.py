# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLayout,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(940, 560)
        MainWindow.setMinimumSize(QSize(940, 560))
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        palette = QPalette()
        brush = QBrush(QColor(221, 221, 221, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush1)
        brush2 = QBrush(QColor(120, 120, 120, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush1)
        self.styleSheet.setPalette(palette)
        self.styleSheet.setStyleSheet(u"#mainContent {	\n"
"	background-color: rgb(40, 44, 52);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* 1 - Left menu */\n"
"/* 1.1 - Menu content */\n"
"#leftMenu {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#menuContent{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"#topLogo {\n"
"	background-color: rgb(33, 37, 43);\n"
"	background-image: url(:/images/images/images/PyDracula.png);\n"
"	background-position: centered;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"#titleLeftApp { font: 63 12pt \"Segoe UI Semibold\"; }\n"
"#titleLeftDescription { font: 8pt \"Segoe UI\"; color: rgb(189, 147, 249); }\n"
"\n"
"/* 1.2 - Top menu */\n"
"#topMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#topMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#topMenu .QPushButton:pre"
                        "ssed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* 1.3 - Bottom menu */\n"
"#bottomMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#bottomMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"\n"
"/* 1.4 -Toggle Button */\n"
"#toggleButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color: rgb(37, 41, 48);\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"	color: rgb(113, 126, 149);\n"
"}\n"
"#toggleButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#toggleButton:pressed {\n"
"	background-c"
                        "olor: rgb(189, 147, 249);\n"
"}\n"
"\n"
"")
        self.appMargins = QHBoxLayout(self.styleSheet)
        self.appMargins.setSpacing(0)
        self.appMargins.setObjectName(u"appMargins")
        self.appMargins.setContentsMargins(10, 10, 10, 10)
        self.mainContent = QFrame(self.styleSheet)
        self.mainContent.setObjectName(u"mainContent")
        palette1 = QPalette()
        brush3 = QBrush(QColor(255, 255, 255, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        brush4 = QBrush(QColor(40, 44, 52, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette1.setBrush(QPalette.Active, QPalette.Light, brush3)
        brush5 = QBrush(QColor(227, 227, 227, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Midlight, brush5)
        brush6 = QBrush(QColor(160, 160, 160, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Dark, brush6)
        palette1.setBrush(QPalette.Active, QPalette.Mid, brush6)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush)
        palette1.setBrush(QPalette.Active, QPalette.BrightText, brush3)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush4)
        brush7 = QBrush(QColor(105, 105, 105, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Shadow, brush7)
        brush8 = QBrush(QColor(245, 245, 245, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.AlternateBase, brush8)
        brush9 = QBrush(QColor(255, 255, 220, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.ToolTipBase, brush9)
        palette1.setBrush(QPalette.Active, QPalette.ToolTipText, brush1)
        brush10 = QBrush(QColor(221, 221, 221, 128))
        brush10.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush10)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette1.setBrush(QPalette.Inactive, QPalette.Light, brush3)
        palette1.setBrush(QPalette.Inactive, QPalette.Midlight, brush5)
        palette1.setBrush(QPalette.Inactive, QPalette.Dark, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.Mid, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.BrightText, brush3)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette1.setBrush(QPalette.Inactive, QPalette.Shadow, brush7)
        palette1.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush8)
        palette1.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush9)
        palette1.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush1)
        brush11 = QBrush(QColor(0, 0, 0, 128))
        brush11.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush11)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette1.setBrush(QPalette.Disabled, QPalette.Light, brush3)
        palette1.setBrush(QPalette.Disabled, QPalette.Midlight, brush5)
        palette1.setBrush(QPalette.Disabled, QPalette.Dark, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.Mid, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.BrightText, brush3)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        palette1.setBrush(QPalette.Disabled, QPalette.Shadow, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush8)
        palette1.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush9)
        palette1.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush11)
#endif
        self.mainContent.setPalette(palette1)
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        self.mainContent.setFont(font)
        self.mainContent.setFrameShape(QFrame.StyledPanel)
        self.mainContent.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.mainContent)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenu = QFrame(self.mainContent)
        self.leftMenu.setObjectName(u"leftMenu")
        self.leftMenu.setMinimumSize(QSize(60, 0))
        self.leftMenu.setMaximumSize(QSize(60, 16777215))
        palette2 = QPalette()
        brush12 = QBrush(QColor(33, 37, 43, 255))
        brush12.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush12)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush12)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush12)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush12)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush12)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush12)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush12)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush12)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush12)
        self.leftMenu.setPalette(palette2)
        self.leftMenu.setFont(font)
        self.leftMenu.setFrameShape(QFrame.NoFrame)
        self.leftMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.leftMenu)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.logo = QFrame(self.leftMenu)
        self.logo.setObjectName(u"logo")
        self.logo.setMinimumSize(QSize(0, 50))
        self.logo.setMaximumSize(QSize(16777215, 50))
        self.logo.setFrameShape(QFrame.StyledPanel)
        self.logo.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.logo)

        self.menuContent = QFrame(self.leftMenu)
        self.menuContent.setObjectName(u"menuContent")
        self.menuContent.setFrameShape(QFrame.NoFrame)
        self.menuContent.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.menuContent)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.toggleBox = QFrame(self.menuContent)
        self.toggleBox.setObjectName(u"toggleBox")
        self.toggleBox.setMaximumSize(QSize(16777215, 45))
        self.toggleBox.setFrameShape(QFrame.NoFrame)
        self.toggleBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.toggleBox)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.toggleButton = QPushButton(self.toggleBox)
        self.toggleButton.setObjectName(u"toggleButton")
        self.toggleButton.setMinimumSize(QSize(0, 45))
        self.toggleButton.setStyleSheet(u"background-image: url(:/icon/image/icon/icon_toggle.png);")

        self.verticalLayout_5.addWidget(self.toggleButton)


        self.verticalLayout_2.addWidget(self.toggleBox)

        self.topMenu = QFrame(self.menuContent)
        self.topMenu.setObjectName(u"topMenu")
        palette3 = QPalette()
        self.topMenu.setPalette(palette3)
        self.topMenu.setFrameShape(QFrame.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.topMenu)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.homeButton = QPushButton(self.topMenu)
        self.homeButton.setObjectName(u"homeButton")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.homeButton.sizePolicy().hasHeightForWidth())
        self.homeButton.setSizePolicy(sizePolicy)
        self.homeButton.setMinimumSize(QSize(0, 50))
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush13 = QBrush(QColor(0, 0, 0, 0))
        brush13.setStyle(Qt.SolidPattern)
        palette4.setBrush(QPalette.Active, QPalette.Button, brush13)
        palette4.setBrush(QPalette.Active, QPalette.Text, brush)
        palette4.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette4.setBrush(QPalette.Active, QPalette.Base, brush13)
        palette4.setBrush(QPalette.Active, QPalette.Window, brush13)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette4.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        brush14 = QBrush(QColor(240, 240, 240, 255))
        brush14.setStyle(Qt.SolidPattern)
        palette4.setBrush(QPalette.Inactive, QPalette.Button, brush14)
        palette4.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.Base, brush3)
        palette4.setBrush(QPalette.Inactive, QPalette.Window, brush14)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush11)
#endif
        palette4.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.Button, brush13)
        palette4.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.Base, brush13)
        palette4.setBrush(QPalette.Disabled, QPalette.Window, brush13)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush11)
#endif
        self.homeButton.setPalette(palette4)
        self.homeButton.setFont(font)
        self.homeButton.setStyleSheet(u"background-image: url(:/icon/image/icon/icon_home.png);")

        self.verticalLayout_4.addWidget(self.homeButton)

        self.dataButton = QPushButton(self.topMenu)
        self.dataButton.setObjectName(u"dataButton")
        sizePolicy.setHeightForWidth(self.dataButton.sizePolicy().hasHeightForWidth())
        self.dataButton.setSizePolicy(sizePolicy)
        self.dataButton.setMinimumSize(QSize(0, 50))
        palette5 = QPalette()
        palette5.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette5.setBrush(QPalette.Active, QPalette.Button, brush13)
        palette5.setBrush(QPalette.Active, QPalette.Text, brush)
        palette5.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette5.setBrush(QPalette.Active, QPalette.Base, brush13)
        palette5.setBrush(QPalette.Active, QPalette.Window, brush13)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette5.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette5.setBrush(QPalette.Inactive, QPalette.Button, brush14)
        palette5.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette5.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette5.setBrush(QPalette.Inactive, QPalette.Base, brush3)
        palette5.setBrush(QPalette.Inactive, QPalette.Window, brush14)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush11)
#endif
        palette5.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.Button, brush13)
        palette5.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.Base, brush13)
        palette5.setBrush(QPalette.Disabled, QPalette.Window, brush13)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush11)
#endif
        self.dataButton.setPalette(palette5)
        self.dataButton.setFont(font)
        self.dataButton.setStyleSheet(u"background-image: url(:/icon/image/icon/icon_excel.png);")

        self.verticalLayout_4.addWidget(self.dataButton)


        self.verticalLayout_2.addWidget(self.topMenu, 0, Qt.AlignTop)

        self.bottomMenu = QFrame(self.menuContent)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setMaximumSize(QSize(16777215, 16777215))
        self.bottomMenu.setFrameShape(QFrame.NoFrame)
        self.bottomMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.settingButton = QPushButton(self.bottomMenu)
        self.settingButton.setObjectName(u"settingButton")
        sizePolicy.setHeightForWidth(self.settingButton.sizePolicy().hasHeightForWidth())
        self.settingButton.setSizePolicy(sizePolicy)
        self.settingButton.setMinimumSize(QSize(0, 45))
        palette6 = QPalette()
        palette6.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette6.setBrush(QPalette.Active, QPalette.Button, brush13)
        palette6.setBrush(QPalette.Active, QPalette.Text, brush)
        palette6.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette6.setBrush(QPalette.Active, QPalette.Base, brush13)
        palette6.setBrush(QPalette.Active, QPalette.Window, brush13)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette6.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette6.setBrush(QPalette.Inactive, QPalette.Button, brush14)
        palette6.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette6.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette6.setBrush(QPalette.Inactive, QPalette.Base, brush3)
        palette6.setBrush(QPalette.Inactive, QPalette.Window, brush14)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush11)
#endif
        palette6.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette6.setBrush(QPalette.Disabled, QPalette.Button, brush13)
        palette6.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette6.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette6.setBrush(QPalette.Disabled, QPalette.Base, brush13)
        palette6.setBrush(QPalette.Disabled, QPalette.Window, brush13)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush11)
#endif
        self.settingButton.setPalette(palette6)
        self.settingButton.setFont(font)
        self.settingButton.setStyleSheet(u"background-image: url(:/icon/image/icon/icon_settings.png);")

        self.verticalLayout_3.addWidget(self.settingButton)


        self.verticalLayout_2.addWidget(self.bottomMenu, 0, Qt.AlignBottom)


        self.verticalLayout.addWidget(self.menuContent)


        self.horizontalLayout.addWidget(self.leftMenu)

        self.centerContent = QFrame(self.mainContent)
        self.centerContent.setObjectName(u"centerContent")
        self.centerContent.setFrameShape(QFrame.NoFrame)
        self.centerContent.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.centerContent)


        self.appMargins.addWidget(self.mainContent)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"Hide", None))
        self.homeButton.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.dataButton.setText(QCoreApplication.translate("MainWindow", u"Data", None))
        self.settingButton.setText(QCoreApplication.translate("MainWindow", u"Setting", None))
    # retranslateUi

