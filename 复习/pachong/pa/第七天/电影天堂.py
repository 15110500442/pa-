from urllib.request import Request, urlopen
import urllib.request


# http://dytt8.net/html/gndy/dyzz/list_23_1.html
def get(url,endpage):
    for page in range(1, endpage + 1):
        fullurl = url + '%s.html' % page
        chuli(fullurl)


def chuli(fullurl):
    headers = {
        'User-Agent': 'Mozilla / 5.0(Linux;Android6.0;Nexus5Build / MRA58N) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 65.0.3325.146MobileSafari / 537.36'
    }
    req = Request(fullurl, headers=headers)
    response = urlopen(req)
    html = response.read()
    html = html.decode('gbk')
    print(html)


if __name__ == '__main__':
    endpage = int(input('请输入截止的页面：'))
    print(endpage)
    url = 'http://dytt8.net/html/gndy/dyzz/list_23_'
    get(url,endpage)
