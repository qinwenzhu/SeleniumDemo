# -*- coding:utf-8 -*-
# @Time: 2020/3/23 11:12
# @Author: wenqin_zhu
# @File: selenium3_ele_operation_wait_integrated_application.py
# @Software: PyCharm


"""
实际工作中可以进行三种等待方式的灵活运用
    time.sleep()

    driver.implicitly_wait()

    等待元素的条件<可见/可用/可操作……>
"""


from selenium import webdriver

# 智能等待 - 显性等待
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time


driver = webdriver.Chrome()

# 智能等待 - 隐性等待
driver.implicitly_wait(20)

driver.maximize_window()
wait = WebDriverWait(driver, 20)

driver.get("https://www.baidu.com/")

input_loc = (By.ID, 'kw')
wait.until(EC.visibility_of_element_located(input_loc))
driver.find_element(*input_loc).send_keys("百度搜索内容")

button_loc = (By.XPATH, '//input[@class="bg s_btn"]')
wait.until(EC.visibility_of_element_located(button_loc))
driver.find_element(*button_loc).click()

# 强制等待
time.sleep(2)


driver.quit()

