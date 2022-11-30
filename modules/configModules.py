#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author   :wjlin0
# @Blog     :https://wjlin0.com
# @Email    :wjlgeren@163.com
# @Time     :2022-07-14 14:07
# @File     :configModules
import os

from main import MainWindow


class config(MainWindow):
    def Json(self):
        self.config['outputType'] = 'json'
        self.config['outputPath'] = os.path.abspath("output/url.json")
        self.db.update_field("config", self.config, 1)
        self.configShow()

    def Csv(self):
        self.config['outputType'] = 'csv'
        self.config['outputPath'] = os.path.abspath("output/url.csv")
        self.db.update_field("config", self.config, 1)
        self.configShow()

    def Txt(self):
        self.config['outputType'] = 'txt'
        self.config['outputPath'] = os.path.abspath("output/url.txt")
        self.db.update_field("config", self.config, 1)
        self.configShow()

    def Timeout(self):
        self.config['timeout'] = 1.2
        self.config['worker'] = 0
        self.db.update_field("config", self.config, 1)
        self.configShow()
