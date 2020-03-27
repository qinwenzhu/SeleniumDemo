# -*- coding:utf-8 -*-
# @Time: 2020/3/23 11:46
# @Author: wenqin_zhu
# @File: selenium4_operation_window_switch_convention.py
# @Software: PyCharm

from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time


driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 20)

driver.get("https://www.baidu.com/")

# 文本框输入内容
input_loc = (By.ID, 'kw')
wait.until(EC.visibility_of_element_located(input_loc))
driver.find_element(*input_loc).send_keys("selenium窗口切换")

# 点击搜索
button_loc = (By.XPATH, '//input[@class="bg s_btn"]')
wait.until(EC.visibility_of_element_located(button_loc))
driver.find_element(*button_loc).click()

ulr_click = (By.XPATH, '//div[contains(@class, "c-container") and @id="2"]/h3/a')
wait.until(EC.visibility_of_element_located(ulr_click))
driver.find_element(*ulr_click).click()

"""
方式一：切换window窗口
"""
# 在点击搜索操作产生新窗口时，获取窗口的总句柄数
wins = driver.window_handles
print(wins)

# 可以通过打印当前窗口句柄，来查看当前页面所在的窗口
print(driver.current_window_handle)

# 进行窗口切换
# driver.switch_to_window(wins[-1])
# 通过列表获取最后一个新打开的窗口为：win[-1]
driver.switch_to.window(wins[-1])

time.sleep(3)
# 将窗口切换回去
driver.switch_to.window(wins[0])


time.sleep(10)

driver.quit()
