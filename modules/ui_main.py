# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QProgressBar, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QTextEdit, QVBoxLayout, QWidget)
from .icon_rc import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(975, 693)
        MainWindow.setMinimumSize(QSize(960, 560))
        MainWindow.setStyleSheet(u"")
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        self.styleSheet.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"\n"
"SET APP STYLESHEET - FULL STYLES HERE\n"
"DARK THEME - DRACULA COLOR BASED\n"
"\n"
"# BY: WANDERSON M.PIMENTA\n"
"# PROJECT MADE WITH: Qt Designer and PySide6\n"
"# V: 1.0.0\n"
"#\n"
"# This project can be used freely for all uses, as long as they maintain the\n"
"# respective credits only in the Python scripts, any information in the visual\n"
"# interface (GUI) can be modified without any implication.\n"
"#\n"
"# There are limitations on Qt licenses if you want to use your products\n"
"# commercially, I recommend reading them on the official website:\n"
"# https://doc.qt.io/qtforpython/licenses.html\n"
"\n"
"///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"\n"
"QWidget{\n"
"	color: #333;\n"
"	font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Tooltip */"
                        "\n"
"QToolTip {\n"
"	color: #333;\n"
"	background-color: #f8f8f2;\n"
"	border: 1px solid #CCC;\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(255, 121, 198);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Bg App */\n"
"#bgApp {\n"
"	background-color: #f8f8f2;\n"
"	border: 1px solid #CCC;\n"
"    color: #44475a;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Left Menu */\n"
"#leftMenuBg {	\n"
"	background-color: #6272a4;\n"
"}\n"
"#topLogo {\n"
"	background-color: #6272a4;\n"
"	background-image: url(:/icons/image/PyDracula.png);\n"
"	background-position: centered;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"#titleLeftApp { font: 63 12pt \"Segoe UI Semibold\"; color: #f8f8f2; }\n"
"#titleLeftDesc"
                        "ription { font: 8pt \"Segoe UI\"; color: #bd93f9; }\n"
"\n"
"/* MENUS */\n"
"#topMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"    color: #f8f8f2;\n"
"}\n"
"#topMenu .QPushButton:hover {\n"
"	background-color: #bd93f9;\n"
"}\n"
"#topMenu .QPushButton:pressed {	\n"
"	background-color: #ff79c6;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#bottomMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"    color: #f8f8f2;\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"	background-color: #bd93f9;\n"
"}\n"
"#bottomMenu .QPushButton:pressed {	\n"
"	background-color: #ff79c6;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#leftMenuFrame{\n"
""
                        "	border-top: 3px solid #6a7cb1;\n"
"}\n"
"\n"
"/* Toggle Button */\n"
"#toggleButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color: #5b6996;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"	color: #f8f8f2;\n"
"}\n"
"#toggleButton:hover {\n"
"	background-color: #bd93f9;\n"
"}\n"
"#toggleButton:pressed {	\n"
"	background-color: #ff79c6;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* Title Menu */\n"
"#titleRightInfo { padding-left: 10px; }\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Extra Tab */\n"
"#extraLeftBox {	\n"
"	background-color: #495474;\n"
"    color: #f8f8f2;\n"
"}\n"
"#extraTopBg{	\n"
"	background-color: rgb(189, 147, 249)\n"
"}\n"
"\n"
"/* Icon */\n"
"#extraIcon {\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"	background-image: url(:/icons/icons/icon_settings.png);\n"
"}\n"
"\n"
""
                        "/* Label */\n"
"#extraLabel { color: rgb(255, 255, 255); }\n"
"\n"
"/* Btn Close */\n"
"#extraCloseColumnBtn { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#extraCloseColumnBtn:hover { background-color: rgb(196, 161, 249); border-style: solid; border-radius: 4px; }\n"
"#extraCloseColumnBtn:pressed { background-color: rgb(180, 141, 238); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Extra Content */\n"
"#extraContent{\n"
"	border-top: 3px solid #6272a4;\n"
"}\n"
"\n"
"/* Extra Top Menus */\n"
"#extraTopMenu .QPushButton {\n"
"    background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"    color: #f8f8f2;\n"
"}\n"
"#extraTopMenu .QPushButton:hover {\n"
"	background-color: #5d6c99;\n"
"}\n"
"#extraTopMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
""
                        "}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Content App */\n"
"#contentTopBg{	\n"
"	background-color: #6272a4;\n"
"}\n"
"#contentBottom{\n"
"	border-top: 3px solid #bd93f9;\n"
"}\n"
"#titleRightInfo{\n"
"    color: #f8f8f2;\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: #bd93f9; border-style: solid; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: #ff79c6; border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Theme Settings */\n"
"#extraRightBox { background-color: #495474; }\n"
"#themeSettingsTopDetail { background-color: #6272a4; }\n"
"\n"
"/* Bottom Bar */\n"
"#bottomBar { background-color: #495474 }\n"
"#bottomBar QLabel { font-size: 11px; color: #f8f8f2; padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
"\n"
"/* CONTENT SETTINGS */\n"
""
                        "/* MENUS */\n"
"#contentSettings .QPushButton {\n"
"    background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"    color: #f8f8f2;\n"
"}\n"
"#contentSettings .QPushButton:hover {\n"
"	background-color: #5d6c99;\n"
"}\n"
"#contentSettings .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QTableWidget */\n"
"QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: #9faeda;\n"
"    outline: none;\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: #9faeda;\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: #9faeda;\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(189, 147, 249);\n"
"    color: #f8f"
                        "8f2;\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: #6272a4;\n"
"	max-width: 30px;\n"
"	border: none;\n"
"	border-style: none;\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: #6272a4;\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid #6272a4;\n"
"	background-color: #6272a4;\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"    color: #f8f8f2;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid #6272a4;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"	background-color: #6272a4;\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(0, 0, 0);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(150, 150, 150);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid #ff79c6;\n"
"}"
                        "\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"PlainTextEdit */\n"
"QPlainTextEdit {\n"
"	background-color: #6272a4;\n"
"	border: 2px solid rgb(0, 0, 0);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"\n"
"}\n"
"QPlainTextEdit  QScrollBar:vertical {\n"
"    width: 8px;\n"
" }\n"
"QPlainTextEdit  QScrollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid #ff79c6;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: #6272a4;\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(189, 147, 249);\n"
" "
                        "   min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: #6272a4;\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: #6272a4;\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background-color: #6272a4;\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {\n"
"	background: rgb(189, 147, 249)"
                        ";\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: #6272a4;\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: #6272a4;\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CheckBox */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid #6272a4;\n"
"	width: 15px;\n"
"	height: 15px;\n"
""
                        "	border-radius: 10px;\n"
"    background: #6272a4;\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(119, 136, 187);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid #bd93f9;\n"
"	border: 3px solid #bd93f9;\n"
"	background-image: url(:/icons/icons/cil-check-alt.png);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"RadioButton */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid #6272a4;\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: #6272a4;\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(119, 136, 187);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid #bd93f9;\n"
"	border: 3px solid #bd93f9;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QComboBox{\n"
"	background-color: #6272a4;\n"
"	border-radius: 5px;\n"
"	border: 2px "
                        "solid rgb(0, 0, 0);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(150, 150, 150);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px;\n"
"	border-left-width: 3px;\n"
"	border-left-color: rgb(0, 0, 0);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;\n"
"	background-image: url(:/icons/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"\n"
"\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 121, 198);\n"
"	background-color: #6272a4;\n"
"\n"
"	padding: 10px;\n"
"	selection-background-color: #6272a4;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Sliders */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"	margin: 0px;\n"
"	background-color: #6272a4;\n"
"}\n"
"QSli"
                        "der::groove:horizontal:hover {\n"
"	background-color: #6272a4;\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(189, 147, 249);\n"
"    border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 5px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	background-color: #6272a4;\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: #6272a4;\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(189, 147, 249);\n"
"	border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(255, 121"
                        ", 198);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CommandLinkButton */\n"
"#pagesContainer QCommandLinkButton {\n"
"	color: rgb(255, 121, 198);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"    border: 2px solid #ff79c6;\n"
"    color: #ff79c6;\n"
"}\n"
"#pagesContainer QCommandLinkButton:hover {\n"
"	color: rgb(255, 170, 255);\n"
"	background-color: #6272a4;\n"
"}\n"
"#pagesContainer QCommandLinkButton:pressed {\n"
"	color: rgb(189, 147, 249);\n"
"	background-color: #586796;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Button */\n"
"#pagesContainer QPushButton {\n"
"	border: 2px solid rgb(0, 0, 0);\n"
"	border-radius: 5px;\n"
"	background-color: #6272a4;\n"
"\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: #7082b6;\n"
"	border: 2px solid rgb(90, 90, 90);\n"
"}\n"
"\n"
"QTextEdit{\n"
"	border: 2px solid rgb(0, 0, 0);\n"
"	border-radius: "
                        "5px;\n"
"}\n"
"QTextEdit:hover{\n"
"	border: 2px solid rgb(150, 150, 150);\n"
"\n"
"\n"
"}\n"
"QTextEdit:focus {\n"
"	border: 2px solid #ff79c6;\n"
"}\n"
"")
        self.appMargins = QVBoxLayout(self.styleSheet)
        self.appMargins.setObjectName(u"appMargins")
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.bgApp)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(60, 0))
        self.leftMenuBg.setMaximumSize(QSize(60, 16777215))
        self.leftMenuBg.setStyleSheet(u"")
        self.leftMenuBg.setFrameShape(QFrame.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(0, 50))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 50))
        self.topLogoInfo.setStyleSheet(u"")
        self.topLogoInfo.setFrameShape(QFrame.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Raised)
        self.topLogo = QFrame(self.topLogoInfo)
        self.topLogo.setObjectName(u"topLogo")
        self.topLogo.setGeometry(QRect(10, 5, 42, 42))
        self.topLogo.setMinimumSize(QSize(42, 42))
        self.topLogo.setMaximumSize(QSize(42, 42))
        self.topLogo.setStyleSheet(u"background-image: url(:/icons/image/PyDracula.png);")
        self.topLogo.setFrameShape(QFrame.NoFrame)
        self.topLogo.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.topLogoInfo)

        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setStyleSheet(u"")
        self.leftMenuFrame.setFrameShape(QFrame.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.leftMenuFrame)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.toggleBox = QFrame(self.leftMenuFrame)
        self.toggleBox.setObjectName(u"toggleBox")
        self.toggleBox.setMaximumSize(QSize(16777215, 45))
        self.toggleBox.setFrameShape(QFrame.NoFrame)
        self.toggleBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.toggleBox)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.toggleButton = QPushButton(self.toggleBox)
        self.toggleButton.setObjectName(u"toggleButton")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggleButton.sizePolicy().hasHeightForWidth())
        self.toggleButton.setSizePolicy(sizePolicy)
        self.toggleButton.setMinimumSize(QSize(0, 45))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.toggleButton.setFont(font)
        self.toggleButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleButton.setLayoutDirection(Qt.LeftToRight)
        self.toggleButton.setStyleSheet(u"background-image: url(:/icons/icons/icon_menu.png);\n"
"")

        self.verticalLayout_6.addWidget(self.toggleButton)


        self.verticalLayout_5.addWidget(self.toggleBox)

        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setStyleSheet(u"")
        self.topMenu.setFrameShape(QFrame.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.topMenu)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.btn_home = QPushButton(self.topMenu)
        self.btn_home.setObjectName(u"btn_home")
        sizePolicy.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy)
        self.btn_home.setMinimumSize(QSize(0, 45))
        self.btn_home.setFont(font)
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home.setLayoutDirection(Qt.LeftToRight)
        self.btn_home.setStyleSheet(u"\n"
"background-image: url(:/icons/icons/cil-home.png);")

        self.verticalLayout_7.addWidget(self.btn_home)

        self.btn_game = QPushButton(self.topMenu)
        self.btn_game.setObjectName(u"btn_game")
        sizePolicy.setHeightForWidth(self.btn_game.sizePolicy().hasHeightForWidth())
        self.btn_game.setSizePolicy(sizePolicy)
        self.btn_game.setMinimumSize(QSize(0, 45))
        self.btn_game.setFont(font)
        self.btn_game.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_game.setLayoutDirection(Qt.LeftToRight)
        self.btn_game.setStyleSheet(u"background-image: url(:/icons/icons/cil-gamepad.png);")

        self.verticalLayout_7.addWidget(self.btn_game)

        self.btn_refresh = QPushButton(self.topMenu)
        self.btn_refresh.setObjectName(u"btn_refresh")
        sizePolicy.setHeightForWidth(self.btn_refresh.sizePolicy().hasHeightForWidth())
        self.btn_refresh.setSizePolicy(sizePolicy)
        self.btn_refresh.setMinimumSize(QSize(0, 45))
        self.btn_refresh.setFont(font)
        self.btn_refresh.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_refresh.setLayoutDirection(Qt.LeftToRight)
        self.btn_refresh.setStyleSheet(u"background-image: url(:/icons/icons/cil-loop-circular.png);")

        self.verticalLayout_7.addWidget(self.btn_refresh)

        self.btn_info = QPushButton(self.topMenu)
        self.btn_info.setObjectName(u"btn_info")
        sizePolicy.setHeightForWidth(self.btn_info.sizePolicy().hasHeightForWidth())
        self.btn_info.setSizePolicy(sizePolicy)
        self.btn_info.setMinimumSize(QSize(0, 45))
        self.btn_info.setStyleSheet(u"background-image: url(:/icons/icons/cil-user.png);")

        self.verticalLayout_7.addWidget(self.btn_info)

        self.btn_style = QPushButton(self.topMenu)
        self.btn_style.setObjectName(u"btn_style")
        sizePolicy.setHeightForWidth(self.btn_style.sizePolicy().hasHeightForWidth())
        self.btn_style.setSizePolicy(sizePolicy)
        self.btn_style.setMinimumSize(QSize(0, 45))
        self.btn_style.setStyleSheet(u"background-image: url(:/icons/icons/cil-moon.png);")

        self.verticalLayout_7.addWidget(self.btn_style)

        self.btn_exit = QPushButton(self.topMenu)
        self.btn_exit.setObjectName(u"btn_exit")
        sizePolicy.setHeightForWidth(self.btn_exit.sizePolicy().hasHeightForWidth())
        self.btn_exit.setSizePolicy(sizePolicy)
        self.btn_exit.setMinimumSize(QSize(0, 45))
        self.btn_exit.setFont(font)
        self.btn_exit.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_exit.setLayoutDirection(Qt.LeftToRight)
        self.btn_exit.setStyleSheet(u"background-image: url(:/icons/icons/cil-x.png);")

        self.verticalLayout_7.addWidget(self.btn_exit)


        self.verticalLayout_5.addWidget(self.topMenu)

        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setStyleSheet(u"")
        self.bottomMenu.setFrameShape(QFrame.NoFrame)
        self.bottomMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.toggleLeftBox = QPushButton(self.bottomMenu)
        self.toggleLeftBox.setObjectName(u"toggleLeftBox")
        sizePolicy.setHeightForWidth(self.toggleLeftBox.sizePolicy().hasHeightForWidth())
        self.toggleLeftBox.setSizePolicy(sizePolicy)
        self.toggleLeftBox.setMinimumSize(QSize(0, 45))
        self.toggleLeftBox.setFont(font)
        self.toggleLeftBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleLeftBox.setLayoutDirection(Qt.LeftToRight)
        self.toggleLeftBox.setStyleSheet(u"background-image: url(:/icons/icons/icon_settings.png);")

        self.verticalLayout_8.addWidget(self.toggleLeftBox)


        self.verticalLayout_5.addWidget(self.bottomMenu, 0, Qt.AlignBottom)


        self.verticalLayout_2.addWidget(self.leftMenuFrame)


        self.horizontalLayout.addWidget(self.leftMenuBg)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.contentBox)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.contentTopBg.sizePolicy().hasHeightForWidth())
        self.contentTopBg.setSizePolicy(sizePolicy1)
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setStyleSheet(u"")
        self.contentTopBg.setFrameShape(QFrame.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 10, 0)
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy2)
        self.leftBox.setFrameShape(QFrame.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy3)
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
        self.titleRightInfo.setFont(font)
        self.titleRightInfo.setStyleSheet(u"")
        self.titleRightInfo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.titleRightInfo)


        self.horizontalLayout_2.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setStyleSheet(u"")
        self.rightButtons.setFrameShape(QFrame.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.settingsTopBtn = QPushButton(self.rightButtons)
        self.settingsTopBtn.setObjectName(u"settingsTopBtn")
        self.settingsTopBtn.setMinimumSize(QSize(28, 28))
        self.settingsTopBtn.setMaximumSize(QSize(28, 28))
        self.settingsTopBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/icons/icon_settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsTopBtn.setIcon(icon)
        self.settingsTopBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_5.addWidget(self.settingsTopBtn)

        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeAppBtn.setIcon(icon1)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_5.addWidget(self.minimizeAppBtn)

        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(28, 28))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setStyleStrategy(QFont.PreferDefault)
        self.maximizeRestoreAppBtn.setFont(font1)
        self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeRestoreAppBtn.setIcon(icon2)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_5.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeAppBtn.setIcon(icon3)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_5.addWidget(self.closeAppBtn)


        self.horizontalLayout_2.addWidget(self.rightButtons)


        self.verticalLayout_3.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setMinimumSize(QSize(0, 0))
        self.contentBottom.setStyleSheet(u"")
        self.contentBottom.setFrameShape(QFrame.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.content)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setStyleSheet(u"")
        self.pagesContainer.setFrameShape(QFrame.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(10, 10, 10, 10)
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.home.setStyleSheet(u"")
        self.verticalLayout_13 = QVBoxLayout(self.home)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_title = QLabel(self.home)
        self.label_title.setObjectName(u"label_title")
        font2 = QFont()
        font2.setFamilies([u"\u5e7c\u5706"])
        font2.setPointSize(16)
        font2.setBold(False)
        font2.setItalic(False)
        self.label_title.setFont(font2)
        self.label_title.setStyleSheet(u"font: 16pt \"\u5e7c\u5706\";")
        self.label_title.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_title)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.frame = QFrame(self.home)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, -1, 0)
        self.label_size = QLabel(self.frame)
        self.label_size.setObjectName(u"label_size")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_size.sizePolicy().hasHeightForWidth())
        self.label_size.setSizePolicy(sizePolicy4)

        self.verticalLayout.addWidget(self.label_size)

        self.label_page = QLabel(self.frame)
        self.label_page.setObjectName(u"label_page")
        sizePolicy4.setHeightForWidth(self.label_page.sizePolicy().hasHeightForWidth())
        self.label_page.setSizePolicy(sizePolicy4)

        self.verticalLayout.addWidget(self.label_page)

        self.label_flag = QLabel(self.frame)
        self.label_flag.setObjectName(u"label_flag")
        sizePolicy4.setHeightForWidth(self.label_flag.sizePolicy().hasHeightForWidth())
        self.label_flag.setSizePolicy(sizePolicy4)

        self.verticalLayout.addWidget(self.label_flag)

        self.label_timeout = QLabel(self.frame)
        self.label_timeout.setObjectName(u"label_timeout")
        sizePolicy4.setHeightForWidth(self.label_timeout.sizePolicy().hasHeightForWidth())
        self.label_timeout.setSizePolicy(sizePolicy4)

        self.verticalLayout.addWidget(self.label_timeout)

        self.label_outputType = QLabel(self.frame)
        self.label_outputType.setObjectName(u"label_outputType")
        sizePolicy4.setHeightForWidth(self.label_outputType.sizePolicy().hasHeightForWidth())
        self.label_outputType.setSizePolicy(sizePolicy4)

        self.verticalLayout.addWidget(self.label_outputType)

        self.label_outputPath = QLabel(self.frame)
        self.label_outputPath.setObjectName(u"label_outputPath")
        sizePolicy4.setHeightForWidth(self.label_outputPath.sizePolicy().hasHeightForWidth())
        self.label_outputPath.setSizePolicy(sizePolicy4)

        self.verticalLayout.addWidget(self.label_outputPath)


        self.horizontalLayout_6.addWidget(self.frame)

        self.frame_2 = QFrame(self.home)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_2)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_size = QLineEdit(self.frame_2)
        self.lineEdit_size.setObjectName(u"lineEdit_size")
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.lineEdit_size.sizePolicy().hasHeightForWidth())
        self.lineEdit_size.setSizePolicy(sizePolicy5)
        self.lineEdit_size.setMinimumSize(QSize(300, 0))
        self.lineEdit_size.setMaximumSize(QSize(300, 16777215))
        self.lineEdit_size.setStyleSheet(u"")

        self.verticalLayout_11.addWidget(self.lineEdit_size)

        self.lineEdit_page = QLineEdit(self.frame_2)
        self.lineEdit_page.setObjectName(u"lineEdit_page")
        self.lineEdit_page.setMinimumSize(QSize(300, 0))
        self.lineEdit_page.setMaximumSize(QSize(300, 16777215))
        self.lineEdit_page.setStyleSheet(u"")

        self.verticalLayout_11.addWidget(self.lineEdit_page)

        self.lineEdit_flag = QLineEdit(self.frame_2)
        self.lineEdit_flag.setObjectName(u"lineEdit_flag")
        self.lineEdit_flag.setMinimumSize(QSize(300, 0))
        self.lineEdit_flag.setMaximumSize(QSize(300, 16777215))
        self.lineEdit_flag.setStyleSheet(u"")

        self.verticalLayout_11.addWidget(self.lineEdit_flag)

        self.lineEdit_timeout = QLineEdit(self.frame_2)
        self.lineEdit_timeout.setObjectName(u"lineEdit_timeout")
        self.lineEdit_timeout.setMinimumSize(QSize(300, 0))
        self.lineEdit_timeout.setMaximumSize(QSize(300, 16777215))
        self.lineEdit_timeout.setStyleSheet(u"")

        self.verticalLayout_11.addWidget(self.lineEdit_timeout)

        self.lineEdit_outputType = QLineEdit(self.frame_2)
        self.lineEdit_outputType.setObjectName(u"lineEdit_outputType")
        self.lineEdit_outputType.setMinimumSize(QSize(300, 0))
        self.lineEdit_outputType.setMaximumSize(QSize(300, 16777215))
        self.lineEdit_outputType.setStyleSheet(u"")

        self.verticalLayout_11.addWidget(self.lineEdit_outputType)

        self.lineEdit_outputPath = QLineEdit(self.frame_2)
        self.lineEdit_outputPath.setObjectName(u"lineEdit_outputPath")
        self.lineEdit_outputPath.setMinimumSize(QSize(300, 0))
        self.lineEdit_outputPath.setMaximumSize(QSize(300, 16777215))
        self.lineEdit_outputPath.setStyleSheet(u"")

        self.verticalLayout_11.addWidget(self.lineEdit_outputPath)


        self.horizontalLayout_6.addWidget(self.frame_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)

        self.frame_5 = QFrame(self.home)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frame_5)
        self.verticalLayout_28.setSpacing(0)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_5)
        self.label.setObjectName(u"label")
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy6)
        self.label.setMinimumSize(QSize(0, 0))
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_28.addWidget(self.label)


        self.horizontalLayout_6.addWidget(self.frame_5)


        self.horizontalLayout_9.addLayout(self.horizontalLayout_6)


        self.verticalLayout_12.addLayout(self.horizontalLayout_9)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_3)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(10)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_2)

        self.pushButton_programme1 = QPushButton(self.home)
        self.pushButton_programme1.setObjectName(u"pushButton_programme1")
        self.pushButton_programme1.setMinimumSize(QSize(100, 0))
        self.pushButton_programme1.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_8.addWidget(self.pushButton_programme1)

        self.pushButton_programme2 = QPushButton(self.home)
        self.pushButton_programme2.setObjectName(u"pushButton_programme2")
        self.pushButton_programme2.setMinimumSize(QSize(100, 0))
        self.pushButton_programme2.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_8.addWidget(self.pushButton_programme2)

        self.pushButton_programme3 = QPushButton(self.home)
        self.pushButton_programme3.setObjectName(u"pushButton_programme3")
        self.pushButton_programme3.setMinimumSize(QSize(100, 0))
        self.pushButton_programme3.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_8.addWidget(self.pushButton_programme3)

        self.pushButton_programme4 = QPushButton(self.home)
        self.pushButton_programme4.setObjectName(u"pushButton_programme4")
        self.pushButton_programme4.setMinimumSize(QSize(100, 0))
        self.pushButton_programme4.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_8.addWidget(self.pushButton_programme4)


        self.horizontalLayout_10.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(5)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_3)

        self.pushButton_clear = QPushButton(self.home)
        self.pushButton_clear.setObjectName(u"pushButton_clear")
        sizePolicy5.setHeightForWidth(self.pushButton_clear.sizePolicy().hasHeightForWidth())
        self.pushButton_clear.setSizePolicy(sizePolicy5)
        self.pushButton_clear.setMinimumSize(QSize(100, 0))
        self.pushButton_clear.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_7.addWidget(self.pushButton_clear)

        self.pushButton_save = QPushButton(self.home)
        self.pushButton_save.setObjectName(u"pushButton_save")
        self.pushButton_save.setMinimumSize(QSize(100, 0))
        self.pushButton_save.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_7.addWidget(self.pushButton_save)

        self.pushButton_close = QPushButton(self.home)
        self.pushButton_close.setObjectName(u"pushButton_close")
        self.pushButton_close.setMinimumSize(QSize(100, 0))
        self.pushButton_close.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_7.addWidget(self.pushButton_close)


        self.horizontalLayout_10.addLayout(self.horizontalLayout_7)


        self.verticalLayout_12.addLayout(self.horizontalLayout_10)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer)


        self.verticalLayout_13.addLayout(self.verticalLayout_12)

        self.stackedWidget.addWidget(self.home)
        self.info = QWidget()
        self.info.setObjectName(u"info")
        self.info.setStyleSheet(u"")
        self.verticalLayout_24 = QVBoxLayout(self.info)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.frame_head = QFrame(self.info)
        self.frame_head.setObjectName(u"frame_head")
        self.frame_head.setFrameShape(QFrame.StyledPanel)
        self.frame_head.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_head)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.frame_14 = QFrame(self.frame_head)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_14)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.frame_14)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font: 16pt \"\u5e7c\u5706\";")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_25.addWidget(self.label_2)


        self.horizontalLayout_17.addWidget(self.frame_14)


        self.verticalLayout_24.addWidget(self.frame_head)

        self.frame_body = QFrame(self.info)
        self.frame_body.setObjectName(u"frame_body")
        self.frame_body.setFrameShape(QFrame.StyledPanel)
        self.frame_body.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.frame_body)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.textEdit = QTextEdit(self.frame_body)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setStyleSheet(u"")

        self.verticalLayout_26.addWidget(self.textEdit)


        self.verticalLayout_24.addWidget(self.frame_body)

        self.frame_foot = QFrame(self.info)
        self.frame_foot.setObjectName(u"frame_foot")
        self.frame_foot.setFrameShape(QFrame.StyledPanel)
        self.frame_foot.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_foot)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.label_4 = QLabel(self.frame_foot)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_27.addWidget(self.label_4)


        self.verticalLayout_24.addWidget(self.frame_foot)

        self.stackedWidget.addWidget(self.info)
        self.exit = QWidget()
        self.exit.setObjectName(u"exit")
        self.stackedWidget.addWidget(self.exit)
        self.game = QWidget()
        self.game.setObjectName(u"game")
        self.game.setStyleSheet(u"")
        self.verticalLayout_14 = QVBoxLayout(self.game)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.game_title = QFrame(self.game)
        self.game_title.setObjectName(u"game_title")
        self.game_title.setFrameShape(QFrame.StyledPanel)
        self.game_title.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.game_title)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.label_3 = QLabel(self.game_title)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"font: 16pt \"\u5e7c\u5706\";")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_20.addWidget(self.label_3)


        self.verticalLayout_14.addWidget(self.game_title)

        self.frame_4 = QFrame(self.game)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.game_info = QFrame(self.frame_4)
        self.game_info.setObjectName(u"game_info")
        self.game_info.setFrameShape(QFrame.StyledPanel)
        self.game_info.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.game_info)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.game_body = QFrame(self.game_info)
        self.game_body.setObjectName(u"game_body")
        self.game_body.setFrameShape(QFrame.StyledPanel)
        self.game_body.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.game_body)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.game_head = QFrame(self.game_body)
        self.game_head.setObjectName(u"game_head")
        self.game_head.setFrameShape(QFrame.StyledPanel)
        self.game_head.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.game_head)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.game_head_head = QFrame(self.game_head)
        self.game_head_head.setObjectName(u"game_head_head")
        self.game_head_head.setFrameShape(QFrame.StyledPanel)
        self.game_head_head.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.game_head_head)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.frame_3 = QFrame(self.game_head_head)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_3)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_code = QLabel(self.frame_3)
        self.label_code.setObjectName(u"label_code")

        self.verticalLayout_18.addWidget(self.label_code)

        self.label_cookies = QLabel(self.frame_3)
        self.label_cookies.setObjectName(u"label_cookies")

        self.verticalLayout_18.addWidget(self.label_cookies)


        self.horizontalLayout_13.addWidget(self.frame_3)

        self.frame_search = QFrame(self.game_head_head)
        self.frame_search.setObjectName(u"frame_search")
        self.frame_search.setFrameShape(QFrame.StyledPanel)
        self.frame_search.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_search)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.lineEdit_code = QLineEdit(self.frame_search)
        self.lineEdit_code.setObjectName(u"lineEdit_code")
        self.lineEdit_code.setMaximumSize(QSize(500, 16777215))
        self.lineEdit_code.setStyleSheet(u"")
        self.lineEdit_code.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_17.addWidget(self.lineEdit_code)

        self.lineEdit_cookies = QLineEdit(self.frame_search)
        self.lineEdit_cookies.setObjectName(u"lineEdit_cookies")
        self.lineEdit_cookies.setMaximumSize(QSize(500, 16777215))
        self.lineEdit_cookies.setStyleSheet(u"")

        self.verticalLayout_17.addWidget(self.lineEdit_cookies)


        self.horizontalLayout_13.addWidget(self.frame_search)

        self.frame_8 = QFrame(self.game_head_head)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_8)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.frame_9 = QFrame(self.frame_8)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.pushButton_run = QPushButton(self.frame_9)
        self.pushButton_run.setObjectName(u"pushButton_run")
        self.pushButton_run.setMinimumSize(QSize(100, 30))
        self.pushButton_run.setStyleSheet(u"")

        self.horizontalLayout_15.addWidget(self.pushButton_run)

        self.pushButton_pause = QPushButton(self.frame_9)
        self.pushButton_pause.setObjectName(u"pushButton_pause")
        self.pushButton_pause.setMinimumSize(QSize(100, 30))
        self.pushButton_pause.setStyleSheet(u"")

        self.horizontalLayout_15.addWidget(self.pushButton_pause)


        self.verticalLayout_23.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.frame_8)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.pushButton_resume = QPushButton(self.frame_10)
        self.pushButton_resume.setObjectName(u"pushButton_resume")
        self.pushButton_resume.setMinimumSize(QSize(100, 30))
        self.pushButton_resume.setStyleSheet(u"")

        self.horizontalLayout_16.addWidget(self.pushButton_resume)

        self.pushButton_cancel = QPushButton(self.frame_10)
        self.pushButton_cancel.setObjectName(u"pushButton_cancel")
        self.pushButton_cancel.setMinimumSize(QSize(100, 30))
        self.pushButton_cancel.setStyleSheet(u"")

        self.horizontalLayout_16.addWidget(self.pushButton_cancel)


        self.verticalLayout_23.addWidget(self.frame_10)


        self.horizontalLayout_13.addWidget(self.frame_8)

        self.pushButton_Orun = QPushButton(self.game_head_head)
        self.pushButton_Orun.setObjectName(u"pushButton_Orun")
        self.pushButton_Orun.setMinimumSize(QSize(100, 50))
        self.pushButton_Orun.setStyleSheet(u"")

        self.horizontalLayout_13.addWidget(self.pushButton_Orun)


        self.verticalLayout_22.addWidget(self.game_head_head)

        self.frame_6 = QFrame(self.game_head)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.checkBox_unknown = QCheckBox(self.frame_6)
        self.checkBox_unknown.setObjectName(u"checkBox_unknown")

        self.horizontalLayout_11.addWidget(self.checkBox_unknown)

        self.check_history = QCheckBox(self.frame_6)
        self.check_history.setObjectName(u"check_history")

        self.horizontalLayout_11.addWidget(self.check_history)

        self.checkBox_3 = QCheckBox(self.frame_6)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.horizontalLayout_11.addWidget(self.checkBox_3)

        self.checkBox_4 = QCheckBox(self.frame_6)
        self.checkBox_4.setObjectName(u"checkBox_4")

        self.horizontalLayout_11.addWidget(self.checkBox_4)


        self.verticalLayout_22.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.game_head)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.comboBox_history = QComboBox(self.frame_7)
        self.comboBox_history.setObjectName(u"comboBox_history")
        self.comboBox_history.setStyleSheet(u"")

        self.horizontalLayout_14.addWidget(self.comboBox_history)

        self.pushButton_history = QPushButton(self.frame_7)
        self.pushButton_history.setObjectName(u"pushButton_history")
        self.pushButton_history.setStyleSheet(u"")

        self.horizontalLayout_14.addWidget(self.pushButton_history)


        self.verticalLayout_22.addWidget(self.frame_7)


        self.verticalLayout_15.addWidget(self.game_head)

        self.game_proBar = QFrame(self.game_body)
        self.game_proBar.setObjectName(u"game_proBar")
        self.game_proBar.setFrameShape(QFrame.StyledPanel)
        self.game_proBar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.game_proBar)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 5, 0, 5)
        self.progressBar = QProgressBar(self.game_proBar)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(24)

        self.verticalLayout_21.addWidget(self.progressBar)


        self.verticalLayout_15.addWidget(self.game_proBar)

        self.game_font = QFrame(self.game_body)
        self.game_font.setObjectName(u"game_font")
        self.game_font.setFrameShape(QFrame.StyledPanel)
        self.game_font.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.game_font)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.textEdit_info = QTextEdit(self.game_font)
        self.textEdit_info.setObjectName(u"textEdit_info")
        self.textEdit_info.setStyleSheet(u"")

        self.verticalLayout_16.addWidget(self.textEdit_info)


        self.verticalLayout_15.addWidget(self.game_font)


        self.verticalLayout_19.addWidget(self.game_body)


        self.horizontalLayout_12.addWidget(self.game_info)

        self.textEdit_output = QTextEdit(self.frame_4)
        self.textEdit_output.setObjectName(u"textEdit_output")
        self.textEdit_output.setStyleSheet(u"")

        self.horizontalLayout_12.addWidget(self.textEdit_output)


        self.verticalLayout_14.addWidget(self.frame_4)

        self.stackedWidget.addWidget(self.game)

        self.verticalLayout_10.addWidget(self.stackedWidget)


        self.verticalLayout_4.addWidget(self.pagesContainer)


        self.verticalLayout_9.addWidget(self.content)

        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 0))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setStyleSheet(u"")
        self.bottomBar.setFrameShape(QFrame.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.creditsLabel = QLabel(self.bottomBar)
        self.creditsLabel.setObjectName(u"creditsLabel")
        self.creditsLabel.setEnabled(True)
        self.creditsLabel.setMaximumSize(QSize(16777215, 16))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setBold(False)
        font3.setItalic(False)
        self.creditsLabel.setFont(font3)
        self.creditsLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.creditsLabel)

        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
        self.version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.version)

        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_3.addWidget(self.frame_size_grip)


        self.verticalLayout_9.addWidget(self.bottomBar)


        self.verticalLayout_3.addWidget(self.contentBottom)


        self.horizontalLayout.addWidget(self.contentBox)


        self.appMargins.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"Hide", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"\u914d\u7f6e", None))
        self.btn_game.setText(QCoreApplication.translate("MainWindow", u"\u8fd0\u884c", None))
        self.btn_refresh.setText(QCoreApplication.translate("MainWindow", u"\u5237\u65b0", None))
        self.btn_info.setText(QCoreApplication.translate("MainWindow", u"\u4e3b\u9875", None))
        self.btn_style.setText(QCoreApplication.translate("MainWindow", u"\u4e3b\u9898", None))
        self.btn_exit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.toggleLeftBox.setText(QCoreApplication.translate("MainWindow", u"Left Box", None))
        self.titleRightInfo.setText(QCoreApplication.translate("MainWindow", u"\u4e0d\u77e5\u53e4\u9053\u4e0a\u7684\u98ce\u4ece\u4f55\u5904\u8d77\uff0c\u53ef\u5b83\u53bb\u5f80\u7684\u662f\u6545\u91cc - \u4f3d\u7f57", None))
#if QT_CONFIG(tooltip)
        self.settingsTopBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Settings", None))
#endif // QT_CONFIG(tooltip)
        self.settingsTopBtn.setText("")
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
        self.label_title.setText(QCoreApplication.translate("MainWindow", u"\u914d\u7f6e", None))
        self.label_size.setText(QCoreApplication.translate("MainWindow", u"size:", None))
        self.label_page.setText(QCoreApplication.translate("MainWindow", u"page:", None))
        self.label_flag.setText(QCoreApplication.translate("MainWindow", u"flag:", None))
        self.label_timeout.setText(QCoreApplication.translate("MainWindow", u"timeout:", None))
        self.label_outputType.setText(QCoreApplication.translate("MainWindow", u"outputType:", None))
        self.label_outputPath.setText(QCoreApplication.translate("MainWindow", u"outputPath:", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"flag          \u6bcf\u4e2a\u57ce\u5e02\u662f\u5426\u722c\u53d6\u5b8c\uff0c\u4e14\u8bbe\u7f6e\u540e page \u65e0\u6548 - \u9ed8\u8ba4 False\n"
"\n"
"\n"
"size          \u722c\u53d6\u6bcf\u9875\u7684\u5927\u5c0f - \u9ed8\u8ba4 20\u4e2a\n"
"\n"
"\n"
"page          \u6bcf\u4e2a\u57ce\u5e02\u722c\u53d6\u7684\u9875\u6570 - \u9ed8\u8ba4500\u9875\n"
"\n"
"\n"
"timeout       \u8bf7\u6c42\u5ef6\u8fdf,\u5373\u6bcf\u6b21\u8bf7\u6c42\u7684\u95f4\u9694 - \u9ed8\u8ba4 0.0\n"
"\n"
"\n"
"outputType    \u8f93\u51fa\u7c7b\u578b\u5305\u542b csv\u3001json\u3001txt - \u9ed8\u8ba4 txt\n"
"\n"
"\n"
"outputPath    \u8f93\u51fa\u8def\u5f84 - \u9ed8\u8ba4 ./output/url.txt\n"
"", None))
        self.pushButton_programme1.setText(QCoreApplication.translate("MainWindow", u"JSON\u8f93\u51fa", None))
        self.pushButton_programme2.setText(QCoreApplication.translate("MainWindow", u"CSV\u8f93\u51fa", None))
        self.pushButton_programme3.setText(QCoreApplication.translate("MainWindow", u"TXT\u8f93\u51fa", None))
        self.pushButton_programme4.setText(QCoreApplication.translate("MainWindow", u"\u5ef6\u8fdf", None))
        self.pushButton_clear.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u7a7a", None))
        self.pushButton_save.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58", None))
        self.pushButton_close.setText(QCoreApplication.translate("MainWindow", u"\u53d6\u6d88", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u4f5c\u8005\u7b80\u4ecb", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">\u535a\u5ba2\uff1ahttp://www.wjlin0.com</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:1"
                        "2px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">\u9879\u76ee\u5730\u5740\uff1ahttps://github.com/wjlin0/FofaSpider_GUI</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\"><br />\u795e\u79d8\u65b9\u5f0f\uff1awjlgeren@163.com</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">\u4f60\u5e72\u561b~ \u54ce\u54df ~</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-lef"
                        "t:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u4e00\u4e2a\u771f\u6b63\u7684man\uff0c\u4ed6\u77e5\u9053\u81ea\u5df1\u8981\u505a\u4ec0\u4e48 - kun", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"FoFaSpider", None))
        self.label_code.setText(QCoreApplication.translate("MainWindow", u"\u67e5\u8be2\u6761\u4ef6", None))
        self.label_cookies.setText(QCoreApplication.translate("MainWindow", u"\u67e5\u8be2cookies", None))
        self.lineEdit_code.setText("")
        self.lineEdit_cookies.setText("")
        self.pushButton_run.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb", None))
        self.pushButton_pause.setText(QCoreApplication.translate("MainWindow", u"\u6682\u505c", None))
        self.pushButton_resume.setText(QCoreApplication.translate("MainWindow", u"\u6062\u590d", None))
        self.pushButton_cancel.setText(QCoreApplication.translate("MainWindow", u"\u53d6\u6d88", None))
        self.pushButton_Orun.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u51fa\u5f53\u524d\u67e5\u8be2", None))
        self.checkBox_unknown.setText(QCoreApplication.translate("MainWindow", u"\u8df3\u8fc7unknown\u7684\u57ce\u5e02", None))
        self.check_history.setText(QCoreApplication.translate("MainWindow", u"\u67e5\u8be2\u662f\u5426\u8986\u76d6\u5386\u53f2\u67e5\u8be2", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"\u5f85\u5b9a", None))
        self.checkBox_4.setText(QCoreApplication.translate("MainWindow", u"\u5f85\u5b9a", None))
        self.pushButton_history.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u51fa\u5386\u53f2\u67e5\u8be2", None))
        self.textEdit_info.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.textEdit_output.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u76f4\u63a5\u8f93\u5165\u67e5\u8be2\u8bed\u53e5\uff0c\u5c06\u4ece\u6807\u9898\uff0chtml\u5185\u5bb9\uff0chttp\u5934\u4fe1\u606f\uff0curl\u5b57\u6bb5\u4e2d\u641c\u7d22</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u2022 title=&quot;abc&quot; \u4ece\u6807\u9898"
                        "\u4e2d\u641c\u7d22abc\u3002\u4f8b\uff1a\u6807\u9898\u4e2d\u6709\u5317\u4eac\u7684\u7f51\u7ad9</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u2022 header=&quot;abc&quot; \u4ecehttp\u5934\u4e2d\u641c\u7d22abc\u3002\u4f8b\uff1ajboss\u670d\u52a1\u5668</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u2022 body=&quot;abc&quot; \u4ecehtml\u6b63\u6587\u4e2d\u641c\u7d22abc\u3002\u4f8b\uff1a\u6b63\u6587\u5305\u542bHacked by</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-"
                        "block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u2022 domain=&quot;qq.com&quot; \u641c\u7d22\u6839\u57df\u540d\u5e26\u6709qq.com\u7684\u7f51\u7ad9\u3002\u4f8b\uff1a \u6839\u57df\u540d\u662fqq.com\u7684\u7f51\u7ad9</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u2022 host=&quot;.gov.cn&quot; \u4eceurl\u4e2d\u641c\u7d22.gov.cn,\u6ce8\u610f\u641c\u7d22\u8981\u7528host\u4f5c\u4e3a\u540d\u79f0\u3002\u4f8b\uff1a \u653f\u5e9c\u7f51\u7ad9, \u6559\u80b2\u7f51\u7ad9</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px;"
                        " margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u2022 port=&quot;443&quot; \u67e5\u627e\u5bf9\u5e94443\u7aef\u53e3\u7684\u8d44\u4ea7\u3002\u4f8b\uff1a \u67e5\u627e\u5bf9\u5e94443\u7aef\u53e3\u7684\u8d44\u4ea7</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u2022 ip=&quot;1.1.1.1&quot; \u4eceip\u4e2d\u641c\u7d22\u5305\u542b1.1.1.1\u7684\u7f51\u7ad9,\u6ce8\u610f\u641c\u7d22\u8981\u7528ip\u4f5c\u4e3a\u540d\u79f0\u3002\u4f8b\uff1a \u67e5\u8be2IP\u4e3a220.181.111.1\u7684\u7f51\u7ad9; \u5982\u679c\u60f3\u8981\u67e5\u8be2\u7f51\u6bb5\uff0c\u53ef\u4ee5\u662f\uff1a ip=&quot;220.181.111.1/24&quot;\uff0c\u4f8b\u5982\u67e5\u8be2IP\u4e3a220.181.111.1\u7684C\u7f51\u6bb5\u8d44\u4ea7</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0p"
                        "x; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u2022 protocol=&quot;https&quot; \u641c\u7d22\u6307\u5b9a\u534f\u8bae\u7c7b\u578b(\u5728\u5f00\u542f\u7aef\u53e3\u626b\u63cf\u7684\u60c5\u51b5\u4e0b\u6709\u6548)\u3002\u4f8b\uff1a \u67e5\u8be2https\u534f\u8bae\u8d44\u4ea7</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u2022 city=&quot;Hangzhou&quot; \u641c\u7d22\u6307\u5b9a\u57ce\u5e02\u7684\u8d44\u4ea7\u3002\u4f8b\uff1a \u641c\u7d22\u6307\u5b9a\u57ce\u5e02\u7684\u8d44\u4ea7</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-"
                        "block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u2022 region=&quot;Zhejiang&quot; \u641c\u7d22\u6307\u5b9a\u884c\u653f\u533a\u7684\u8d44\u4ea7\u3002\u4f8b\uff1a \u641c\u7d22\u6307\u5b9a\u884c\u653f\u533a\u7684\u8d44\u4ea7</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u2022 country=&quot;CN&quot; \u641c\u7d22\u6307\u5b9a\u56fd\u5bb6(\u7f16\u7801)\u7684\u8d44\u4ea7\u3002\u4f8b\uff1a \u641c\u7d22\u6307\u5b9a\u56fd\u5bb6(\u7f16\u7801)\u7684\u8d44\u4ea7</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin"
                        "-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u2022 cert=&quot;google&quot; \u641c\u7d22\u8bc1\u4e66(https\u6216\u8005imaps\u7b49)\u4e2d\u5e26\u6709google\u7684\u8d44\u4ea7\u3002\u4f8b\uff1a \u641c\u7d22\u8bc1\u4e66(https\u6216\u8005imaps\u7b49)\u4e2d\u5e26\u6709google\u7684\u8d44\u4ea7</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u2022 banner=users &amp;&amp; protocol=ftp \u641c\u7d22FTP\u534f\u8bae\u4e2d\u5e26\u6709users\u6587\u672c\u7684\u8d44\u4ea7\u3002\u4f8b\uff1a \u641c\u7d22FTP\u534f\u8bae\u4e2d\u5e26\u6709users\u6587\u672c\u7684\u8d44\u4ea7</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" "
                        "margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u2022 type=service \u641c\u7d22\u6240\u6709\u534f\u8bae\u8d44\u4ea7\uff0c\u652f\u6301subdomain\u548cservice\u4e24\u79cd\u3002\u4f8b\uff1a \u641c\u7d22\u6240\u6709\u534f\u8bae\u8d44\u4ea7</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u2022 os=windows \u641c\u7d22Windows\u8d44\u4ea7\u3002\u4f8b\uff1a \u641c\u7d22Windows\u8d44\u4ea7</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u2022 server==&quot;Microsoft-IIS/7.5&quot; \u641c"
                        "\u7d22IIS 7.5\u670d\u52a1\u5668\u3002\u4f8b\uff1a \u641c\u7d22IIS 7.5\u670d\u52a1\u5668</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u2022 app=&quot;\u6d77\u5eb7\u5a01\u89c6-\u89c6\u9891\u76d1\u63a7&quot; \u641c\u7d22\u6d77\u5eb7\u5a01\u89c6\u8bbe\u5907\uff0c\u66f4\u591aapp\u89c4\u5219\u3002\u4f8b\uff1a \u641c\u7d22\u6d77\u5eb7\u5a01\u89c6\u8bbe\u5907</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u2022 after=&quot;2017&quot; &amp;&amp; before=&quot;2017-10-01&quot; \u65f6\u95f4\u8303\u56f4\u6bb5\u641c\u7d22\u3002\u4f8b\uff1a \u65f6"
                        "\u95f4\u8303\u56f4\u6bb5\u641c\u7d22\uff0c\u6ce8\u610f\uff1a after\u662f\u5927\u4e8e\u5e76\u4e14\u7b49\u4e8e\uff0cbefore\u662f\u5c0f\u4e8e\uff0c\u8fd9\u91ccafter=&quot;2017&quot; \u5c31\u662f\u65e5\u671f\u5927\u4e8e\u5e76\u4e14\u7b49\u4e8e 2017-01-01 \u7684\u6570\u636e\uff0c\u800c before=&quot;2017-10-01&quot; \u5219\u662f\u5c0f\u4e8e 2017-10-01 \u7684\u6570\u636e</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u2022 asn=&quot;19551&quot; \u641c\u7d22\u6307\u5b9aasn\u7684\u8d44\u4ea7\u3002\u4f8b\uff1a \u641c\u7d22\u6307\u5b9aasn\u7684\u8d44\u4ea7</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0"
                        "px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u2022 org=&quot;Amazon.com, Inc.&quot; \u641c\u7d22\u6307\u5b9aorg(\u7ec4\u7ec7)\u7684\u8d44\u4ea7\u3002\u4f8b\uff1a \u641c\u7d22\u6307\u5b9aorg(\u7ec4\u7ec7)\u7684\u8d44\u4ea7</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u2022 base_protocol=&quot;udp&quot; \u641c\u7d22\u6307\u5b9audp\u534f\u8bae\u7684\u8d44\u4ea7\u3002\u4f8b\uff1a \u641c\u7d22\u6307\u5b9audp\u534f\u8bae\u7684\u8d44\u4ea7</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u2022 is_ipv6=true \u641c\u7d22ipv"
                        "6\u7684\u8d44\u4ea7,\u53ea\u63a5\u53d7true\u548cfalse\u3002\u4f8b\uff1a \u641c\u7d22ipv6\u7684\u8d44\u4ea7</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u2022 is_domain=true \u641c\u7d22\u57df\u540d\u7684\u8d44\u4ea7,\u53ea\u63a5\u53d7true\u548cfalse\u3002\u4f8b\uff1a \u641c\u7d22\u57df\u540d\u7684\u8d44\u4ea7</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u2022 ip_ports=&quot;80,443&quot; \u6216\u8005 ports=&quot;80,443&quot; \u641c\u7d22\u540c\u65f6\u5f00\u653e80\u548c443\u7aef\u53e3\u7684ip\u8d44\u4ea7(\u4ee5ip\u4e3a\u5355\u4f4d"
                        "\u7684\u8d44\u4ea7\u6570\u636e)\u3002\u4f8b\uff1a \u641c\u7d22\u540c\u65f6\u5f00\u653e80\u548c443\u7aef\u53e3\u7684ip</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u2022 ip_country=&quot;CN&quot; \u641c\u7d22\u4e2d\u56fd\u7684ip\u8d44\u4ea7(\u4ee5ip\u4e3a\u5355\u4f4d\u7684\u8d44\u4ea7\u6570\u636e)\u3002\u4f8b\uff1a \u641c\u7d22\u4e2d\u56fd\u7684ip\u8d44\u4ea7</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u2022 ip_region=&quot;Zhejiang&quot; \u641c\u7d22\u6307\u5b9a\u884c\u653f\u533a\u7684ip\u8d44\u4ea7(\u4ee5ip\u4e3a\u5355\u4f4d\u7684"
                        "\u8d44\u4ea7\u6570\u636e)\u3002\u4f8b\uff1a \u641c\u7d22\u6307\u5b9a\u884c\u653f\u533a\u7684\u8d44\u4ea7</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u2022 ip_city=&quot;Hangzhou&quot; \u641c\u7d22\u6307\u5b9a\u57ce\u5e02\u7684ip\u8d44\u4ea7(\u4ee5ip\u4e3a\u5355\u4f4d\u7684\u8d44\u4ea7\u6570\u636e)\u3002\u4f8b\uff1a \u641c\u7d22\u6307\u5b9a\u57ce\u5e02\u7684\u8d44\u4ea7</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u2022 ip_after=&quot;2019-01-01&quot; \u641c\u7d222019-01-01\u4ee5\u540e\u7684ip\u8d44\u4ea7(\u4ee5ip\u4e3a\u5355\u4f4d"
                        "\u7684\u8d44\u4ea7\u6570\u636e)\u3002\u4f8b\uff1a \u641c\u7d222019-01-01\u4ee5\u540e\u7684ip\u8d44\u4ea7</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u2022 ip_before=&quot;2019-01-01&quot; \u641c\u7d222019-01-01\u4ee5\u524d\u7684ip\u8d44\u4ea7(\u4ee5ip\u4e3a\u5355\u4f4d\u7684\u8d44\u4ea7\u6570\u636e)\u3002\u4f8b\uff1a \u641c\u7d222019-01-01\u4ee5\u524d\u7684ip\u8d44\u4ea7</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0p"
                        "x; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u9ad8\u7ea7\u641c\u7d22\uff1a\u53ef\u4ee5\u4f7f\u7528\u62ec\u53f7 \u548c &amp;&amp; || !=\u7b49\u7b26\u53f7\uff0c\u5982</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">title=&quot;powered by&quot; &amp;&amp; title!=discuz</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">title!=&quot;powered by&quot; &amp;&amp; body=discuz</p></body></html>", None))
        self.creditsLabel.setText(QCoreApplication.translate("MainWindow", u"By: fofaSpider - wjlin0 \u6539\u7f16\u81f3 PyDracula", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"v5.0.2", None))
    # retranslateUi

