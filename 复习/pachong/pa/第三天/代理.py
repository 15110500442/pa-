#urllib使用代理
#服务器吧咱们的ip封掉,请求的次数太鱼频繁
import urllib.request
#构造一个代理的Proxyhandler对象
hander = urllib.request.ProxyHandler({'协议':'ip和端口号'})
#需要用户名和密码的代理（需要验证）
#urllib.request.ProxyHandler({'协议':'用户名：密码ip+端口号'})
#创建一个opener对象
opener = urllib.request.build_opener(hander)
#使用opener.open方法去发起请求
rew = opener.open('http://www.baidu.com')
#查看响应的结果
print(rew.code)