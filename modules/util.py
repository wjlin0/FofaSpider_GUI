#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author   :wjlin0
# @Blog     :https://wjlin0.com
# @Email    :wjlgeren@163.com
# @Time     :2022-07-15 14:45
# @File     :util
import base64
import csv
import json
import os
import re
import shutil
import threading
import time
import warnings
from urllib import parse
from urllib.parse import unquote

import bs4
import loguru
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


def rmTree(path):
    shutil.rmtree(path)


class driver:
    instance = None
    lock = threading.RLock()
    driverInstall = "."
    arguments = ['--disable-dev-shm-usage', '–ignore-certificate-errors', '--ignore-ssl-errors',
                 'headless',
                 '--no-sandbox']
    chrome_options = None
    driver_ = None

    def getDriver(self):
        driverPath = ""
        try:
            for fpathe, dirs, fs in os.walk(self.driverInstall):
                for f in fs:
                    if 'chromedriver' in os.path.join(fpathe, f):
                        driverPath = os.path.join(fpathe, f)
                        break
            return webdriver.Chrome(executable_path=os.path.abspath(driverPath),
                                    chrome_options=self.chrome_options)
        except:
            try:
                rmTree(self.driverInstall)  # 清空目录
            except:
                raise
            os.mkdir(self.driverInstall)
            return webdriver.Chrome(executable_path=ChromeDriverManager(path=self.driverInstall).install(),
                                    chrome_options=self.chrome_options)

    def getChromeOptions(self):
        chrome_options = Options()
        # for argument in self.arguments:
        #     chrome_options.add_argument(argument)
        chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
        self.chrome_options = chrome_options

    def __init__(self):

        self.driverInstall = "."
        self.arguments = ['--disable-dev-shm-usage', '–ignore-certificate-errors', '--ignore-ssl-errors',
                          'headless',
                          '--no-sandbox']
        self.chrome_options = None
        self.driver_ = None
        warnings.filterwarnings("ignore", category=DeprecationWarning)
        self.driverInstall = "./drivers/"
        if not os.path.exists(self.driverInstall):
            os.mkdir(self.driverInstall)
        self.getChromeOptions()
        self.driver_ = self.getDriver()

    def get(self, url: str):

        return self.driver_.get(url)

    def getDriverClass(self, by: By, value: str, timeout=15):
        WebDriverWait(driver=self.driver_, timeout=timeout).until(
            expected_conditions.presence_of_element_located((by, value)))

    def cookies(self, cookies, url):

        self.get(url)
        self.driver_.delete_all_cookies()
        if type(cookies) == str:
            cookies = cookies.split('; ')
            cookies_dict = {}
            for c in cookies:
                if c == '':
                    break
                cookies_dict[c.split('=')[0]] = c.split('=')[-1]
        elif type(cookies) == dict:
            cookies_dict = cookies
        else:
            raise
        for key, value in cookies_dict.items():
            cookie = dict(name=key, value=value)
            self.driver_.add_cookie(cookie)
        self.refresh()

    def refresh(self):
        return self.driver_.refresh()

    def execute_script(self, js):
        return self.driver_.execute_script(js)

    def find_element(self, by, value):

        return self.driver_.find_element(by=by, value=value)

    def html_text(self) -> str:

        text = self.driver_.page_source
        return text

    def close(self):
        return self.driver_.close()

    def quit(self):
        return self.driver_.quit()


def getDriverSoup(url, sign, value, driver):
    driver.get(url=url)
    if 'Retry later' in driver.html_text():
        raise Exception("Retry later")
    if '查询语法错误' in driver.html_text():
        raise Exception("查询语句出错")
    if '仅限高级会员及以上使用' in driver.html_text():
        raise Exception("仅限高级会员及以上使用")
    if not sign:
        try:
            driver.getDriverClass(by=By.CLASS_NAME, value=value, timeout=30)
        except:
            raise Exception("搜索失败，搜索结果为0 请检查 网络原因 或 更换搜索语句 或 次数限制")
    else:
        # driver.find_element(by=By.CLASS_NAME, value="apikeyconeye").click()
        try:
            driver.find_element(by=By.CLASS_NAME, value=value).click()
        except Exception as e:
            print(e)
            raise

    html = driver.html_text()
    return bs4.BeautifulSoup(html, "html.parser")


def enBase64code(str_):
    return parse.quote(str(base64.b64encode(str_.encode("utf-8")), "utf-8"))


def deBase64code(str_):
    return parse.quote(str(base64.b64decode(parse.unquote(str_, "utf-8")), "utf-8"))


def StringToDict(str_: str, reg: str = "; "):
    dictStr = str_.split(reg)
    D = {}
    for c in dictStr:
        D[c.split('=')[0]] = c.split('=')[-1]
    return D


def getRequestsSoup(url, cookies, headers, waitTime=20):
    try:
        html = requests.get(url=url, headers=headers,
                            cookies=cookies, timeout=20)
        if 'Retry later' in html.text:
            raise Exception("请求繁忙 - （若此语句频繁出现可选择调低线程）")
        if html.status_code != 200:
            raise Exception("请求繁忙 - （若此语句频繁出现可选择调低线程）")
        return bs4.BeautifulSoup(html.content, "html.parser")
    except Exception as e:
        loguru.logger.warning(e)
        return False


def NumCode(soup: bs4.BeautifulSoup, code, tagString="hsxa-nav-font-size"):
    info = {}
    tag = soup.find(name="p", attrs={"class": tagString})
    if tag is None:
        raise Exception("不存在Num Code Tag")
    num = tag.find_all(name="span")[0].string
    # num = tag.find_all(name="span")[1].span.string
    if num is None:
        raise Exception("这次查询不存在目标")
    else:
        num = int(str(num).replace(',', ''))
    info['Num'] = num
    info['code'] = code
    return info


def getCityUrls(soup: bs4.BeautifulSoup, Strings=None):
    if Strings is None:
        Strings = {
            "countryLi": "hsxa-country-li",
            "countryName": "hsxa-title-left",
            "cityTags": "hsxa-country-div-list",
            "cityName": "hsxa-table-label-left",
            "cityNum": "hsxa-table-label-right",
        }
    Cityurls = {}
    try:
        countryLi = soup.find_all(name="li", attrs={"class": Strings['countryLi']})
        for tag in countryLi:
            temp = {}
            countryName = tag.find(name="div", attrs={"class": Strings['countryName']}).a.string
            countryName = str(countryName).encode("utf-8").decode("utf-8").strip()

            cityTags = tag.find_all(name="div", attrs={"class": Strings['cityTags']})
            for city in cityTags:
                tempCity = {}
                cityName = city.find(name="div", attrs={"class": Strings['cityName']}).a.string
                cityName = str(cityName).strip()
                cityNum = city.find(name="div", attrs={"class": Strings['cityNum']}).span.string
                cityNum = str(cityNum).encode("utf-8").decode("utf-8").replace(',', '')
                tempCity['href'] = city.find(name="div", attrs={"class": Strings["cityName"]}).a['href'].encode(
                    "utf-8").decode("utf-8")
                tempCity['Num'] = int(cityNum)
                temp[cityName] = tempCity

            Cityurls[countryName] = temp

    except Exception as e:
        loguru.logger.error(e)
        raise Exception("不存在城市信息")
    return Cityurls


def getRelatedSearch(soup: bs4.BeautifulSoup, Strings: dict = None):
    relatedSearch = dict()
    if Strings is None:
        Strings = {
            "relatedSearch": "relatedSearch",
            "searchSpanList": "searchSpanList",
        }
    tag = soup.find(name="div", attrs={"class": Strings['relatedSearch'], })
    if tag is None:
        raise Exception("不存在相关搜索的tag")
    searchSpanList = tag.find_all(name="a", attrs={"class": Strings['searchSpanList']})
    if searchSpanList is None:
        raise searchSpanList
    try:
        for search in searchSpanList:
            relatedSearch[search.string] = search['href']
    except:
        raise Exception("提取相关搜索时，出现错误")
    return relatedSearch


def getInfoDict(infoList: bs4.BeautifulSoup, Strings):
    infoList = infoList.children
    infoDict = list()
    for info in infoList:
        url = ""
        title = ""
        host = ""
        addr = ""
        port = ""
        server = ""
        code = ""
        if info is None:
            continue
        urlTag = info.find(name="div", attrs={"class": Strings["url"][0]})
        if urlTag is not None:
            urlTag = urlTag.find(name="span", attrs={"class": Strings["url"][1]})
        if urlTag is not None:
            urlTag = urlTag.a
        if urlTag is not None:
            url = urlTag['href']
        portTag = info.find("div", attrs={"class": Strings["port"][0]})
        if portTag is not None:
            portTag = portTag.find(name="a", attrs={"class": Strings["port"][1]})
        if portTag is not None:
            port = portTag.string

        title_host_addrTag = info.find("div", attrs={"class": Strings["title"][0]})
        if title_host_addrTag is not None:
            title_host_addrTag = title_host_addrTag.find_all(name="p")
        if title_host_addrTag is not None:
            title = str(title_host_addrTag[0].string)
            host = str(title_host_addrTag[1].a.string)
            addrTag = title_host_addrTag[2].find_all(name="a", attrs={"class": Strings["addr"][0]})
            if addrTag is not None:
                for a in addrTag:
                    if a is None:
                        continue
                    s = a.string
                    if s is None:
                        s = ""
                    addr = addr + "/" + s
                addr = addr.lstrip("/")
        tag = info.find("div", attrs={"class": Strings["serverTag"][0]})
        if tag is not None:
            tag1 = tag.find("div", attrs={"class": Strings["serverTag"][1]})
            if tag1 is not None:
                t = tag1.span.string
                server = "".join(re.findall(r"\nServer:(.*?)\n", t))
                code = "".join(re.findall(r"HTTP/.{3} (.{3}?) .{2}", t))
        if url.replace(",", " ").strip() != "" or url:
            tmp = {
                "url": url,
                "port": port,
                "title": title,
                "host": host,
                "addr": addr,
                "server": server,
                "code": code,
            }
            for key, value in tmp.items():
                if value == 'None':
                    value = ''
                value = value.replace("=", "").replace("-", "_").strip()
                tmp[key] = value
                # print(f"{key}:{value}")
            infoDict.append(tmp)

    return infoDict


def getInfo(soup: bs4.BeautifulSoup, filename, OutputType, Strings=None):
    n = 0
    if soup is None:
        return 0
    if Strings is None:
        Strings = {
            'infoTag': 'el-checkbox-group',
            "url": ["hsxa-fl hsxa-meta-data-list-lv1-lf", "hsxa-host"],
            "title": ["hsxa-meta-data-list-main-left"],
            "host": ["hsxa-jump-a"],
            "addr": ["hsxa-jump-a"],
            "port": ["hsxa-fr", "hsxa-port"],
            "serverTag": ["hsxa-body-content", "el-scrollbar__view"]
        }
    infoList = soup.find(name="div", attrs={"class": Strings['infoTag']})
    try:
        if infoList is None:
            raise Exception("不存在IP的tag")
    except Exception as e:
        loguru.logger.error(e)
        return 0

    info = getInfoDict(infoList, Strings)
    if not os.path.exists(os.path.dirname(filename)):
        os.makedirs(os.path.dirname(filename))

    if OutputType == "csv":
        csvSave(info, filename)
    elif OutputType == "json":
        jsonSave(info, filename)
    elif OutputType == "txt":
        outputSave(info, filename)
    else:
        raise Exception("不存在输出格式")
    return info


def csvSave(info, filename):
    headers = ["url", "port", "title", "host", "addr", "server", "code"]
    # print(info)
    with open(filename, 'a+', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=headers)  # 提前预览列名，当下面代码写入数据时，会将其一一对应。
        if not os.path.getsize(filename):
            writer.writeheader()  # 写入列名
        writer.writerows(info)  # 写入数据


json_num = 0
json_info = {}


def jsonSave(info, filename):
    global json_num
    for i in info:
        json_info[f'{json_num}'] = i
        json_num += 1
        with open(filename, "w", encoding="utf-8")as f:
            json.dump(json_info, f, indent=4, ensure_ascii=False)


def outputSave(info, filename):
    url = list()

    for i in info:
        if i['url'] not in url:
            url.append(i['url'] + "\n")
    with open(filename, 'a+', newline='', encoding='utf-8') as f:
        f.writelines(url)


def UnknownCity(href, value):
    code = "".join(re.findall(r"qbase64=(.*)$", href))
    code = deBase64code(code)
    code = unquote(code, 'utf-8')
    c = {
        'hk': '中国香港特别行政区', 'cn': '中国', 'af': '阿富汗', 'al': '阿尔巴尼亚', 'dz': '阿尔及利亚', 'us': '美国', 'ad': '安道尔', 'ao': '安哥拉',
        'ag': '安提瓜和巴布达', 'ae': '阿联酋', 'ar': '阿根廷', 'am': '亚美尼亚', 'au': '澳大利亚', 'at': '奥地利', 'az': '阿塞拜疆', 'bs': '巴哈马',
        'bh': '巴林', 'bd': '孟加拉', 'bb': '巴巴多斯', 'by': '白俄罗斯', 'be': '比利时', 'bz': '伯利兹', 'bj': '贝宁', 'bt': '不丹',
        'bo': '玻利维亚', 'ba': '波斯尼亚', 'bw': '博茨瓦纳', 'br': '巴西', 'bn': '文莱', 'bg': '保加利亚', 'bf': '布基纳法索', 'bi': '布隆迪',
        'kh': '柬埔寨', 'cm': '喀麦隆', 'ca': '加拿大', 'cf': '中非', 'td': '乍得', 'cl': '智利', 'co': '哥伦比亚', 'km': '科摩罗',
        'cd': '刚果布',
        'cg': '刚果金', 'cr': '哥斯达黎加', 'ci': '科特迪瓦', 'hr': '克罗地亚', 'cy': '塞浦路斯', 'cz': '捷克', 'dk': '丹麦', 'dj': '吉布提',
        'dm': '多米尼克', 'do': '多米尼加', 'ec': '厄瓜多尔', 'eg': '埃及', 'sv': '萨尔瓦多', 'gb': '英国', 'gq': '赤道几内亚',
        'er': '厄立特里亚',
        'ee': '爱沙尼亚', 'et': '埃塞俄比亚', 'fj': '斐济', 'fi': '芬兰', 'fr': '法国', 'ga': '加蓬', 'gm': '冈比亚', 'ge': '格鲁吉亚',
        'de': '德国',
        'gh': '加纳', 'gr': '希腊', 'gd': '格林纳达', 'gt': '危地马拉', 'cu': '古巴', 'gn': '几内亚', 'gw': '几内亚比绍', 'gy': '圭亚那',
        'ht': '海地', 'nl': '荷兰', 'hn': '洪都拉斯', 'hu': '匈牙利', 'is': '冰岛', 'in': '印度', 'id': '印尼', 'ir': '伊朗',
        'iq': '伊拉克',
        'ie': '爱尔兰', 'il': '以色列', 'it': '意大利', 'jm': '牙买加', 'jp': '日本', 'jo': '约旦', 'kz': '哈萨克斯坦', 'ke': '肯尼亚',
        'kg': '吉尔吉斯', 'ki': '基里巴斯', 'kr': '韩国', 'kw': '科威特', 'la': '老挝', 'lv': '拉脱维亚', 'lb': '黎巴嫩', 'ls': '莱索托',
        'lr': '利比里亚', 'ly': '利比亚', 'li': '列支敦士登', 'lt': '立陶宛', 'lu': '卢森堡', 'mk': '马其顿', 'mg': '马达加斯加',
        'mw': '马拉维',
        'my': '马来西亚', 'mv': '马尔代夫', 'ml': '马里', 'mt': '马耳他', 'mh': '马绍尔群岛', 'mr': '毛里塔尼亚', 'mu': '毛里求斯',
        'mx': '墨西哥',
        'fm': '密克罗尼西亚', 'md': '摩尔多瓦', 'mc': '摩纳哥', 'mn': '蒙古', 'me': '黑山共和国', 'ma': '摩洛哥', 'mz': '莫桑比克',
        'mm': '缅甸',
        'na': '纳米比亚', 'nr': '瑙鲁', 'np': '尼泊尔', 'nz': '新西兰', 'ni': '尼加拉瓜', 'ne': '尼日尔', 'ng': '尼日利亚', 'kp': '朝鲜',
        'no': '挪威', 'om': '阿曼', 'pk': '巴基斯坦', 'pw': '帕劳', 'ps': '巴勒斯坦', 'pa': '巴拿马', 'pg': '新几内亚', 'py': '巴拉圭',
        'pe': '秘鲁',
        'ph': '菲律宾', 'pl': '波兰', 'pt': '葡萄牙', 'qa': '卡塔尔', 'ro': '罗马尼亚', 'ru': '俄罗斯', 'rw': '卢旺达', 'kn': '圣基茨和尼维斯',
        'vc': '圣文森特和格林纳丁斯', 'lc': '圣卢西亚', 'ws': '萨摩亚', 'sm': '圣马力诺', 'st': '圣多美和普林西比', 'sa': '沙特', 'sn': '塞内加尔',
        'rs': '塞尔维亚', 'sc': '塞舌尔', 'sl': '塞拉利昂', 'sg': '新加坡', 'sk': '斯洛伐克', 'si': '斯洛文尼亚', 'sb': '所罗门群岛',
        'so': '索马里',
        'ss': '南苏丹', 'za': '南非', 'es': '西班牙', 'lk': '斯里兰卡', 'sd': '苏丹', 'sr': '苏里南', 'sz': '斯威士兰', 'se': '瑞典',
        'ch': '瑞士',
        'sy': '叙利亚', 'tj': '塔吉克斯坦', 'tz': '坦桑尼亚', 'th': '泰国', 'tl': '东帝汶', 'tg': '多哥', 'to': '汤加',
        'tt': '特立尼达和多巴哥',
        'tn': '突尼斯', 'tr': '土耳其', 'tm': '土库曼斯坦', 'tv': '图瓦卢', 'ug': '乌干达', 'ua': '乌克兰', 'uy': '乌拉圭',
        'uz': '乌兹别克斯坦',
        'vu': '瓦努阿图', 've': '委内瑞拉', 'cv': '佛得角', 'vn': '越南', 'ye': '也门', 'zm': '赞比亚', 'zw': '津巴布韦', 'tw': '台湾',
        'va': '梵蒂冈'}
    for cb, name in c.items():
        if name == value:
            code = code + f" && country=\"{cb.upper()}\""
            break
    return "/result?qbase64=" + enBase64code(code)
