# FofaSpider
FofaSpider 是基于Python3.7,pyside6,pyDracula,selenium无头浏览器 开发而成的爬虫GUI脚本。针对 fofa 提取关键信息

# 免责声明

由于传播、利用此工具所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责。本工具仅限学习爬虫开发使用

# 安装

```bash
git clone https://github.com/wjlin0/FofaSpider_GUI.git
cd FofaSpider_GUI
python -m pip install -r requirements.txt
```
# 使用

```text
python main.py
GUI 启动就会
```

# 打包命令

```
pyinstaller -F -w -i icon.ico main.py
```

# 弹出浏览器解决方式

modules -> util -> 66,67 打开注释就可以了

# 环境

windows 、linux（desktop）都可以用

# 功能

**1.支持csv导出**

**2.支持json格式导出**

**3.支持调整每个城市爬取的最大页数**

**4.fofa原生查询语句**

**5.支持导出最后一次查询历史记录**

**6.支持历史查询导出**


