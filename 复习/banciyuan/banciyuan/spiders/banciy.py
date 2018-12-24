# -*- coding: utf-8 -*-
import scrapy
from banciyuan.items import BanciyuanItem

class BanciySpider(scrapy.Spider):
    name = 'banciy'
    allowed_domains = ['bcy.net']
    start_urls = ['http://bcy.net/illust/']


    def parse(self, response):
        drawing = response.xpath('//li[@class="js-smallCards _box"]/@data-since').extract()
        for i in drawing:
            url = 'https://bcy.net/circle/timeline/showtag?since=%s&grid_type=flow&sort=hot&tag_id=5798'%i
            yield scrapy.Request(url,callback=self.parsedrawing)


    def parsedrawing(self,response):
        name = response.xpath('//a[@class="name"]/span/text()').extract()
        link = response.xpath('//img[@class="cardImage"]/@src').extract()
        comment = response.xpath('//span[@class="like"]/text()').extract()
        for i in range(0,len(name)):
            item = BanciyuanItem()
            item['name'] = name[i]
            item['link'] = link[i]
            item['comment'] = comment[i]
            #print(type(item['name']))
            yield item





