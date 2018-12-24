# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

#继承CrawlSpider，CrawlSpider他又继承是Spider
class CrawljonboleSpider(CrawlSpider):
    #爬虫名称
    name = 'crawljonbole'
    #域
    allowed_domains = ['blog.jobbole.com']
    #起始url
    start_urls = ['http://blog.jobbole.com/']

    rules = (
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return i
