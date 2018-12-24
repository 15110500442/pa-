# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class JiansSpider(CrawlSpider):
    name = 'jians'
    allowed_domains = ['jianshu.com']
    start_urls = ['https://www.jianshu.com']
    rules = (
         Rule(LinkExtractor(allow=r'',
                            restrict_xpaths='//div[@class="recommend-collection"]'),
                            callback='parse_item',
                            follow=True),

         Rule(LinkExtractor(allow=r'',
                            restrict_xpaths='//ul[@class="note-list"]'),
                            callback='parse_jianshu_detail',
                            follow=True),

         Rule(LinkExtractor(allow=('')),
              callback='parse_jianshu_detail1',
              follow=True),
    )

    def parse_item(self, response):
        print(response.status)
        print(response.body)

    def parse_jianshu_detail(self, response):
        # print(response.status)
        # title = response.xpath('//a[@class="title"]/text()').extract()
        # print(title)
        pass


    def parse_jianshu_detail1(self, response):
        #print(response.body)
        # title = response.xpath('//a[@class="title"]/text()').extract()
        # print(title)
        pass

