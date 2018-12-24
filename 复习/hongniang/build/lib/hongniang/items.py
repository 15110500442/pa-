# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HongniangItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #姓名
    name = scrapy.Field()
    #年龄
    age = scrapy.Field()
    #身高
    height = scrapy.Field()
    #工作地点
    worklocal = scrapy.Field()

