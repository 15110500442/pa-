import json
# json.load：读取本地的json文件，并转化为python对象
# json.loads:将json字符串转换为Python对
# json.dump:可以将python对象转换为json字符串，并且可以写入文件
# json.dumps:将python对象转换为json字符串


# json.loads
json_str = '{"data":{"dict1":"value1","dict2":"value2","dict2":"value2"}}'
dict = json.loads(json_str)
print(dict)
print(type(dict))

#json.dumps
json_str_1 = json.dumps(dict)
print(json_str_1)
print(type(json_str_1))

# json.dump
# 不加ensure_ascii默认是ascii编码，ensure_ascii = False 表示utf8
json.dump(dict,open('json_dump.json','w'),ensure_ascii=False)

# json.load,读取本地的json文件，并转化为python对象
data = json.load(open('json_dump.json','r'))
print(data)
