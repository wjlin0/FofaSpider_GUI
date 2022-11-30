#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author   :wjlin0
# @Blog     :https://wjlin0.com
# @Email    :wjlgeren@163.com
# @Time     :2022-07-15 12:58
# @File     :M
import re
import time
from urllib.parse import urljoin

import loguru

from datetime import datetime, timedelta

from modules.C import fofaSpider


class cookies(fofaSpider):

    def insert(self, cookie, table_):
        self.table_name = 'cookies'
        startTime = time.time()
        endTime = (datetime.fromtimestamp(startTime) + timedelta(days=0.5)).timestamp()
        d = {
            "startTime": startTime,
            "endTime": endTime,
            'cookies': cookie,
            'table_name': table_,
        }
        data = self.db.queryData("select * from " + self.table_name)
        if data is None or data == []:
            self.db.insert_data(self.table_name, d)
        else:
            self.db.update_field(self.table_name, d, data[0])
        return True


class history(fofaSpider):
    def searchTable_name(self, code):

        return self.db.queryData(f"select table_name from history where code=:codes", {
            "codes": code,
        })
        # return self.db.query_data(f"select table_name from history where code=\"{code}\"")

    def searchTables(self):
        return self.db.query_data_all("select code from history")

    def insert(self, code, num, table_name):
        self.table_name = 'history'
        # code = re.escape(code)
        table_name = table_name
        startTime = time.time()
        data = {
            'code': code,
            'table_name': table_name,
            'startTime': startTime,
            'progress': "",
            "num": num
        }
        try:
            sql = 'SELECT * FROM history where CODE=:codes;'
            # c = self.db.query_data(sql)
            c = self.db.queryData(sql, {
                "codes": code
            })
            if c:
                ID = c[0]
                self.db.update_field(self.table_name, data, ID)
            else:
                self.db.insert_data(self.table_name, data)
        except Exception as e:
            loguru.logger.error(e)
            return False
        return True


class search(fofaSpider):
    def insert(self, cityInfo: dict):
        self.table_name = 'search'
        self.db.cursor.execute(f"DELETE FROM {self.table_name};")
        self.db.cursor.execute(f"DELETE FROM sqlite_sequence WHERE name = '{self.table_name}';")
        for country, value in cityInfo.items():
            for city, info in value.items():
                d = {
                    'country': country,
                    'city': city,
                    'url': urljoin(self.url, info['href']),
                    'num': info['Num'],
                }
                self.db.insert_data(self.table_name, d)


class config(fofaSpider):
    def getConfig(self):
        c = self.db.queryData("select * from config")
        if c[1] == 'False' or c[1] == '0' or c[1]=="none" or c[1]=="false" or  c[1] == 'None' or c[1] == '':
            flag = False
        else:
            flag = True
        r = {
            'flag': flag,
            'page': int(c[2]),
            'size': int(c[3]),
            'worker': int(c[4]),
            'timeout': float(c[5]),
            'outputType': c[6],
            'outputPath': c[7],
        }
        return r


class url(fofaSpider):
    def insert(self, infoList):
        for info in infoList:
            self.db.insert_data(self.table_, info)

    def create(self):
        field_list = [
            'ID INTEGER PRIMARY KEY autoincrement', 'url TEXT NOT NULL', 'port TEXT NOT NULL',
            'title TEXT NOT NULL', 'host', 'addr', 'server', 'code'
        ]
        self.db.create_tables(self.table_, field_list)
