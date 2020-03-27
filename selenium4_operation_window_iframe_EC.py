# -*- coding:utf-8 -*-
# @Time: 2020/3/27 10:44
# @Author: wenqin_zhu
# @File: selenium4_operation_window_iframe_EC.py.py
# @Software: PyCharm

from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time


driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 20)

driver.get("https://ke.qq.com/")

# 点击登录
click_login = (By.ID, 'js_login')
wait.until(EC.visibility_of_element_located(click_login))
driver.find_element(*click_login).click()

# 选择QQ登录
click_qq_login = (By.XPATH, '//a[contains(@class, "btns-enter-qq")]')
wait.until(EC.visibility_of_element_located(click_qq_login))
driver.find_element(*click_qq_login).click()

""" 因为选择QQ登录的点击，现在页面元素切换到iframe窗口 
切换iframe的方式：
通过 name  属性
通过 页面中iframe的下标
通过 元素定位 webElement

显性等待会新增一种切换到iframe的方式 - 传入定位元素，元组的方式 (By.NAME, 'login_frame_qq')
"""

# 定位iframe元素并等待iframe可用
WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.NAME, 'login_frame_qq')))


# 成功切换到iframe窗口 - 点击'帐号密码登录'
login_btn = (By.ID, 'switcher_plogin')
wait.until(EC.visibility_of_element_located(login_btn))
driver.find_element(*login_btn).click()


time.sleep(5)

driver.quit()

