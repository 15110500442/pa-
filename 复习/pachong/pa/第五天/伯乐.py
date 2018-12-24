import urllib.request
from urllib.request import Request
from lxml import etree
import re


def get_page_data(startpage, endpage, url):
    for i in range(startpage, endpage + 1):
        # 构建完整的目标URL
        fullurl = url + 'page/%s/' % i
        # 调用方法发起请求
        send_request(fullurl)
        print(fullurl)


def send_request(fullurl):
    print(fullurl + '正在下载')
    headers = {
        'User-Agent': 'Mozilla / 5.0(Linux;Android6.0;Nexus5Build / MRA58N) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 65.0.3325.146MobileSafari / 537.36',
    }
    req = Request(fullurl, headers=headers)
    response = urllib.request.urlopen(req)
    html = response.read().decode('utf-8')
    print(fullurl + '下载完成')
    reqq = re.compile('<li.*?class="media".*?<div.*?class="media-body">(.*?)</div>',re.S)
    result = re.findall(reqq, html)
    print(result)
    for i in result:
        htmlstr = etree.tostring(i).decode('UTF-8')
        print(htmlstr)



if __name__ == '__main__':
    startpage = input('请输入开始页码（从1开始）：')
    endpage = input('请输入结束页码：')
    print(startpage, endpage)
    url = 'http://top.jobbole.com/'
    get_page_data(int(startpage), int(endpage), url)
