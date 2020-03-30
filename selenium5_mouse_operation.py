# -*- coding:utf-8 -*-
# @Time: 2020/3/27 19:30
# @Author: wenqin_zhu
# @File: selenium5_mouse_operation.py
# @Software: PyCharm


from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
""" 鼠标操作   
常见的鼠标操作   详细了解  ActionChains 类"""
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 20)

driver.get("https://www.baidu.com/")

# 定位到需要鼠标操作的元素滑动操作
move_ele = driver.find_element_by_xpath('//div[@id="u1"]//a[@class="pf"]')
# 滑动到指定元素上面
ActionChains(driver).move_to_element(move_ele).perform()

click_taget_ele = driver.find_element_by_xpath('//a[@class="setpref"]')
# 滑动到指定元素上并点击指定元素    pause() 暂停操作    perform() 执行所有链式动作
ActionChains(driver).move_to_element(move_ele).pause(1).click(click_taget_ele).perform()

time.sleep(10)

driver.quit()

