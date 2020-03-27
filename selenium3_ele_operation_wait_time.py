# -*- coding:utf-8 -*-
# @Time: 2020/3/23 11:12
# @Author: wenqin_zhu
# @File: selenium3_ele_operation_wait_time.py
# @Software: PyCharm


from selenium import webdriver

# 强制等待
import time


driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.baidu.com/")

# 强制等待2秒
time.sleep(2)
driver.find_element_by_id('kw').send_keys("百度搜索内容")

time.sleep(3)
driver.find_element_by_xpath('//input[@class="bg s_btn"]').click()


driver.quit()
