# -*- coding: utf-8 -*-
import pymongo
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class SanwanwangPipeline(object):
    #初始化方法
    def __init__(self):
        #连接数据库
        self.client = pymongo.MongoClient('localhost', 27017)
        #创建数据库
        db = self.client.sanwenwang
        #创建数据库中的集合
        self.sw = db.sanwen
    #调用open_spider方法
    def open_spider(self, spider):
        print('开始了')

    def process_item(self, item, spider):
        #写入数据库
        self.sw.insert(dict(item))
        print(self.sw)
        return item

    # 调用close_spider方法
    def close_spider(self, spider):
        self.client.close()
        print('结束了')

