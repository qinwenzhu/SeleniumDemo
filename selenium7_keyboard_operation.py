# -*- coding:utf-8 -*-
# @Time: 2020/3/30 13:27
# @Author: wenqin_zhu
# @File: selenium7_keyboard_operation.py
# @Software: PyCharm


from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 导入键盘类 Keys
from selenium.webdriver.common.keys import Keys

import time


driver = webdriver.Chrome()
wait = WebDriverWait(driver, 20)
driver.get("https://www.baidu.com/")

input_loc = (By.ID, 'kw')
wait.until(EC.visibility_of_element_located(input_loc))
# driver.find_element(*input_loc).send_keys("百度搜索内容")

# 使用键盘enter键，代替鼠标点击   -   使用前提是：该元素绑定了键盘操作快捷键
# send_keys()可以同时传递多个参数
driver.find_element(*input_loc).send_keys("selenium窗口切换", Keys.ENTER)


#  操作百度搜索内容，配合键盘的回车键使用
# button_loc = (By.XPATH, '//input[@class="bg s_btn"]')
# wait.until(EC.visibility_of_element_located(button_loc))
# driver.find_element(*button_loc).click()


time.sleep(10)
driver.quit()
