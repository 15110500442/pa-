import requests



#使用request发起一个get请求

#response = requests.get('http://docs.python-requests.org/zh_CN/latest/')
#发起一个带参数的请求
#url = 'https://cn.bing.com/search?q=%E7%99%BE%E5%BA%A'
dict = {
   'q':'百度'
}
# a = requests.get('https://cn.bing.com/search?',params=dict)
# print(a.url)


#发起一个请求默认是会验证ssl证书,这里是verify
# a = requests.get('http://www.12306.cn',verify=false)
# print(a.)

#设置代理
proxy = {
    'https':'https://125.120.10.240:6666'
}
a = requests.get('https://cn.bing.com/search?',params=dict,proxies=proxy)
print(a.status_code)
print(a.text)






#响应状态码
#print(response.status_code)
#响应的结果  字符串
#print(response.text)
#字节类型‘xxxx’  二进制流的方式
#print(response.content)
#查看我们请求的网址
#print(response.url)
#获取响应的头
#print(response.headers)
# cookie = a.cookies
# cookie_str = ''
# for i in cookie:
#     print(i.name, i.value)
#     cookie_str = cookie_str + i.name + '=' + i.value + '; '
# print(cookie_str[:-1])