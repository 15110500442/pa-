import json
import scrapy

# json.load:可以将json字符串转化为python对象，并且可以写入文件
# json.loads:将json字符串转化为python对象
# json.dump:将python对象转化为json字符串 并且写入文件
# json.dumps:将python对象转化为json字符串

# j'son.loads:
j = '[1,2,3,4,5]'
json_str = '{"data":{"dict1":"value1","dict2":"value2","dict3":"value3"}}'
s = json.loads(json_str)
print(type(json_str))
