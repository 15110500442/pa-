# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from hongniang.items import HongniangItem
from scrapy_redis.spiders import RedisCrawlSpider

class HnSpider(CrawlSpider):
    name = 'hn'
    allowed_domains = ['hongniang.com']
    redis_key = ' hn:start_urls'
    #start_urls = ['http://www.hongniang.com/index/search?sort=0&wh=0&sex=2&starage=1,2,3,4,5,6,7,8,9,10&province=%E5%8C%97%E4%BA%AC&city=0&marriage=1&edu=3,2,4,5,6,7&income=1,2,3,4,5,6,7,8&height=0&pro=0&house=0&child=0&xz=0&sx=0&mz=0&hometownprovince=0']

    rules = (
        Rule(LinkExtractor(allow=r'http.*?page=\d+'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow='.*?user.*?',allow_domains=('www.hongniang.com')), callback='parse_detail', follow=True),

    )

    def parse_item(self, response):
        print(response.url)
        # i = {}
        # #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        # #i['name'] = response.xpath('//div[@id="name"]').extract()
        # #i['description'] = response.xpath('//div[@id="description"]').extract()
        # return i

    def parse_detail(self, response):
        print(response.url)
        item = HongniangItem()
        # 姓名
        item['name'] = response.xpath('//div[@class="name nickname"]/text()').extract_first('').strip()
        # 年龄
        item['age'] = response.xpath('//div[@class="sub1"]//div[@class="info2"]//ul[1]//li[1]/text()').extract_first('')
        # 身高
        item['height'] = response.xpath('//div[@class="sub1"]//div[@class="info2"]//ul[2]//li[1]/text()').extract_first('')
        # 工作地点
        item['worklocal']  = response.xpath('//div[@class="sub1"]//div[@class="info2"]//ul[3]//li[2]/text()').extract_first('')
        yield item