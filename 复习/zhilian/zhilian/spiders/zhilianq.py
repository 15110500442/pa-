# -*- coding: utf-8 -*-
import scrapy


class ZhilianqSpider(scrapy.Spider):
    name = 'zhilianq'
    allowed_domains = ['sou.zhaopin.com']
    start_urls = ['http://sou.zhaopin.com/']

    def parse(self, response):
        pass
