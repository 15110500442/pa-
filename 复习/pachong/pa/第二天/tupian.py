import ssl
import urllib.parse
import urllib.request
import re
context = ssl._create_unverified_context()
page = 5

for i in range(1,page+1):
    url = 'https://www.ugirls.com/Index/Search/Magazine-57-%s.html'%i
    data = {

    }
    header = {
        # 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
    }
    data = urllib.parse.urlencode(data).encode('utf-8')
    # print(data)
    req = urllib.request.Request(
        url,  # 目标网址
        data=data,  # 要传入的相关参数，如果要传入必须是bytes类型
        headers=header,  # 请求头
        # origin_req_host =  None,  # 指域名或ip
        # method='GET',  # 请求方式(post,get)
        # unverifiable = False,   # 请求权限，False 为有权限
    )
    response = urllib.request.urlopen(req, context=context)
    result = response.read().decode('utf-8')

    with open('youguo.txt', 'w') as x:
        x.write(result)
    f = open('youguo.txt','r')
    d = str(f.read())
    f.close()

    a = r'<img.*?magazine_img lazy.*?data-original="(.*?)".*?>'
    result = re.compile(a,re.S)
    ret = re.findall(result,d)

    for p in ret:
        count = ret.index(p)+1
        print('正在下载第%s页第%d张图片'%(i,count))
        b = r'https://img.ugirls.tv/uploads/magazine/cover/\d*/*\d*/*\d*/*(.*?).jpg'
        resul = re.compile(b, re.S)
        ree = re.findall(resul, p)
        #print(ree)
        print('下载中...')
        picUrl = p
        response = urllib.request.urlopen(picUrl, context=context)
        result = response.read()

        with open('pic/%s.jpg'%ree[0], 'wb') as x:
            x.write(result)
            print('第%s页第%d张图片下载完成'%(i,count))
