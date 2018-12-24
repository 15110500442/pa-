# selenium 模拟登陆
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests 
from fake_useragent import UserAgent
#
from selenium.common.exceptions import TimeoutException,NoSuchElementException

driver = webdriver.Chrome(executable_path='/Users/ljh/Desktop/chromedriver')

#打开豆瓣首页
driver.get('https://www.douban.com/')
#显示等待，目的是为了等待页面全部加载完毕
driver.implicitly_wait(10)
#做了异常处理
try:
    driver.find_element_by_id('form_email').send_keys('18518753265')
    driver.find_element_by_id('form_password').send_keys('ljh123456')
    driver.find_element_by_class_name('bn-submit').click()
except NoSuchElementException:
    #如果没有找到对应的element对报错
    print("没有这个节点")

#获取cookie值
print(driver.get_cookies())
#也可以直接使用driver打开个人主页，获取个人主页信息
# driver.get('https://www.douban.com/people/175417123/')
# print(driver.page_source)

#_pk_ses.100001.8cb4=*; __utma=30149280.894979317.1528945710.1528945710.1528945710.1; 
#拼接cookie
cookie_str = ''
for cookie in driver.get_cookies()[::-1]:
    # print(type(cookie))
    cookie_str += cookie['name']+'+'+cookie['value']+'; '

print(cookie_str[:-2])

#构造header
ua = UserAgent()
headers = {
    'User-Agent':ua.chrome,
    'cookie':cookie_str,
    'Referer':'https://www.douban.com/',
    'Host':'www.douban.com'
}
#构造请求发起请求，获取响应
response = requests.get('https://www.douban.com/people/175417123/',headers=headers)
print(response.status_code)





