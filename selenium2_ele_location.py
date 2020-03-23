# -*- coding:utf-8 -*-
# @Time: 2020/3/23 11:02
# @Author: wenqin_zhu
# @File: selenium2_ele_location.py
# @Software: PyCharm

from selenium import webdriver


driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.baidu.com/")

driver.find_element_by_id('')
driver.find_element_by_name('')
driver.find_element_by_tag_name('')
driver.find_element_by_class_name('')
driver.find_element_by_link_text('')
driver.find_element_by_partial_link_text('')
driver.find_element_by_xpath('')
driver.find_element_by_css_selector('')


driver.quit()
