from urllib.request import Request,urlopen
from urllib import parse
import ssl
import re
def tiebaSpider(url, beginPage, endPage):
    b = []
    for page in range(beginPage, endPage + 1):
        pn = (page - 1) * 12
        fullurl = url + 'offset=' + str(pn)
        # print(fullurl)
        response = urlopen(fullurl)
        resultcontent = response.read().decode('utf-8')
        pattern = re.compile('<div.*?cinema-info.*?href="(.*?)".*?>(.*?)</a>.*?cinema-address">(.*?)</p>',re.S)
        result = re.findall(pattern,resultcontent)
        for i in result:
            b.append(i)
    print(b)
    with open('filename.txt','a') as f:
        f.write(str(b))
        print('完成')

def main():
    beginPage = int(input("请输入起始页："))
    endPage = int(input("请输入终止页："))
    url = 'http://maoyan.com/cinemas?'
    tiebaSpider(url,beginPage,endPage)

if __name__ == '__main__':
    main()
