#-*- coding:UTF-8 -*-
#pip3 install beautifulsoup4
# beautifulsoup4跟xpath功能相似，
# 是用来帮助我们清洗数据的
from bs4 import BeautifulSoup
import requests
from lxml import etree
import csv

url = 'https://hr.tencent.com/position.php?&start=0#a'
header = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:60.0) Gecko/20100101 Firefox/60.0',
}
response = requests.get(url,headers = header)
print(response.status_code)
with open('qichezhijia.html','w') as f:
    f.write(response.text)
html = response.text
#构建一个beautifulsoup对象，它是一个tag对象
# soup = BeautifulSoup(open('qichezhijia.html'),'lxml')
soup = BeautifulSoup(response.text,'lxml')

xhtml = etree.HTML(response.text)
# print(soup.prettify())
# print(type(soup))
tr_result = soup.find_all('tr')
#find_all使用class属性作为选择条件的时候，一定要注意加 class_
# tr_result1 = soup.find_all(class_='even')
# tr_result2 = soup.find_all(class_='odd')
tr_result1 = soup.select('.even')
tr_result2 = soup.select('.odd')
result = tr_result1 + tr_result2
#根据id查找，可以这样写
# tr_result1 = soup.find_all(id='homeDep')
# find_all返回的是一个list
# soup = BeautifulSoup(html,'lxml')
# prettify()帮助我们格式化的输出转换的html
# print(soup.prettify())
# print(soup.p)
# print(soup.head)
# print(type(soup.head))
#获取标签的所有属性
# print(soup.p.attrs)

# del soup.p['class']
# print(soup.p)

# result = soup.find_all('p') 
# print(result)
# for i in result:
#     print(i.name)
#     print(i.attrs) 
#     print(i.string)
#     print(i.get_text()) 

# css用法
# . 表示class
# “#” 表示id
# css选择器基本语法：
# <td><h3 class='oppt' id='ncnk'><h1></h1></h3></td>
# soup.select('td h3 h1') 
# soup.select('.oppt h1')
# soup.select('#ncnk h1')
# 返回的是一个列表
for tr in result:
    title = tr.select('td a')[0].get_text()
    job_type = tr.select('td')[1].get_text()
    need_pople = tr.select('td')[2].get_text()
    adress = tr.select('td')[3].get_text()
    publish = tr.select('td')[4].get_text()
    # print(title,job_type,need_pople,adress,publish)
    dict = {
        'title':title,
        'job_type':job_type,
        'need_pople':need_pople,
        'adress':adress,
        'publish':publish,
    }

    with open('zhiwei.csv','a') as csvfile:
        #创建一个csv的文件操作句柄
        fieldnames = ['title','job_type','need_pople','adress','publish']
        writer = csv.DictWriter(csvfile,fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow(dict)
        # writer = csv.writer(csvfile)

with open('zhiwei.csv','r') as csvfile:
      lines = csv.reader(csvfile)
      for line in lines:
          print(line)
        
    


#Xpath写法
xtr_odd =  xhtml.xpath('//tr[@class="odd"]')
xtr_even = xhtml.xpath('//tr[@class="even"]')
xtr_result = xtr_odd+xtr_even











