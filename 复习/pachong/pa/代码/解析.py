#urllib.parse:解析url 拼接  编码
import urllib.parse

url = 'https://cn.bing.com/search?q=%E7%BE%8E%E5%A5%B3&qs=n&'
#urlparse:拆分一个url链接
r = urllib.parse.urlparse(url)
print(r)
#  scheme： 协议
#  netloc： 域名
#  path：   路径
#  params： 参数
#  query：  查询条件，一般用于get请求
#  fragment： 锚点


#urlunparse是拼接
urls = ('https','cn.bing.com','/search','','q=%E7%BE%8E%E5%A5%B3&qs=n&','')
fullurl = urllib.parse.urlunparse(urls)
print(fullurl)


#urlencode:一班用于字典序列化为url编码的格式
da = {
    'name':'s',
    'pwd':'fdsf'
}
data = urllib.parse.urlencode(da).encode('utf-8')
print(data)

#parsr_qs:将url编码的格式化为字典

a = urllib.parse.parse_qs(data)
print(a)
for k,v in a.items():
    print(k.decode('utf-8'),v[0].decode('utf-8'))


#urljoin:url的拼接
base_url = 'http://maoyan.com/cinema'
son_url = 'cinema/15280?poi=99389254'
fullurl = urllib.parse.urljoin(base_url,son_url)
print(fullurl)

