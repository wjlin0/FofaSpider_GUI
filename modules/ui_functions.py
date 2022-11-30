#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author   :wjlin0
# @Blog     :https://wjlin0.com
# @Email    :wjlgeren@163.com
# @Time     :2022-07-10 16:08
# @File     :ui_functions.py
import os

from PySide6.QtCore import QEasingCurve, QEvent, QTimer, Qt, QPropertyAnimation
from PySide6.QtGui import QIcon, QColor
from PySide6.QtWidgets import QPushButton, QGraphicsDropShadowEffect, QSizeGrip, QMessageBox
import main
from . import Settings

GLOBAL_STATE = False
GLOBAL_TITLE_BAR = True


class UIFunctions(main.MainWindow):

    def maximize_restore(self):
        global GLOBAL_STATE
        status = GLOBAL_STATE
        if not status:
            self.showMaximized()
            GLOBAL_STATE = True
            self.ui.appMargins.setContentsMargins(0, 0, 0, 0)
            self.ui.maximizeRestoreAppBtn.setToolTip("Restore")
            self.ui.maximizeRestoreAppBtn.setIcon(QIcon(u":/icons/icons/icon_restore.png"))
            self.ui.frame_size_grip.hide()

        else:
            GLOBAL_STATE = False
            self.showNormal()
            self.resize(self.width() + 1, self.height() + 1)
            self.ui.appMargins.setContentsMargins(10, 10, 10, 10)
            self.ui.maximizeRestoreAppBtn.setToolTip("Maximize")
            self.ui.maximizeRestoreAppBtn.setIcon(QIcon(u":/icons/icons/icon_maximize.png"))
            self.ui.frame_size_grip.show()

    def toggleMenu(self, enable):
        if enable:
            # GET WIDTH
            width = self.ui.leftMenuBg.width()
            maxExtend = Settings.MENU_WIDTH
            standard = 60

            # SET MAX WIDTH
            if width == 60:
                widthExtended = maxExtend
            else:
                widthExtended = standard

            # ANIMATION
            self.animation = QPropertyAnimation(self.ui.leftMenuBg, b"minimumWidth")
            self.animation.setDuration(Settings.TIME_ANIMATION)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QEasingCurve.InOutQuart)
            self.animation.start()

    def resetStyle(self, widget):
        for w in self.ui.topMenu.findChildren(QPushButton):
            if w.objectName() != widget:
                w.setStyleSheet(UIFunctions.deselectMenu(w.styleSheet()))

    def selectMenu(getStyle):
        select = getStyle + Settings.MENU_SELECTED_STYLESHEET
        return select

    def deselectMenu(getStyle):
        deselect = getStyle.replace(Settings.MENU_SELECTED_STYLESHEET, "")
        return deselect

    def resize_grips(self):
        if Settings.ENABLE_CUSTOM_TITLE_BAR:
            pass
            # self.left_grip.setGeometry(0, 10, 10, self.height())
            # self.right_grip.setGeometry(self.width() - 10, 10, 10, self.height())
            # self.top_grip.setGeometry(0, 0, self.width(), 10)
            # self.bottom_grip.setGeometry(0, self.height() - 10, self.width(), 10)

    def uiDefinitions(self):
        def dobleClickMaximizeRestore(event):
            # IF DOUBLE CLICK CHANGE STATUS
            # pass
            if event.type() == QEvent.MouseButtonDblClick:
                QTimer.singleShot(250, lambda: UIFunctions.maximize_restore(self))

        self.ui.titleRightInfo.mouseDoubleClickEvent = dobleClickMaximizeRestore

        if Settings.ENABLE_CUSTOM_TITLE_BAR:
            # STANDARD TITLE BAR
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)

            # MOVE WINDOW / MAXIMIZE / RESTORE
            def moveWindow(event):
                # IF MAXIMIZED CHANGE TO NORMAL
                if UIFunctions.returStatus(self):
                    UIFunctions.maximize_restore(self)
                # MOVE WINDOW
                if event.buttons() == Qt.LeftButton:
                    self.move(self.pos() + event.globalPos() - self.dragPos)
                    self.dragPos = event.globalPos()
                    event.accept()

            self.ui.titleRightInfo.mouseMoveEvent = moveWindow
        else:
            self.ui.appMargins.setContentsMargins(0, 0, 0, 0)
            self.ui.minimizeAppBtn.hide()
            self.ui.maximizeRestoreAppBtn.hide()
            self.ui.closeAppBtn.hide()
            self.ui.frame_size_grip.hide()
            # DROP SHADOW
            self.shadow = QGraphicsDropShadowEffect(self)
            self.shadow.setBlurRadius(17)
            self.shadow.setXOffset(0)
            self.shadow.setYOffset(0)
            self.shadow.setColor(QColor(0, 0, 0, 150))
            self.ui.bgApp.setGraphicsEffect(self.shadow)

        # RESIZE WINDOW
        self.sizegrip = QSizeGrip(self.ui.frame_size_grip)
        self.sizegrip.setStyleSheet("width: 20px; height: 20px; margin 0px; padding: 0px;")

        # MINIMIZE
        self.ui.minimizeAppBtn.clicked.connect(lambda: self.showMinimized())

        # MAXIMIZE/RESTORE
        self.ui.maximizeRestoreAppBtn.clicked.connect(lambda: UIFunctions.maximize_restore(self))

        # CLOSE APPLICATION
        self.ui.closeAppBtn.clicked.connect(lambda: self.close())

    def returStatus(self):
        return GLOBAL_STATE

    def configClear(self, w):
        w.lineEdit_flag.setText("")
        w.lineEdit_page.setText("")
        w.lineEdit_size.setText("")
        w.lineEdit_timeout.setText("")
        w.lineEdit_outputType.setText("")
        w.lineEdit_outputPath.setText("")

    def configSave(self, w):
        flag = w.lineEdit_flag.text()
        page = w.lineEdit_page.text()
        size = w.lineEdit_size.text()
        timeout = w.lineEdit_timeout.text()
        outputType = w.lineEdit_outputType.text()
        outputPath = w.lineEdit_outputPath.text()
        t = False
        text = ""
        if size != "" and size != '20' and size != '10':
            t = True
            text += "每页大小 只能 20 或 10\n"
        if outputType != "" and outputType != "csv" and outputType != "json" and outputType != "txt":
            t = True
            text += "输出类型 只有 txt、json、csv\n"
        if t:
            QMessageBox.about(w.home, "配置错误", text)
            return
        if flag == "" or flag == "None" or flag == "none" or flag == "False" or flag == "false" or flag == "0":
            flag = False
        else:
            flag = True
        self.config['flag'] = flag
        self.config['page'] = 500 if page == "" else page
        self.config['worker'] = 2
        self.config['timeout'] = 0.0 if timeout == "" else timeout
        self.config['size'] = 20 if size == "" else size
        self.config['outputType'] = "txt" if outputType == "" else outputType
        self.config['outputPath'] = os.path.abspath("output/url.txt") if outputPath == "" else os.path.abspath(
            outputPath)
        if not os.path.exists(os.path.dirname(self.config['outputPath'])):
            os.makedirs(os.path.dirname(self.config['outputPath']))
        if self.db.update_field("config", self.config, ID=1):
            self.configShow()
