# -*- coding:utf-8 -*-
# @Time: 2020/3/23 11:12
# @Author: wenqin_zhu
# @File: selenium3_ele_operation_wait2_implicitly.py
# @Software: PyCharm


from selenium import webdriver

# 智能等待 - 隐性等待


driver = webdriver.Chrome()

# 隐性等待，之后在开启会话的时候被调用一次，设置等待时长的上限为20
driver.implicitly_wait(20)

driver.maximize_window()
driver.get("https://www.baidu.com/")

driver.find_element_by_id('kw').send_keys("百度搜索内容")
driver.find_element_by_xpath('//input[@class="bg s_btn"]').click()

driver.quit()
