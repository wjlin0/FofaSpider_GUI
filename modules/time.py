#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author   :wjlin0
# @Blog     :https://wjlin0.com
# @Email    :wjlgeren@163.com
# @Time     :2022-07-20 10:18
# @File     :time
import datetime


def now():
    return "[ "+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+" ]"
