import urllib.request


#使用urlopen来请求一个网页 而且赋值给response
response = urllib.request.urlopen('https://www.python.org')
#以只读的方式输出  并且解析码为utf8
#print(response.read().decode('utf-8'))
#查看他的类型
print(type(response))
#查看请求的状态码
print(response.status)
#获取到响应的请求头
print(response.getheaders())
#为获取的响应的请求头添加一个参数
print(response.getheaders('Server'))
#这是一个说明,可以看见urlopen里面有什么参数
#def urlopen(url, data=None, timeout=socket._GLOBAL_DEFAULT_TIMEOUT,*, cafile=None, capath=None, cadefault=False, context=None):

