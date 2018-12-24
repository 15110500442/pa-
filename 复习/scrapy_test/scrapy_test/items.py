# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyTestItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #职位名称
    name = scrapy.Field()
    #工作地点
    didian = scrapy.Field()
    #工作类别
    leibie = scrapy.Field()
    #职责
    zhize = scrapy.Field()
    #要求
    yaoqiu= scrapy.Field()
