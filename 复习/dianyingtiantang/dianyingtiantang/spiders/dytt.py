# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class DyttSpider(CrawlSpider):
    name = 'dytt'
    allowed_domains = ['dytt8.net']
    start_urls = ['http://dytt8.net/']

    rules = (
        #电影分类
        Rule(LinkExtractor(allow=('http.*?html'),
                           restrict_xpaths='//div[@id="menu"]'),
                           callback='parse_item',
                           follow=True),
        #获取电影中的所有页码
        Rule(LinkExtractor(allow=('list_.*?html'),
                           restrict_xpaths='//div[@class="co_content8"]'),
                           callback='parse_dytt_page',
                           follow=True),
        #获取电影名
        Rule(LinkExtractor(allow=('/html.*?html'),
                           restrict_xpaths='//div[@class="co_content8"]/ul'),
                           callback='parse_dytt_detail',
                           follow=True),

    )

    def parse_item(self, response):
        print(response.status)
        i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return i

    def parse_dytt_page(self, response):
        print(response.status)

    def parse_dytt_detail(self, response):
        #发布时间
        #release_time = response.xpath('//div[@class="co_content8"]/ul/text()').re('\d-\d-\d')
        #title = response.xpath('//div[@class="co_content8"]/div/div[@id="Zoom"]/span/p[1]/text()').extract()
        with open('r.html','a+') as f:
            f.write(response.text)

