# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import requests
import lxml

url = 'https://www.autohome.com.cn/all/'
header = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:60.0) Gecko/20100101 Firefox/60.0',
}
response = requests.get(url,headers=header)
response.encoding = 'gbk'
# print(response.text)

# soup = BeautifulSoup(response.text,features='lxml')
soup = BeautifulSoup(response.text,features='html.parser')
# print(soup.prettify())
list = soup.select('.article')
# print(list)

for i in list:
    print(i)