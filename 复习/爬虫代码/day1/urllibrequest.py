from urllib.request import Request,urlopen
import urllib.parse as parse
import ssl
#urlopen(官方给我们封装的一个简单的发起请求的方法)
#def __init__(self, url, data=None, headers={},
#                 origin_req_host=None, unverifiable=False,
#                 method=None):
#url:这是我们要请求的路径
#data：我们需要出入的相关参数，如果要传入的话必须是bytes类型
#headers:请求头
#origin_req_host：指域名或者是IP
#method：请求方式（post get）
#unverifiable：意思是说用户没有足够的权限来访问资源
#默认是False，表示我们有权获取，默认是True，表示我们没有权限获取
#构建一个请求对象
# url = 'http://www.1905.com/film/?fr=homepc_menu_news'
#url = 'http://www.1905.com/film/?fr=homepc_menu_news'
headers = {
    'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Mobile Safari/537.36',
}
#构造了一个get方式的请求对象，设置了url，headers。请求方式
#req = Request(url,headers=headers,method='GET')
#response = urlopen(req)
#print(response.read())
#构造一个get请求
data = {
    'wd':'美女',
    'ie':'utf-8'
}
url = 'https://www.baidu.com/s?wd=%E7%BE%8E%E5%A5%B3&pn=0'
context = ssl._create_unverified_context()
data = parse.urlencode(data).encode('utf-8')
print(data)
req = Request(url,data=data,headers=headers,method='GET')
response = urlopen(req,context=context)
resultcontent = response.read().decode('utf-8')
print(response.read().decode('utf-8'))
with open('05.html','w') as f:
     f.write(resultcontent)


