#倒入webdriver，使用浏览器驱动
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#将chromeder设置为无头浏览器(没有浏览器界面)
chromeOption = webdriver.ChromeOptions
chromeOption.set_headless()
browse = webdriver.Chrome(executable_path='/Users/ljh/Desktop/chromedriver',options=chromeOption)

#有浏览器的界面
browse = webdriver.Chrome(executable_path='/Users/ljh/Desktop/chromedriver')
#模拟浏览器发起一个请求
browse.get('https://www.baidu.com')
#获取的是浏览器渲染之后的页面
print(browse.page_source)

#如何模拟用户输入
browse.find_element_by_id('kw').send_keys('美女')
#模拟用户点击按钮
browse.find_element_by_id('su').click()
time.sleep(5)
# #模拟点击下一页
# # browse.find_elements_by_class_name('n')[0].click()
browse.find_element_by_class_name('n').click()
time.sleep(5)

#点击更多
browse.find_element_by_xpath('//div[@class="s_tab"]/a[last()]').click()

#模拟前进
# browse.forward()
#模拟后退
browse.back()
# 关闭当前 Closes the current window.
browse.close()
#退出，关闭所有
# browse.quit()


