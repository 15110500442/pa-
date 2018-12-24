import random
import pymysql
import urllib.request
import ssl

context = ssl._create_unverified_context()
conn = pymysql.connect(host='127.0.0.1', user='root', password='bc123', database='IP', port=3306, charset='utf8')
cur = conn.cursor()
sql = 'SELECT count(*) FROM ip'
cur.execute(sql)
result = cur.fetchone()
conn.commit()
a = random.randint(1,int(result[0]))
print(a)
sql1 = 'SELECT ipaddr,duankou,type FROM ip WHERE id = "%d"'%a
cur.execute(sql1)
result = cur.fetchone()
httpproxy_handler = urllib.request.ProxyHandler({'http':'%s:%s'%(result[0],result[1])})
opener = urllib.request.build_opener(httpproxy_handler)
url = 'https://xueqiu.com/'
request = urllib.request.Request(url)
response = opener.open(request)
print(response.read())
print(result)
with open('xueqiu.txt','a') as f:
    f.write(response)