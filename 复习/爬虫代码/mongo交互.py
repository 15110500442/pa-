import pymongo


#本地的两种连接方式
a = pymongo.MongoClient('127.0.0.1',27017)
#a1 = pymongo.MongoClient('loacalhost',27017)


#远程链接
#client = pymongo.MongoClient('mongodb://localhost:27017/')
#获取数据库
db = a.jobs
#获取数据中的集合
jobs = db.jobs
#查询所有的数据文档
# b = jobs.find()
# for i in b:
#     print(i)


#如果数据库存在就获取  不存在就创建
db = a.meinv
model = db.model

docement = {
    'name':'tianjing',
    'age':'20',
    'class':'201',
    'height':'165',

}
docement1 = {
    'name': 'tianjing1',
    'age': '29',
    'class': '202',
    'height': '165',

}

docement2 = {
    'name': 'tianjing2',
    'age': '27',
    'class': '203',
    'height': '165',

}

docement3 = {
    'name': 'tianjing3',
    'age': '30',
    'class': '204',
    'height': '165',

}
#插入单条
#c = model.insert(docement)



#插入多条
# d = model.insert([docement1,docement2,docement3])
# print(d)
# c = model.find()



# #获取第一条：
# d = model.find_one()
# print(d)


# #条件获取
# e = model.find({'name':'tianjing3'})
# print(e)
# for i in e:
#     print(i)


# #获取第一条满足条件
# f = model.find_one({'name':'tianjing3'})
# print(f)


#跳过第一条数据获取后面的所有数据
# g = model.find().skip(1)
# for i in g:
#    print(i)


#跳过第一条,获取后面2条
# h = model.find().skip(1).limit(2)
# for i in h:
#      print(i)


#删除数据
# j = model.remove({'name':'tianjing'})
# print(j)


# #更新数据
# i = model.update({'name':'tianjing2'},{'$set':{'height':199}})
# print(i)


#显示所有
# c = model.find()
# for i in c:
#    print(i)


#排序
# c = model.find().sort('age',1)
# for i in c:
#     print(i)


#save跟update区别是什么？ 如果update跟新内容的话（_id）在集合中不存在，就无法跟新
#如果update跟新内容的话（_id）在集合中不存在，就会插一条数据




