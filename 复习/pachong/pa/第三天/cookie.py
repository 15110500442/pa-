import urllib.request
import http.cookiejar
#创建一个cookiejar对象,他用使用存储cookie的
cookie = http.cookiejar.CookieJar()

#创建一个cookie的处理器对象handler
cookie_headler = urllib.request.HTTPCookieProcessor(cookie)

#作用创建opener
opener = urllib.request.build_opener(cookie_headler)

#使用open方法请求
req = opener.open('http://www.baidu.com')


cookie_str = ''
for i in cookie:
    print(i.name,i.value)
    cookie_str = cookie_str + i.name + '=' + i.value + ':'
print(cookie_str[:-1])




#mozillaCookieJar():可以直接指定保存的文件，使用save方法保存
cookie_file = 'cookie.txt'

#构建一个mozillaCookieJar对象来保存cookie
mz_cookie = http.cookiejar.MozillaCookieJar(cookie_file)

#构建一个cookie的处理对象
hander = urllib.request.HTTPCookieProcessor(mz_cookie)

#构建一个opener对像
opener = urllib.request.build_opener(hander)

#发起请求
a = opener.open('http://www.baidu.com')


#设置为全部变量
#保存
mz_cookie.save()
print(a.code)

mz_cookie.load('cookie.txt')
print(mz_cookie)





