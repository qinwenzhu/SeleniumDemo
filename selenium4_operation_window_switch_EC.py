# -*- coding:utf-8 -*-
# @Time: 2020/3/23 11:46
# @Author: wenqin_zhu
# @File: selenium4_operation_window_switch_EC.py
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

"""
方式二：切换window窗口，使用显性等待，等待新窗口出现切换到新窗口
"""

# 在新窗口出现之前，获取当前窗口句柄
wins = driver.window_handles

# 通过元素操作产生新的窗口
ulr_click = (By.XPATH, '//div[contains(@class, "c-container") and @id="2"]/h3/a')
wait.until(EC.visibility_of_element_located(ulr_click))
driver.find_element(*ulr_click).click()

# 等待新的窗口出现后进行窗口切换
wait.until(EC.new_window_is_opened(wins))


time.sleep(10)

driver.quit()
