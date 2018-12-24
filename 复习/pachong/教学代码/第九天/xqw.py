#第一步找到分类
#找Ajax接口
# https://xueqiu.com/v4/statuses/public_timeline_by_category.json?
# since_id=-1&max_id=20289488&count=15&category=-1
# https://xueqiu.com/v4/statuses/public_timeline_by_category.json?
# since_id=-1&max_id=-1&count=10&category=105
# https://xueqiu.com/v4/statuses/public_timeline_by_category.json?
# since_id=-1&max_id=-1&count=10&category=111

# 数据层级结构
# data = {
#     'list':[
#         {},
#         {},
#         {},
#     ]
# }
# data['list']
# for item in data['list']:
#     print(item)
#     item['data']['id']
#     item['data']['title']


