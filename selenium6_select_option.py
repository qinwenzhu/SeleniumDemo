# -*- coding:utf-8 -*-
# @Time: 2020/3/30 12:51
# @Author: wenqin_zhu
# @File: selenium6_select_option.py
# @Software: PyCharm


from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

""" 针对select下拉列表，参考 Select 类"""
from selenium.webdriver.support.select import Select
import time

"""
正常的select下拉列表产生的下拉列表效果 - Select 类
其他标签通过样式仿制的下拉列表效果 - 采用鼠标辅助操作移动到下拉列表中并选择
"""

driver = webdriver.Chrome()
# driver.maximize_window()
wait = WebDriverWait(driver, 20)

driver.get("https://www.baidu.com/")

# 定位到需要鼠标操作的元素滑动操作
move_ele = driver.find_element_by_xpath('//div[@id="u1"]//a[@class="pf"]')
# 滑动到指定元素上面
ActionChains(driver).move_to_element(move_ele).perform()

click_taget_ele = driver.find_element_by_xpath('//a[@class="setpref"]')
# 滑动到指定元素上并点击指定元素    pause() 暂停操作    perform() 执行所有链式动作
ActionChains(driver).move_to_element(move_ele).pause(1).click(click_taget_ele).perform()


# 该页面存在select下拉列表，定位到指定的select标签
loc = (By.XPATH, '//select[@name="NR"]')
wait.until(EC.visibility_of_element_located(loc))
ele_select = driver.find_element(*loc)

# 实例化Select对象
sel = Select(ele_select)

# 获取select下 option 内容的几种方式

# 1、通过option所处的下标
sel.select_by_index(2)
# 强制等待查看每次选择后的效果
time.sleep(3)

# 2、通过可见文本
sel.select_by_visible_text("每页显示10条")
time.sleep(3)

# 3、通过option标签中的value值
sel.select_by_value("20")

time.sleep(10)

driver.quit()


