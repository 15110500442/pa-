# -*- coding:utf-8 -*-
import urllib.request
from urllib import parse
import json

def transfrom(str):
    # POST请求的目标URL
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null'
    headers = {
        'User_Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
    }
 
    formData = {
        'action':'FY_BY_REALTIME',
        'client':'fanyideskweb',
        'doctype':'json',
        'from':'zh-CHS',
        'i':str,
        'keyfrom':'fanyi.web',
        'to':'en',
        'typoResult':'false',
        'version':'2.1',
    }
    #print(formData)
 
    #data = parse.urlencode(formData)
    #直接转会报错，POST data should be bytes, an iterable of bytes,
    #or a file object. It cannot be of type str.
    data = parse.urlencode(formData).encode('utf-8')
    #print(data)

    request = urllib.request.Request(url,data=data,headers=headers)
    response = urllib.request.urlopen(request)
    result = response.read().decode('utf-8')

    #json.loads() 是把 Json格式字符串解码转换成Python对象，
    #如果在json.loads的时候出错，要注意被解码的Json字符的编码。(后面会讲到)
    dict = json.loads(result)
    print(type(dict))
    print(dict['translateResult'][0][0]['tgt'])
 
if __name__ == '__main__':
    while True:
        str = input('请输入需要翻译的中文:')
        transfrom(str)