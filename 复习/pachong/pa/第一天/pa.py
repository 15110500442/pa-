import urllib.request
import ssl
import urllib.parse


context = ssl._create_unverified_context()
url = 'https://www.baidu.com/s?'
#https://www.baidu.com/s?wd=%E7%88%AC%E8%99%AB&pn=0&oq=%E7%88%AC%E8%99%AB&tn=baiduhome_pg&ie=utf-8&usm=2&rsv_idx=2&rsv_pq=dcdd048d0006aab2&rsv_t=ac29QzFnh%2BCDQDvjvuZXrKzcbgrCZqna4ymCHjw4P5EVon9hZaMcf22hEhCnSlSdJDm4
page = int(input('请输入你要爬取的页数:'))
for yeshu in range(1,page + 1):
    print("第%s页下载中......"%yeshu)
    pn = str((yeshu - 1) * 10)
    data = {
        'ie':'utf-8',
        'pn':pn,#第一页为0.第二页为10,以此类推
        'wd':'爬虫'
    }
    header = {
        'User-Agent':'Mozilla / 5.0(Linux;Android6.0;Nexus5Build / MRA58N) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 65.0.3325.146Mobile Safari / 537.36'
    }
    data = urllib.parse.urlencode(data)
    url1 = url + data
    print(url1)
    request = urllib.request.Request(url1,headers=header,method='GET')
    response = urllib.request.urlopen(request,context=context)
    print(response.url)
    a = response.read().decode('utf-8')


    wenjian = '第%s页.html' %yeshu
    with open(wenjian,'w') as f:
        f.write(a)
    print('第%s页下载完成'% yeshu)
