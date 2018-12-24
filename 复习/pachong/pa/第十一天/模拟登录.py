from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException,NoSuchElementException
import requests
from lxml import etree

browse = webdriver.Chrome(executable_path='/home/bc/下载/chromedriver')
browse.get('https://github.com/login')
browse.implicitly_wait(5)
try:
    #browse.find_element_by_css_selector('.text-bold.text-white.no-underline').click()
    browse.find_element_by_id('login_field').send_keys('15110500442')
    browse.find_element_by_id('password').send_keys('sjl1314520')
    browse.find_element_by_css_selector('.btn.btn-primary.btn-block').click()
    browse.find_element_by_css_selector('.avatar.float-left.mr-1').click()
    browse.implicitly_wait(5)
    browse.find_element_by_xpath('//*[@id="user-links"]/li[3]/details/ul/li[3]/a').click()
    url = 'https://github.com/15110500442'
    response = requests.get(url)
    print(response.text)
    with open('github.html','a') as f:
        f.write(response.text)
except NoSuchElementException:
    print('')


