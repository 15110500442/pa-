# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZuowenwangItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 作文标题
    title = scrapy.Field()
    # 发布时间及作者
    shijian_zuozhe = scrapy.Field()
    #作文类型
    type = scrapy.Field()
    #作文字数
    zishu = scrapy.Field()
    #作文内容
    content = scrapy.Field()