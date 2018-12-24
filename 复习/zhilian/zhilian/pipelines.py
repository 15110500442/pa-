# -*- coding: utf-8 -*-
import pymysql
from twisted.enterprise import adbapi
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ZhilianPipeline(object):
    def __init__(self,dbpool):
        self.dbpool = dbpool

    #使用这个函数来应用settings配置文件。
    @classmethod
    def from_settings(cls,settings):
        parmas = {
            'host':settings['MYSQL_HOST'],
            'user':settings['MYSQL_USER'],
            'passwd':settings['MYSQL_PASSWD'],
            'db':settings['MYSQL_DB'],
            'port':3306,
            'charset':'utf8',
        }

        # **表示字典，*tuple元组,
        # 使用ConnectionPool，起始最后返回的是一个ThreadPool
        dbpool = adbapi.ConnectionPool('pymysql',**parmas)

        return cls(dbpool)

    def process_item(self, item, spider):
        #这里去调用任务分配的方法
        query = self.dbpool.runInteraction(self.insert_data_todb,item,spider)
        #数据插入失败的回调
        query.addErrback(self.handle_error,item)


    #执行数据插入的函数
    def insert_data_todb(self,cursor,item,spider):
        insert_str,parmas = item.insertdata()
        cursor.execute(insert_str,parmas)
        print('插入成功')

    def handle_error(self,failure,item):
        print(failure)
        print('插入错误')
        #在这里执行你想要的操作

    def close_spider(self, spider):
        self.dbpool.close()
