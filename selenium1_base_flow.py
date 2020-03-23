# -*- coding:utf-8 -*-
# @Time: 2020/3/23 10:59
# @Author: wenqin_zhu
# @File: selenium1_base_flow.py
# @Software: PyCharm


from selenium import webdriver


driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.baidu.com/")

import time
time.sleep(2)

driver.refresh()

time.sleep(2)

driver.quit()
