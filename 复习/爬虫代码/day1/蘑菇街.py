import requests
import re
import json
# 获取首页分类菜单
# '[图片]http://mce.mogucdn.com/jsonp/multiget/3?callback=jQuery21109555013915685151_152844997983
# 3&pids=109499%2C109520%2C109731%2C109753%2C110549%2C109779%2C110548%2C110547%2C109757%2C109793%2C109795%2C110563%2C110546%2C110544&_=1528449979837'
# 从连接中找分类id 分类的名称
response  =requests.get('http://mce.mogucdn.com/jsonp/multiget/3?callback=jQuery21109165411369411709_1528699316717&pids=110119&_=1528699316718')
# print(response.text)
pattern = re.compile("jQuery.*?\((.*?)\)")
print(pattern)
# json_data = re.findall(pattern,response.text)
# data = json.loads(json_data)
# b = data['data']['110119']['list']
# print(b)



