# -*- coding: utf-8 -*-
import pymongo


# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

# 数据管道  负责存储和清洗数据
class ScrapyTestPipeline(object):
    def __init__(self):
        # print(item)
        self.client = pymongo.MongoClient('localhost', 27017)
        db = self.client.tengxun
        self.jobs = db.jobs

    def open_spider(self, spider):
        print('开始了')
    def process_item(self, item, spider):
        # 先将数据转换成dict，然后插入数据
        self.jobs.insert(dict(item))
        print(self.jobs)
        return item

    def close_spider(self, spider):
        self.client.close()
        print('结束了')
