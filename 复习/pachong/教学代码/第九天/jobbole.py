# -*- coding:utf-8 -*-
# pip3 install pyquery
# import pyquery.PyQuery as PyQuery
from pyquery import PyQuery
import requests

#目标url
url = 'http://blog.jobbole.com/all-posts/'
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:60.0)'
}
response = requests.get(url,headers=headers)
print(response.status_code)
# with open('jobbole.html','w') as f:
#     f.write(response.text)

pq_html = PyQuery(response.text)
# pq_html = PyQuery(filename='jobbole.html')
# pq_html = PyQuery(url)
# print(type(pq_html))
# print(pq_html.html())

result_articles = pq_html('.post.floated-thumb')

# print(result_articles)
# print(result_articles.items())

for sub_div in result_articles.items():
    print('======大美妞=======')
    # print(sub_div)
    print(type(sub_div))
    title = sub_div('.archive-title').text()
    link = sub_div('.archive-title').attr('href')
    print(title,link)
    # print(sub_div.children())
    # print(sub_div.parents())
    # print(sub_div.hasClass('xidada')) 






