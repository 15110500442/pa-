# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from meinv.items import MeinvItem

class MnSpider(CrawlSpider):
    name = 'mn'
    allowed_domains = ['mzitu.com']
    start_urls = ['http://mzitu.com/']

    rules = (
        #获取所有的分类
        Rule(LinkExtractor(allow=('http://www.mzitu.com/.*?/'),
                           restrict_xpaths='//ul[@id="menu-nav"]'),
                           ),
        #获取总分类的所有页码
        Rule(LinkExtractor(allow=('http://www.mzitu.com/.*?/'),
                           restrict_xpaths='//div[@class="nav-links"]'),
                           ),
        #获取详情
        Rule(LinkExtractor(allow=('http://www.mzitu.com/.*?'),
                           restrict_xpaths='//ul[@id="pins"]'),
                           callback='parse_item',),
        #获取详情的所有页码
        Rule(LinkExtractor(allow=('http://www.mzitu.com/.*?'),
                           restrict_xpaths='//div[@class="pagenavi"]'),
                           ),


    )

    def parse_item(self, response):
        item =  MeinvItem()
        #标题
        item['title'] = response.xpath('//h2[@class="main-title"]/text()').extract_first('')
        #分类
        item['classify'] = response.xpath('//div[@class="main-meta"]/span[1]/a/text()').extract_first('')
        #发布时间
        item['time'] = "".join(response.xpath('//div[@class="main-meta"]/span[2]/text()').extract_first('')).replace('发布于','')
        #浏览量
        item['page_view'] = response.xpath('//div[@class="main-meta"]/span[3]/text()').extract_first('')
        #图片链接
        item['image_link'] = response.xpath('//div[@class="main-image"]/p/a/img/@src').extract()
        yield scrapy.Request(item['image_link'][0],callback=self.a)
    def a(self,response):
        print(response.status)

