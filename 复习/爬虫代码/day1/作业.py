import urllib.request
import ssl
import urllib.parse
#设置这个可以忽略https请求协议
context = ssl._create_unverified_context()
#打开url(https://docs.python.org/3/library/urllib.htm),并且把context传进去
#re = urllib.request.urlopen('https://docs.python.org/3/library/urllib.html',context=context)
#打印输出结果(以读的方式打开re，编码转换成utf-8)
#print(type(re))
#读取返回响应的状态码
#print(re.getheaders())
#单独获取响应头的其中某一个参数
#print(re.getheader('Content-Length'))

#创建一个post请求：
#这是一个字典  字典中有一个键(key)和值(value)
#datadict = {
#    'key':'value'
#}
#转换成url编码格式(betys字节的字符串)
#data = bytes(urllib.parse.urlencode(datadict),encoding='utf-8')
#第二种方法  结果一样
#data = parse.urlencode(datadict).encode('utf-8')
#输出结果
#print(data)





def getajax():
    #先输入一个要即将获取的网址
    url = 'https://movie.douban.com/j/search_subjects?'
    #变动的参数
    dataajax = {
        #页面限制
        'page_limit':'20',
        #页面开始
        'page_start':'40',
        'type':'tv',
    }
    #转换成url编码格式（字符串,这里不是post请求不用转换成字节，直接拼接在地址上）
    data = urllib.parse.urlencode(dataajax)
    
    url = url + data
    print('urlencode转换后:'+data,'完整的get请求地址为:'+url)
    #设置这个参数表示我们可以忽略https请求协议
    requestContext = ssl._create_unverified_context()
    # Request对象作为urlopen()方法的参数，发送给服务器并接收响应
    response = urllib.request.urlopen(url,context=requestContext)
    #打印结果可以知道获取的结果为一个json串
    result = response.read()
    #读取返回结果的类型
    print(type(response))
    #打印输出result
    print(result)
    #读取response中的网址
    print(response.url)
    #读取dict返回来的类型
    print(type(dict))
    #输出dict
    print(dict)
if __name__ == '__main__':
    getajax()


