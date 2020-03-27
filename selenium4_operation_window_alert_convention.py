# -*- coding:utf-8 -*-
# @Time: 2020/3/27 11:55
# @Author: wenqin_zhu
# @File: selenium4_operation_window_alert_convention.py
# @Software: PyCharm


from selenium import webdriver

import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get(r"D:\wenqin\SeleniumDemo\prepare\alert.html")

# 点击测试的input按钮 - 出现alert弹框
driver.find_element_by_id("btn1").click()
# 当出现alert弹框的时候，切换到alert弹框上进行操作   - 具体用法参考 Alert 类
alert = driver.switch_to.alert
time.sleep(2)
# 点击alert弹框的确定按钮，关闭弹框
alert.accept()

# 点击测试的input按钮 - 出现alert弹框
driver.find_element_by_id("btn2").click()
# 当出现alert弹框的时候，切换到alert弹框上进行操作   - 具体用法参考 Alert 类
alert = driver.switch_to.alert
time.sleep(2)
# 点击alert弹框的确定按钮，关闭弹框
alert.dismiss()

# 点击测试的input按钮 - 出现alert弹框
driver.find_element_by_id("btn3").click()
# 当出现alert弹框的时候，切换到alert弹框上进行操作   - 具体用法参考 Alert 类
alert = driver.switch_to.alert
time.sleep(2)
# 点击alert弹框的确定按钮，关闭弹框
alert.send_keys("confirm")


time.sleep(10)

driver.quit()
