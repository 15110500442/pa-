#-*- coding:utf-8 -*-
# pip install requests
# http://docs.python-requests.org/zh_CN/latest/
import requests
#使用requests发起一个get请求
# response = requests.get('http://docs.python-requests.org/')
#发起一个带参数的get请求
# https://www.baidu.com/s?wd=%E7%BE%8E%E5%A5%B3
dict = {
    'wd':'美女'
}
# response = requests.get('https://www.baidu.com/s',params=dict)
# print(response.url)

#发起一个请求默认是会验证SSL证书，这里verify设置为False意思就是关闭（忽略）SSL验证
# response = requests.get('https://www.12306.cn',verify=False)

# 设置代理 
# https://125.120.10.240:6666
proxies = {
    'https':'https://125.120.10.240:6666',
}
# http://ip.chinaz.com/
response = requests.get('https://www.baidu.com',params=dict,proxies=proxies)
#响应的状态码
response.encoding = 'utf-8'
print(response.status_code)
#响应的结果，字符串
print(response.text)
# #字节类型b'xxxxxxx'
# print(response.content)
# #查看我们请求的网址
# print(response.url)
# #获取响应的头
# print(response.headers)
#可以直接读取cookie
# cookie = response.cookies
# print(type(cookie))
# # print(cookie)
# print(type(cookie.items()))
# print(cookie.items())
# #浏览器里面的格式_ga=GA1.2.1432862965.1528245025; _gid=GA1.2.1623234917.1528245025
# for item in cookie.items():
#     print(item)
#     print(item[0])
#     print(item[1])
# 
