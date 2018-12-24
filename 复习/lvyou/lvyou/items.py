# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LvyouItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    grade = scrapy.Field()
    comment = scrapy.Field()
    content = scrapy.Field()
    link = scrapy.Field()
    luxian_num = scrapy.Field()


# class LvyouItem1(scrapy.Item):
#     title1  = scrapy.Field()
#     luxian1 = scrapy.Field()
#     luxian2 = scrapy.Field()
#     key_work = scrapy.Field()




