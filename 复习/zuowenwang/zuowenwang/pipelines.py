# -*- coding: utf-8 -*-
import pymongo
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ZuowenwangPipeline(object):
    #初始化方法
    def __init__(self):
        #连接mongo数据库
        self.client = pymongo.MongoClient('localhost', 27017)
        #创建数据库
        db = self.client.zuowenwang
        #创建集合
        self.zw = db.zuowen
    #调用open_spider  是检测开始的意思
    def open_spider(self, spider):
        print('开始了')

    def process_item(self, item, spider):
        #写入数据库
        self.zw.insert(dict(item))
        return item

    # 调用close_spider  是检测全部运行结束的意思
    def close_spider(self, spider):
        self.client.close()
        print('结束了')


