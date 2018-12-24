# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from sanwanwang.items import SanwanwangItem

class SanwenSpider(CrawlSpider):
    name = 'sanwen'
    allowed_domains = ['sanwen.com']
    start_urls = ['http://www.sanwen.com/sanwen/shige/']

    rules = (
        #获取诗歌下面的所有标题
        Rule(LinkExtractor(allow=('/.*?/'),restrict_xpaths='//div[@class="row inner-row"]//li[@class="head"]')),
        #获取诗歌详情的所有页码
        Rule(LinkExtractor(allow=('.*?.html'), restrict_xpaths='//div[@class="list-pages"]'),follow=True),
        #获取诗歌详情
        Rule(LinkExtractor(allow=('.*?.html'), restrict_xpaths='//div[@class="list-base-article"]'), callback='parse_item',follow=True),

    )

    def parse_item(self, response):
        item = SanwanwangItem()
        #标题
        item['title'] = response.xpath('//div[@class="row-article"]/h1/text()').extract_first('')
        #发布时间
        item['time'] = response.xpath('//div[@class="article-writer"]/div/text()').extract_first('').replace('阅读：', '')
        #阅读次数
        item['read_num'] = response.xpath('//span[@id="read"]/text()').extract_first('')
        #内容
        item['content'] = "".join(response.xpath('//div[@class="article-content"]/text()').extract()).replace('','').split()
        yield item


        #i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        #return i
