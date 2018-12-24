# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SanwanwangItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #标题
    title = scrapy.Field()
    #时间
    time = scrapy.Field()
    #阅读量
    read_num = scrapy.Field()
    #内容
    content = scrapy.Field()
