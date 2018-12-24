# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JobboleItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #标题、创建时间、文章地址、文章图片链接、点赞数量、收藏数量、评论数量、文章内容、标签
    #标题
    title = scrapy.Field()
    #创建时间
    creation_time = scrapy.Field()
    #文章地址
    article_addresses = scrapy.Field()
    #文章图片链接
    image_links = scrapy.Field()
    #点赞数量
    praise_num = scrapy.Field()
    #收藏数量
    collect_num = scrapy.Field()
    #评论数量
    comment_num = scrapy.Field()
    #文章内容
    centent = scrapy.Field()
    #标签
    label = scrapy.Field()



