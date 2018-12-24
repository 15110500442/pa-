import re
import urllib.request
from urllib.request import Request,urlopen


def get_image(url,start,end):
    for page in range(start,end +1):
        fullurl = url + 'list%s.html'%page
        chuli(fullurl)
        print(fullurl)
        
def chuli(fullurl):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
    }
    req = Request(fullurl,headers=headers)
    response = urlopen(req)
    html = response.read().decode('gbk')
    print(html)
    link = re.compile(r'<div.*?class="w1000 box03".*?<ul.*?<li.*?<a.*?scr="(.*?)"',re.S)
    print(link)






if __name__ == '__main__':
    start = int(input('请输入开始页面:')) 
    end = int(input('请输入结束页面:'))  
    url = 'http://www.yggk.net/xiaohua/xiaohua/'  
    get_image(url,start,end)