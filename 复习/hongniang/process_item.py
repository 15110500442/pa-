import redis
import pymongo
import json

def main():
    #mongo连接
    mongocli = pymongo.MongoClient('127.0.0.1',27017)
    #redis连接
    rediscli = redis.StrictRedis(host='127.0.0.1', port=6379, db=0)

    #拿到mongo里面的数据库
    db = mongocli['hongniang']
    #拿数据库中的集合
    hn = db['hn']

    while True:

        source,data = rediscli.blpop(['hn:items'])
        data = data.decode('utf8')
        #转换成json
        item = json.loads(data)
        #写入数据
        hn.insert(item)
        print(source,data)













if __name__ == '__main__':
    main()