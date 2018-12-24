# -*- coding:utf-8 -*-
# import urllib.request,urllib.parse
from urllib.request import Request
import re
import random
import pymysql
import urllib.request
import time

def get_page_data(startpage, endpage, url):
    for i in range(startpage, endpage + 1):
        # 构建完整的目标URL
        fullurl = url + 'nn/%s' % i
        # 调用方法发起请求
        send_request(fullurl)
        print(fullurl)


def send_request(fullurl):
    print(fullurl + '正在下载')
    headers = {
         'User-Agent':'Mozilla / 5.0(Linux;Android6.0;Nexus5Build / MRA58N) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 65.0.3325.146MobileSafari / 537.36',
     }
    req = Request(fullurl,headers=headers)
    response = urllib.request.urlopen(req)
    html = response.read().decode('utf-8')
    print(fullurl + '下载完成')
    compile1 = re.compile('<tr.*?class="odd".*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?class="country".*?<td>(.*?)</td>', re.S)
    result = re.findall(compile1, html)
    print(result)
    for info in result:
        conn = pymysql.connect(host='127.0.0.1', user='root', password='bc123', database='IP', port=3306, charset='utf8')
        cur = conn.cursor()
        sql = 'INSERT INTO ip VALUES(0,"%s","%s","%s")'%(info[0],info[1],info[2])
        cur.execute(sql)
        result = cur.fetchall()
        conn.commit()
        conn.close()



if __name__ == '__main__':
    startpage = input('请输入开始页码（从1开始）：')
    endpage = input('请输入结束页码：')
    print(startpage, endpage)
    url = 'http://www.xicidaili.com/'
    get_page_data(int(startpage),int(endpage), url)
