#导入外部驱动
from selenium import webdriver
import time
#from selenium.webdriver.common.keys import keys
browse = webdriver.Chrome(executable_path='/home/bc/下载/chromedriver')
#模拟浏览器发起一个请求
#browse.get('https://www.baidu.com/')
browse.get('https://www.091ee.com/')
browse.find_element_by_id('img01').click()
time.sleep(5)
browse.find_element_by_xpath('//ul[@calss="menu mt5"]/li[2]')
#获取是浏览器渲染之后的页面
# print(browse.page_source)
# #如何输入模拟
# browse.find_element_by_id('kw').send_keys('美女')
# browse.find_element_by_id('su').click()
# time.sleep(5)
# browse.find_element_by_class_name('n').click()
# time.sleep(5)
# #前进
# #browse.forward()
# #后退
# #browse.back()
# #点击更多
# browse.find_element_by_xpath('//div[@class="s_tab"]/a[last()-1]').click()
#
# time.sleep(5)

browse.close()
