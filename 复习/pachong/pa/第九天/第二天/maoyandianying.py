from urllib.request import urlopen, Request
import re


def get_image(startpage, endpage,url):
    for page in range(startpage, endpage + 1):
        pn = (page - 1) * 12
        fullurl = url + 'offset=' + str(pn)
        chuli(fullurl)
        print(fullurl)


def chuli(fullurl):
    req = Request(fullurl)
    response = urlopen(req)
    html = response.read().decode('utf-8')
    pattern = re.compile('<div.*?cinema-info.*?href="(.*?)".*?>(.*?)</a>.*?cinema-address">(.*?)</p>', re.S)
    result = re.findall(pattern, html)
    print(result)
    for i in result:
        infotext = ':'.join(i)
        with open('maoyandy.txt', 'a') as f:
            f.write(infotext)


if __name__ == '__main__':
    startpage = int(input('请输入开始页码（从1开始）：'))
    endpage = int(input('请输入结束页码：'))
    url = 'http://maoyan.com/cinemas?'
    print(startpage, endpage)
    get_image(startpage, endpage,url)
