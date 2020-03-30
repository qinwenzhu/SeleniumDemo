# -*- coding:utf-8 -*-
# @Time: 2020/3/27 11:55
# @Author: wenqin_zhu
# @File: selenium4_alert_EC.py.py
# @Software: PyCharm


from selenium import webdriver

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time


""" alert 弹框
 浏览器中存在三种alert弹框
 了解 Alert 类
 常见的方法：
    accept()
    dismiss()
    text
    send_keys()
 """


driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 20)

driver.get(r"D:\wenqin\SeleniumDemo\prepare\alert.html")

# 点击测试的input1按钮 - 出现alert弹框 - 警告消息框
driver.find_element_by_id("btn1").click()

alert = wait.until(EC.alert_is_present())

time.sleep(2)
# 点击alert弹框的确定按钮，关闭弹框
alert.accept()

# 点击测试的input2按钮 - 出现alert弹框 - 确认消息框
driver.find_element_by_id("btn2").click()

alert = wait.until(EC.alert_is_present())

time.sleep(2)

# 点击alert弹框的确定按钮，关闭弹框
alert.dismiss()

# 点击测试的input3按钮 - 出现alert弹框 - 提示消息框
driver.find_element_by_id("btn3").click()

alert = wait.until(EC.alert_is_present())
# 获取alert弹框的文本
print(alert.text)


time.sleep(2)

alert.send_keys("alert文本框内容输入！")

alert.accept()


time.sleep(10)

driver.quit()
