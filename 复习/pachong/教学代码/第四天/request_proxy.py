# -*- coding:UTF-8 -*-
# urllib使用代理
# 服务器把咱们的ip封掉：请求的次数过于频繁，超过服务器设定的阀值
# 有付费代理和免费代理
import urllib.request

proxy = [
  '代理1',
  '代理2',
  '代理1',
  '代理2',
  '代理1',
  '代理2',
  '代理1',
  '代理2',
]
#判断打击是否有效
for i in proxy:
    #构建一个代理的ProxyHandler对象
    handler = urllib.request.ProxyHandler(i)
    #需要用户名和密码的代理（需要验证）
    # urllib.request.ProxyHandler({'协议':'用户名:密码@ip+端口号'})
    #创建一个opener对象
    opener = urllib.request.build_opener(handler)
    #使用opener.open方法去发起请求
    response = opener.open('http://www.baidu.com')
    html = response.read()
    if html:
        #查看响应的结果code
        print(response.code)
        print('当前代理可用')
    else:
        print('不可用')

