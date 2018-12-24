import urllib.request
import http.cookiejar
#创建一个cookiesJar对象，他用使用存储cookie的
cookie = http.cookiejar.CookieJar()

#构建一个cookie的处理器对象handler
cookie_handler = urllib.request.HTTPCookieProcessor(cookie)

#作用构建opener，
opener = urllib.request.build_opener(cookie_handler)

#使用open方法项服务器发送请求，获取响应
response = opener.open('http://www.baidu.com')

# print(response.code)
# print(cookie)
cookie_str = ''
for item in cookie:
    # print(item.name)
    # print(item.value)
    cookie_str = cookie_str + item.name+'='+item.value+';'
# print(cookie_str)    



#mozillaCookieJar():可以直接指定保存的文件，使用save方法保存

cookie_file = 'cookie.txt'

#构建一个 mozillaCookieJar 对象来保存cookie
mz_cookie = http.cookiejar.MozillaCookieJar(cookie_file)

#读取本地的cookie对象
# mz_cookie.load(cookie_file)
# print(mz_cookie)

#构建一个cookie的处理器对象
handler = urllib.request.HTTPCookieProcessor(mz_cookie) 

#构建一个opener对象
opener = urllib.request.build_opener(handler)

#发送请求（打开一个url）
response = opener.open('http://www.baidu.com')

#设置为全局的opener,这个时候调用urlopen方法实质上是使用了
#你自定义的opener
urllib.request.install_opener(opener)
urllib.request.urlopen('http://www.baidu.com')

#保存方法cookie
# mz_cookie.save()

#获取响应的状态
print(response.code)

mz_cookie.load(cookie_file)
print(mz_cookie)




