#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author   :wjlin0
# @Blog     :https://wjlin0.com
# @Email    :wjlgeren@163.com
# @Time     :2022-07-15 14:41
# @File     :C
import os
import re
import time
from urllib.parse import urljoin

import PySide6
import loguru
from PySide6 import QtCore
from PySide6.QtCore import QThread, Signal, QWaitCondition, QMutex
from PySide6.QtWidgets import QMessageBox

import modules
from . import db
from .util import driver, getDriverSoup, enBase64code, getRelatedSearch, NumCode, getCityUrls, \
    StringToDict, getRequestsSoup, getInfo, UnknownCity


def setDriver(url, cookie):
    try:

        Driver = driver()
        loguru.logger.info("driver 初始化成功")
        Driver.cookies(cookie, url)
        return Driver
    except:
        raise


class fofaSpider(QThread):
    signal = Signal(str)
    signalError = Signal(str)
    signalText = Signal(str)
    signalBar = Signal(int, int, int)
    signalHistory = Signal(tuple)

    def __init__(self, **kwargs):
        super(fofaSpider, self).__init__()
        self.isPause = False
        self.isCancel = False
        self.cond = QWaitCondition()
        self.mutex = QMutex()
        self.main = kwargs.get("main")
        self.db: db.SQL = self.main.db
        self.url = "https://fofa.info"
        self.code = self.main.ui.lineEdit_code.text()
        self.cookies = self.main.ui.lineEdit_cookies.text()
        self.driver = None
        self.userGroup = None
        self.table_ = 'f_' + str(int(float(time.time())))
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/97.0.4692.99 Safari/537.36 Edg/97.0.1072.76 ',
        }
        self.config = modules.config.getConfig(self)
        self.size = self.getSize()
        self.Page = self.getPage()
        self.flag = self.getFlag()

    # 暂停
    def pause(self):
        self.signalText.emit("任务暂停。。。")
        self.isPause = True

    # 恢复
    def resume(self):
        self.signalText.emit("任务恢复。。。")
        self.isPause = False
        self.cond.wakeAll()

    # 取消
    def cancel(self):
        self.signalText.emit("任务取消。。。")
        self.isCancel = True

    def getFlag(self):
        return self.config['flag']

    def getPage(self):
        return self.config['page']

    def getSize(self):
        return self.config['size']

    def __del__(self):
        self.wait()

    def getNum(self):
        datas = self.db.query_data_all("select num from search")
        num = 0
        for d in datas:
            if int(d[0]) > 10000:
                num += 10000
            else:
                num += int(d[0])
        # for key, value in data.items():
        #     for city, info in value.items():
        #         # print(info)
        #         if int(info['num']) > 10000:
        #             num += 10000
        #         else:
        #             num += info['num']
        return num

    def deleteHistory(self):
        t = self.main.ui.check_history.isChecked()
        code = self.main.ui.lineEdit_code.text()
        # code = re.escape(code)
        table_name = self.db.queryData("select table_name from history where code=:codes", {
            "codes": code
        })
        # table_name = self.db.query_data(f'select table_name from history where code="'+code+'"')

        if table_name is None or table_name == []:
            return True
        table_name = table_name[0]
        if not t:
            return True
        try:
            self.db.drop_tables(table_name)
        except:
            return False
        return True

    def run(self):
        self.main.runFlag = True

        self.ishistory()
        if self.main.ishistory:
            self.main.runFlag = False
            return
        try:
            self.mutex.lock()
            self.signalText.emit("登陆中，请稍后。。。。")
            ok = "0"
            loguru.logger.info(self.url)
            loguru.logger.info(self.cookies)
            self.driver = setDriver(self.url, self.cookies)

            try:
                if self.login():
                    ok = "1"
                else:
                    ok = "0"
            except Exception as e:
                ok = f"错误: {e}"
            self.signal.emit(ok)
            if ok != "1":
                return
            if self.deleteHistory():
                self.signalText.emit("清空上一次 相同搜索数据 成功。。。")
            else:
                self.signalText.emit("清空上一次 相同搜索数据 失败，详情查看 运行日志。。")
            self.signalText.emit("开始搜索，请稍后。。。。")
            from modules import M

            M.cookies.insert(self, self.cookies, self.table_)
            data = self.Init()

            M.history.insert(self, self.code, data['numCode']['Num'], self.table_)
            M.search.insert(self, data['cityUrls'])
            Num = self.getNum()

            self.signalBar.emit(0, int(Num), 1)
            self.driver.quit()
            M.url.create(self)
            countrys = ""
            for country, value in data['cityUrls'].items():
                countrys += country + ','
            country = countrys.rstrip(",")
            if os.path.exists(self.config['outputPath']):
                os.remove(self.config['outputPath'])
            self.signalText.emit(f"初始化成功 本次搜索一共：{data['numCode']['Num']} \n 涉及国家: {country}")
            # Num = data['numCode']['Num']
            successNum = 0
            # if Num <= 50:
            #     page = Num / 10
            #     url = urljoin(self.url, f"/result?qbase64={enBase64code(self.code)}")
            #     successNum = self.singleThread(url, self.getCookies(), self.headers, self.config['size'], self.config['page'],
            #                       self.config['outputPath'], self.config['outputType'], self.config['timeout'],successNum)
            # else:
            for country, value in data['cityUrls'].items():
                for city, info in value.items():
                    # 线程锁on
                    if city == 'Unknown':
                        if self.main.ui.checkBox_unknown.isChecked():
                            continue
                        info['href'] = UnknownCity(info['href'], country)
                    text = f"{country} - {city} : {info['href']}"
                    self.signalText.emit(text)
                    url = self.url + info['href']
                    num = info['Num']
                    page = self.get_page(num=num)
                    if page == 0:
                        continue
                    successNum = self.singleThread(url, self.getCookies(), self.headers, self.size, page,
                                                self.config['outputPath'],
                                                self.config['outputType'],
                                                self.config['timeout'],successNum)
                    if self.isCancel:
                        self.signalText.emit("任务取消。。。")
                        self.final()
                        return
            self.final()
        except Exception as e:
            self.signalError.emit(str(e))
            loguru.logger.error(e)
            self.signalText.emit("任务取消。。。")
            self.main.runFlag = False
            self.mutex.unlock()
            self.signalText.emit("closeThread")

    def singleThread(self, url, cookies, header, size, page, filename, OutputType, timeout,successNum):
        urlList = [url + f"&page={pa + 1}&page_size={size}" for pa in range(int(page))]
        for url in urlList:
            if self.isPause:
                self.cond.wait(self.mutex)
            if self.isCancel:
                return 0
            if timeout > 0:
                loguru.logger.info(f"等待请求 {timeout}s。。。。")
                time.sleep(timeout)
            result = getRequestsSoup(url, cookies, header)
            if not result:
                continue
            b = getInfo(soup=result, filename=filename, OutputType=OutputType)
            if not b:
                continue
            from modules import M
            M.url.insert(self, b)
            # print(num)
            successNum = successNum + len(b)
            self.signalBar.emit(successNum, 0, 0)

            if self.isCancel:
                self.signalText.emit("任务取消。。。")
                self.final()

        return successNum

    def login(self):
        userinfo = {}
        url = self.url + "/personalData"
        from .util import getDriverSoup
        try:
            soup = getDriverSoup(url=url, sign=True, value="apikeyconeye", driver=self.driver)
        except Exception as e:
            raise Exception("cookies 错误")
        tags = soup.find_all(name="div", attrs={"class": "personList"})
        apiTag = soup.find(name="span", attrs={"class": "apikeynumber"})
        if tags is None:
            raise Exception("不存在personList")
        if apiTag is None:
            raise Exception("不存在apikeynumber")
        try:
            userinfo['username'] = tags[1].contents[2].string
            userinfo['useremail'] = tags[2].contents[2].string
            userinfo['usergroup'] = tags[4].contents[2].string
            userinfo['userApikey'] = apiTag.string.strip()
            for key, value in userinfo.items():
                if value is None:
                    raise
        except Exception as e:
            userinfo = None
        finally:
            loguru.logger.success(userinfo)
            if userinfo is None:
                self.driver.close()
                return False
            self.userGroup = userinfo['usergroup']
            return True

    def Init(self):
        data = {
        }
        url = self.url + f"/result?qbase64={enBase64code(self.code)}"
        try:
            soup = getDriverSoup(url=url, sign=False, value="hsxa-list-main", driver=self.driver)
        except Exception as e:
            loguru.logger.error(str(e))
            raise

        numCode = NumCode(soup, self.code, tagString="hsxa-nav-font-size")
        print(numCode)
        relatedSearch = getRelatedSearch(soup, Strings={
            "relatedSearch": "relatedSearch",
            "searchSpanList": "searchSpanList",
        })
        print(relatedSearch)
        cityUrls = getCityUrls(soup, Strings = {
            "countryLi": "hsxa-country-li",
            "countryName": "hsxa-title-left",
            "cityTags": "hsxa-country-div-list",
            "cityName": "hsxa-table-label-left",
            "cityNum": "hsxa-table-label-right",
        })
        print(cityUrls)
        data['relatedSearch'] = relatedSearch
        data['numCode'] = numCode
        data['cityUrls'] = cityUrls
        return data

    def get_page(self, num):
        num = int(num)
        if num >= 10000:
            num = 10000
        if num == 0:
            return 0
        if 0 < num <= self.size:
            page = 1
        else:
            page = int(num / self.size)
        if (self.userGroup == "注册用户") & (page > 5):
            self.size = 10
            page = 5
        if page > self.Page and not self.flag:
            page = self.Page
        return page

    def getCookies(self):
        c = self.main.ui.lineEdit_cookies.text()
        if c is None: raise Exception("不存在Cookies")
        try:
            cookies = StringToDict(c, "; ")
        except Exception as e:
            raise Exception(e)
        return cookies

    def final(self):
        self.main.runFlag = False
        self.signalBar.emit(1, 1, 1)
        self.signalText.emit("搜索完成,请稍后")
        self.mutex.unlock()
        self.signalText.emit("closeThread")

    def ishistory(self):
        from modules import M
        d = M.history.searchTable_name(self, self.code)
        self.signalHistory.emit(d)
