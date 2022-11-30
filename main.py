#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author   :wjlin0
# @Blog     :https://wjlin0.com
# @Email    :wjlgeren@163.com
# @Time     :2022-07-10 15:34
# @File     :main.py
import os
import re
import sys
import time

from PySide6.QtGui import QFont
from PySide6.QtWidgets import QMainWindow, QToolTip, QFileDialog, QApplication
from modules.ui_main import Ui_MainWindow
from modules import *
from modules.C import fofaSpider
from modules.time import now
from modules.util import csvSave, jsonSave, outputSave

os.environ["QT_FONT_DPI"] = "96"  # FIX Problem for High DPI and Scale above 100%
widgets = None
config = {
    'flag': False,
    'size': 20,
    'page': 300,
    'worker': 2,
    'timeout': 0.0,
    'outputPath': os.path.abspath("output/url.txt"),
    'outputType': "txt",
}


class MainWindow(QMainWindow):

    def __init__(self, *arg):
        super().__init__(*arg)
        self.__re = True
        self.ishistory = False
        self.runFlag = False
        self.config = config
        self.startRun = False
        self.styleInfo = ""
        self.ui = Ui_MainWindow()

        self.ui.setupUi(self)
        # self.ui.styleSheet.setStyleSheet()
        self.db = db.SQL()
        self.configShow()
        QToolTip.setFont(QFont('Decorative', 8, QFont.Bold))
        Settings.ENABLE_CUSTOM_TITLE_BAR = True
        if Settings.ENABLE_CUSTOM_TITLE_BAR:
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)
        UIFunctions.uiDefinitions(self)
        global widgets
        widgets = self.ui
        title = "wjlin0 - fofaSpider GUI"
        description = "不知古道上的风从何处起，可它去往的是故里 - 伽罗."
        # APPLY TEXTS
        self.setWindowTitle(title)
        self.get_history()
        self.ui.check_history.setChecked(True)
        self.ui.checkBox_unknown.setChecked(True)
        widgets.titleRightInfo.setText(description)
        # TOGGLE MENU
        # ///////////////////////////////////////////////////////////////
        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))
        # LEFT MENUS
        widgets.btn_home.clicked.connect(self.buttonClick)
        widgets.btn_game.clicked.connect(self.buttonClick)
        widgets.btn_refresh.clicked.connect(self.buttonClick)
        widgets.btn_info.clicked.connect(self.buttonClick)
        widgets.btn_style.clicked.connect(self.buttonClick)
        widgets.btn_exit.clicked.connect(lambda: self.close())
        widgets.pushButton_clear.clicked.connect(self.buttonClick)
        widgets.pushButton_save.clicked.connect(self.buttonClick)
        widgets.pushButton_history.clicked.connect(self.searchHistory)
        widgets.toggleLeftBox.clicked.connect(self.buttonClick)
        widgets.settingsTopBtn.clicked.connect(self.buttonClick)
        widgets.pushButton_programme1.clicked.connect(self.buttonClick)
        widgets.pushButton_programme2.clicked.connect(self.buttonClick)
        widgets.pushButton_programme3.clicked.connect(self.buttonClick)
        widgets.pushButton_programme4.clicked.connect(self.buttonClick)
        widgets.pushButton_Orun.clicked.connect(self.output)

        ## 开始 暂停 恢复 取消
        widgets.pushButton_run.clicked.connect(self.gameRun)
        widgets.pushButton_pause.clicked.connect(self.__pause)
        widgets.pushButton_resume.clicked.connect(self.__resume)
        widgets.pushButton_cancel.clicked.connect(self.__cancel)
        widgets.pushButton_Orun.setEnabled(False)
        widgets.pushButton_pause.setEnabled(False)
        widgets.pushButton_resume.setEnabled(False)
        widgets.pushButton_cancel.setEnabled(False)

        # SET style
        self.getStyle()
        # SET CODE TIP
        self.codeTip()
        self.cookiesShow()
        # 修改进度条
        self.ui.progressBar.setMinimum(0)
        self.ui.progressBar.setMaximum(100)
        self.ui.progressBar.setValue(0)

    def deleteHistory(self):
        t = self.ui.check_history.isChecked()
        code = self.ui.lineEdit_code.text()
        # code = re.escape(code)
        # table_name = self.db.query_data(f'select table_name from history where code="{code}"')
        table_name = self.db.queryData("select table_name from history where code=:codes", {
            "codes": code
        })
        if table_name is None:
            return
        table_name = table_name[0]
        if not t:
            return
        self.db.DROP_tables(table_name)

    def searchHistory(self):
        dir_path = QFileDialog.getExistingDirectory(self, "choose directory", os.path.dirname("."))
        if dir_path == "":
            self.setTextInfo("请正确选择路径")
            return
        code = self.ui.comboBox_history.currentText()
        table_name = self.db.queryData("select table_name from history where code=:codes", {
            "codes": code
        })[0]
        # table_name = self.db.query_data(f"select table_name from history where code=\"{code}\"")[0]
        method = self.db.queryData("select outputType from config")[0]
        name = "/output_" + str(int(time.time())) + "." + method
        datas = self.db.query_data_all(f"select * from {table_name}")
        datas = self.tupleToDict(datas)
        if method == 'txt':
            outputSave(datas, dir_path + name)
        elif method == 'csv':
            csvSave(datas, dir_path + name)
        elif method == 'json':
            jsonSave(datas, dir_path + name)
        self.setTextInfo("导出完成")

    def __cancel(self):
        self.ui.pushButton_run.setEnabled(True)
        self.ui.pushButton_pause.setEnabled(False)
        self.ui.pushButton_resume.setEnabled(False)
        self.ui.pushButton_cancel.setEnabled(False)
        self.ui.pushButton_save.setEnabled(False)
        self.fofa.cancel()

    def __resume(self):
        self.ui.pushButton_run.setEnabled(False)
        self.ui.pushButton_pause.setEnabled(True)
        self.ui.pushButton_resume.setEnabled(False)
        self.ui.pushButton_cancel.setEnabled(True)
        self.fofa.resume()

    def __pause(self):
        self.ui.pushButton_run.setEnabled(False)
        self.ui.pushButton_pause.setEnabled(False)
        self.ui.pushButton_resume.setEnabled(True)
        self.ui.pushButton_cancel.setEnabled(True)
        self.fofa.pause()

    def BarNew(self, value, maximum, start=0):
        if start == 1:
            self.ui.progressBar.setMinimum(0)
            self.ui.progressBar.setMaximum(maximum)
        if start == 2:
            self.ui.progressBar.setValue(self.ui.progressBar.maximum())
            return
        self.ui.progressBar.setValue(value)

    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        if btnName == "toggleLeftBox":
            widgets.stackedWidget.setCurrentWidget(widgets.home)  # SET PAGE

        if btnName == "settingsTopBtn":
            widgets.stackedWidget.setCurrentWidget(widgets.home)  # SET PAGE

        # SHOW HOME PAGE
        if btnName == "btn_home":
            widgets.stackedWidget.setCurrentWidget(widgets.home)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW WIDGETS PAGE
        if btnName == "btn_game":
            widgets.stackedWidget.setCurrentWidget(widgets.game)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW NEW PAGE
        if btnName == "btn_new":
            widgets.stackedWidget.setCurrentWidget(widgets.new_page)  # SET PAGE
            UIFunctions.resetStyle(self, btnName)  # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))  # SELECT MENU
        if btnName == "btn_style":
            self. __reStyle()
        if btnName == "btn_refresh":
            self.__refresh()
        if btnName == "btn_info":
            loguru.logger.info("Save btn_info clicked!")
            widgets.stackedWidget.setCurrentWidget(widgets.info)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
        if btnName == "pushButton_clear":
            UIFunctions.configClear(self, widgets)
        if btnName == "pushButton_save":
            UIFunctions.configSave(self, widgets)
        from modules import configModules
        if btnName == "pushButton_programme1":
            configModules.config.Json(self)
        if btnName == "pushButton_programme2":
            configModules.config.Csv(self)
        if btnName == "pushButton_programme3":
            configModules.config.Txt(self)
        if btnName == "pushButton_programme4":
            configModules.config.Timeout(self)
        # PRINT BTN NAME
        loguru.logger.info(f'Button "{btnName}" pressed!')
        # RESIZE EVENTS
        # ///////////////////////////////////////////////////////////////

    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()

        # PRINT MOUSE EVENTS
        if event.buttons() == Qt.LeftButton:
            loguru.logger.info('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            loguru.logger.info('Mouse click: RIGHT CLICK')

    def configShow(self):
        c = self.db.queryData("select * from config")
        if c[1] == '0' or c[1] == '' or c[1] == 'None' or c[1] == 'False' or c[1]=='false' or c[1] == 'none':
            flag = "0"
        else:
            flag = c[1]
        self.ui.lineEdit_flag.clear()
        self.ui.lineEdit_page.clear()
        self.ui.lineEdit_size.clear()
        self.ui.lineEdit_timeout.clear()
        self.ui.lineEdit_outputPath.clear()
        self.ui.lineEdit_outputType.clear()
        self.ui.lineEdit_flag.setText(str(flag))
        self.ui.lineEdit_page.setText(str(c[2]))
        self.ui.lineEdit_size.setText(str(c[3]))
        # self.ui.lineEdit_worker.setText(str(c[4]))
        self.ui.lineEdit_timeout.setText(str(c[5]))
        self.ui.lineEdit_outputType.setText(str(c[6]))
        self.ui.lineEdit_outputPath.setText(str(c[7]))

    def cookiesShow(self):
        datas = self.db.queryData("select * from cookies")
        if datas:
            self.ui.lineEdit_cookies.setText(datas[1])

    def codeTip(self):
        datas = self.db.query_data_all("select * from history")
        text = ""
        if datas:
            for data in datas:
                t = time.localtime(int(float(data[4])))
                text += f"code: {data[2]}, time: {time.strftime('%Y-%m-%d %H:%M:%S', t)}\n"
        else:
            text = "暂无任何数据"
        self.ui.lineEdit_code.setToolTip(text)

    def gameRun(self):

        if self.runFlag:
            self.setTextInfo("上一任务正在运行请稍后....")
            return
        self.codeTip()
        self.code = self.ui.lineEdit_code.text()
        self.cookie = self.ui.lineEdit_cookies.text()
        if not self.checkArg():
            QMessageBox.warning(self.ui.game, "参数错误", "cookie 查询参数不能为空")
            return
        self.ui.pushButton_run.setEnabled(False)
        self.ui.pushButton_pause.setEnabled(True)
        self.ui.pushButton_resume.setEnabled(False)
        self.ui.pushButton_cancel.setEnabled(True)
        self.ui.pushButton_save.setEnabled(True)
        self.fofa = fofaSpider(main=self)
        self.fofa.signal.connect(self.loginTip)
        self.fofa.signalBar.connect(self.BarNew)
        self.fofa.signalText.connect(self.setTextInfo)
        self.fofa.signalError.connect(self.setTextInfo)
        self.fofa.signalHistory.connect(self.history)
        self.fofa.start()

    def history(self, d):
        if d is not None:
            pass

    def setTextInfo(self, s):
        if s == "closeThread":
            self.__cancel()
            return
        self.ui.textEdit_info.append(now() + " " + s)

    def loginTip(self, ok):
        if ok == "0":
            self.setTextInfo("登录失败")
            QMessageBox.information(widgets.game, "登录失败", "登录失败")
        elif ok == "1":
            self.setTextInfo("登录成功")
            self.ui.progressBar.setValue(100)
        else:
            self.setTextInfo("登录失败")
            QMessageBox.information(widgets.game, "登录失败", ok)
        if ok != "1":
            self.runFlag = False
            return

    def output(self):
        dir_path = QFileDialog.getExistingDirectory(self, "choose directory", os.path.dirname("."))
        if dir_path == "":
            return
        # d = self.db.query_data("select table_name from cookies")
        d = self.db.queryData("select table_name from cookies")
        table_name = d[0]
        # c = self.db.query_data("select outputType from config")
        c = self.db.queryData("select outputType from config")
        method = c[0]
        name = "/output_" + str(int(time.time())) + "." + method
        data = self.db.queryDataAll("select * from :tablename", {
            'table_name': table_name
        })
        # data = self.db.query_data_all(f"select * from {table_name}")
        data = self.tupleToDict(data)
        if method == 'txt':
            outputSave(data, dir_path + name)
        elif method == 'csv':
            csvSave(data, dir_path + name)
        elif method == 'json':
            jsonSave(data, dir_path + name)
        self.setTextInfo("导出完成")

    def checkArg(self):
        if self.ui.lineEdit_code.text() == "" or self.ui.lineEdit_cookies == "":
            return False
        return True

    def __refresh(self):
        self.configShow()
        self.get_history()

    def tupleToDict(self, data: list):
        dataList = []
        for d in data:
            temp = {
                'url': d[1],
                'port': d[2],
                'title': d[3],
                'host': d[4],
                'addr': d[5],
                'server': d[6],
                'code': d[7],
            }
            dataList.append(temp)
        return dataList

    def get_history(self):
        names = list()
        temps = self.db.query_data_all("select code from history")
        for temp in temps:
            names.append(temp[0])
        self.ui.comboBox_history.clear()
        self.ui.comboBox_history.addItems(names)

    def __reStyle(self):
        if self.__re:
            self.__re = False
            with open("themes/py_dracula_light.qss", "r") as f:
                styleInfo = f.read()
            self.ui.btn_style.setStyleSheet("background-image: url(:/icons/icons/cil-moon.png);")
        else:
            self.__re = True
            with open("themes/py_dracula_dark.qss", "r") as f:
                styleInfo = f.read()

            self.ui.btn_style.setStyleSheet("background-image: url(:/icons/icons/cil-lightbulb.png);")
        self.ui.styleSheet.setStyleSheet(styleInfo)

    def getStyle(self):
        d = time.localtime()

        if d.tm_hour < 12:
            self.__re = True
        else:
            self.__re = False
        self.__reStyle()


def InitDB():
    config_fields = [
        'ID INTEGER PRIMARY KEY autoincrement', 'flag TEXT',
        'page INT', 'size INT', 'worker INT', 'timeout TEXT', 'outputType TEXT', 'outputPath TEXT'
    ]
    history_fields = [
        'ID INTEGER PRIMARY KEY autoincrement',
        'table_name TEXT', 'code TEXT', 'progress TEXT', "startTime TEXT", "num INT"
    ]
    search_fields = [
        'ID INTEGER PRIMARY KEY autoincrement', 'country TEXT', 'city TEXT', 'url TEXT not null', 'num INT'
    ]
    cookies_fields = [
        'ID INTEGER PRIMARY KEY autoincrement', 'cookies TEXT NOT NULL', 'table_name TEXT NOT NULL',
        'startTime TEXT NOT NULL',
        'endTime TEXT NOT NULL'
    ]
    if os.path.exists(os.path.abspath("spider.sqlite3")):
        c = db.SQL()
        d = c.queryData("select * from sqlite_master where tbl_name='search';")
        if d is not None:
            c.cursor.execute("DROP TABLE search;")
            c.create_tables("search", search_fields)
        return
    conn = db.SQL()
    conn.create_tables("config", config_fields)
    conn.create_tables("history", history_fields)
    conn.create_tables("search", search_fields)
    conn.create_tables("cookies", cookies_fields)
    conn.insert_data("config", config)


def InitLog():
    today = time.strftime('%Y%m%d', time.localtime(time.time()))
    loguru.logger.add('./log/' + today + '.log', rotation='1 day', retention='30 days', encoding='utf-8')


if __name__ == "__main__":
    InitDB()
    InitLog()
    try:
        app = QApplication([])
        app.setWindowIcon(QIcon("icon.ico"))
        window = MainWindow()
        window.show()
        sys.exit(app.exec())
    except Exception as e:
        loguru.logger.info(e)
