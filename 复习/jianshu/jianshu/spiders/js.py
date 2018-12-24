# -*- coding: utf-8 -*-
import scrapy


class JsSpider(scrapy.Spider):
    name = 'js'
    allowed_domains = ['']
    start_urls = ['http://www.ygdy8.net/html/gndy/jddy/20180622/57010.html']

    def parse(self, response):
        url = response.xpath('div[@class="recommend-collection"]/a[@class="collection"]/@href')
        print(response.status)
