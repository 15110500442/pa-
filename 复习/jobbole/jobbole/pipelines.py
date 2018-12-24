# -*- coding: utf-8 -*-
import pymongo


# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class JobbolePipeline(object):

    def __init__(self):
        self.client = pymongo.MongoClient('localhost', 27017)
        db = self.client.jobbole
        self.jobs = db.jobsboledb

    def open_spider(self, spider):
        print('开始了')

    def process_item(self, item, spider):
        self.jobs.insert(dict(item))
        print(self.jobs)
        return item

    def close_spider(self, spider):
        self.client.close()
        print('结束了')
