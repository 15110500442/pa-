# -*- coding: utf-8 -*-
import pymongo
from scrapy.pipelines.images import ImagesPipeline
import scrapy
import os
#为了找到settings.py文件对应的值
from scrapy.utils.project import get_project_settings
import json
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
class BanciyuanImagePipleline(ImagesPipeline):

    IMAGES_STORE = get_project_settings().get('IMAGES_STORE')

    def get_media_requests(self, item, info):
        # 根据图片链接构造一个Request，给调度器，放在任务队列里面
        image_url = item['link']
        # for url in image_url:
        #     yield scrapy.Request(url)
        yield scrapy.Request(image_url)

    def item_completed(self, results, item, info):
        for ok, value in results:
            print(results)
            if ok:
                image_path = value['path']
                try:
                    os.rename(self.IMAGES_STORE + '/' + image_path,self.IMAGES_STORE+'/'+ item['name'] +'.jpg')
                    item['path'] = self.IMAGES_STORE+'/'+item['name']+'.jpg'
                finally:
                    return item



class BanciyuanPipeline(object):

    def __init__(self):
        self.client = pymongo.MongoClient('localhost', 27017)
        db = self.client.drawing
        self.huihua = db.drawings

    def open_spider(self, spider):
        print('开始了')

    def process_item(self, item, spider):
        self.huihua.insert(dict(item))
        print(self.huihua)
        return item

    def close_spider(self, spider):
        self.client.close()
        print('结束了')




    # def __init__(self):
    #     self.file = open('imageurl.json', 'a+')
    #
    # def process_item(self, item, spider):
    #     data = json.dumps(dict(item), ensure_ascii=False)
    #     self.file.write(data + '\n')
    #     return item
    #
    # def close_spider(self, spider):
    #     self.file.close()
