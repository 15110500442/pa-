from pyquery import PyQuery
from lxml import etree
import pymysql
import re
# html = """
# <div>
# <tr class="item-0">
# <td>first section</td>
# <td>1111</td>
# <td>17-01-28 22:51</td>
# </tr>
# <tr class="item-1">
# <td>second section</td>
# <td>2222</td>
# <td>17-01-28 22:53</td>
# </tr>
# </div>
# """

# #可以通过4种方式来进行初始化
# #可以通过传入 字符串、lxml、文件 或者 url 来使用PyQuery。
# pqhtml1 = PyQuery(html)
# print(type(pqhtml1))
# # print(pqhtml1)

# pqhtml2 = PyQuery('http://blog.jobbole.com/all-posts/')
# # print(pqhtml2)

pqhtml3 = PyQuery(filename='data.html') # 传入文件 example.html
# print(pqhtml3.html()) # html()方法获取当前选中的 html 块
articles = pqhtml3('.post.floated-thumb')
# print(articles)
#是一个pyquery.pyquery.PyQuery对象

print(type(articles))
#  :param host: Host where the database server is located
#     :param user: Username to log in as
#     :param password: Password to use.
#     :param database: Database to use, None to not use a particular one.
#     :param port: MySQL port to use, default is usually OK. (default: 3306)

# self.client = pymysql.Connect('localhost','root','ljh123456','ipproxy',3306)
client = pymysql.Connect('localhost','root','ljh123456','jobbole',3306,charset='utf8') 
cursor = client.cursor()
sql = """INSERT INTO article(imageurl,title,desc,time,comentnum)VALUES(%s,%s,%s,%s,%s)"""
sql = """INSERT INTO article(imageurl,title)VALUES(%s,%s)"""


for item in articles.items():
    image_url = item.find('.post-thumb')('a img').attr('src')
    title = item('.archive-title').text().replace(' ','')
    desc = item('span.excerpt p').text()
    time = item('.post-meta p').eq(0).text()
    tag = item('.post-meta p').eq(0)('a').eq(1).text()
    parretn_re = re.compile(".*?(\d+/\d+/\d+).*?",re.S)
    coment_num = item('.post-meta p').eq(0)('a').eq(2).text()
    time = re.findall(parretn_re,time)[0]
    if coment_num=='':
        coment_num='0评论'
    print('++++++++++')
    print((image_url,title,desc,time,tag,coment_num))
    
    # cursor.execute(sql,(image_url,title,desc,time,coment_num))
    cursor.execute(sql,(image_url,title))
    client.commit()

    #http://www.codeweblog.com/利用pyquery获取html指定标签内容/

    # title = item.find('a').text()
    # href = item.find('a').attr('href')
    # print(item.find('a').attr('href'))
    # print(type(item))



# -*- coding: utf-8 -*-
# from pyquery import PyQuery as pq#引入 PyQuery

# doc = pq(filename='example.html')# 传入文件 example.html

# print (doc.html()) # html()方法获取当前选中的 html 块

# print (doc('.item-1')) # 相当于 class 选择器，选取 class 为 item-1 的 html 块

# data = doc('tr') # 选取 <tr> 元素

# for tr in data.items():# 遍历 data 中的 <tr> 元素
#     temp = tr('td').eq(2).text() # 选取第3个 <td> 元素中的文本块
#     print(temp)


# 7、其他操作：
# .addClass(value)：添加 class；
# .hasClass(name)：判断是否包含指定的 class，返回 True 或 False；
# .children()：获取子元素；
# .parents()：获取父元素；
# .next()：获取下一个元素；
# .nextAll()：获取后面全部元素块；
# .not_('selector')：获取所有不匹配该选择器的元素；
# for i in d.items('li'): 
# print i.text()：遍历 d 中的 li 元素