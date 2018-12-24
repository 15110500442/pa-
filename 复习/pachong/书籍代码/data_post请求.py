import urllib.parse
import urllib.request


#传送一个参数 并且要把它转换成字节流（bytes）
data = bytes(urllib.parse.urlencode({'work':'hello'}),encoding='utf-8')
#发起一个请求,并且传入参数,超时时间为1秒
#response = urllib.request.urlopen('http://www.httpbin.org/post',data=data,timeout=1)
#设置超时时间
response1 = urllib.request.urlopen('http://www.httpbin.org/post',timeout=1)
print(response1.read())

#请求回来的参数
# {"args":{},
#  "data":"",
#  "files":{},
#  "form":{"work":"hello"},
#  "headers":{"Accept-Encoding":"identity",
#  "Connection":"close",
#  "Content-Length":"10",
#  "Content-Type":"application/x-www-form-urlencoded",
#  "Host":"www.httpbin.org",
#  "User-Agent":"Python-urllib/3.5"},
#  "json":null,
#  "origin":"124.205.158.242",
#  "url":"http://www.httpbin.org/post"
#  }