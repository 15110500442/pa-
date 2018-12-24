# -*- coding:UTF-8 -*-
import urllib.request as request
import ssl
import urllib.parse as parse
#构造一个请求
#get请求
#设置这个参数表示我们可以忽略https请求协议
context = ssl._create_unverified_context()
# response = request.urlopen('https://docs.python.org/3/library/urllib.html',context=context,timeout=0.1)
#打印返回结果
# print(response.read().decode('utf-8'))
#查看返回的结果类型
# print(type(response))
# #查看返回的状态码
# print(response.status)
# #读取返回响应的响应头
# print(response.getheaders())
# #单独获取响应头里面其中的某一参数
# print(response.getheader('Content-Length'))

# urlopen(url, data=None, timeout=socket._GLOBAL_DEFAULT_TIMEOUT,
            # *, cafile=None, capath=None, cadefault=False, context=None):

# data：data参数是可选择的，如果没有这个参数，那我们发起的请求默认是get
#如果有这个参数，默认post请求，如果这个要赋值，那是字节类型（bytes）
#创建一个post请求
datadict = {
    "name":"liwenhao",
    "sex":"1",
}
data = bytes(parse.urlencode(datadict),encoding='utf-8')
# data = parse.urlencode(datadict).encode('utf-8')
print(data)
response = request.urlopen('https://httpbin.org/post',data=data,context=context)
print(response.read())
# timeout：设置请求的超时时间，一旦超过设置的值，就会报错
#urllib.error.URLError: <urlopen error _ssl.c:817: The handshake operation timed out>

# context：可以忽略安全证书的存在
# capath：设置CA证书的路径
# cafile: 指定CA证书