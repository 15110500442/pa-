# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from zuowenwang.items import ZuowenwangItem

class ZuowenSpider(CrawlSpider):
    name = 'zuowen'
    allowed_domains = ['263y.com']
    start_urls = ['http://263y.com/']

    rules = (
        #获取的总的分类
        Rule(LinkExtractor(allow=('http://www.263y.com/.*?/'),
                           restrict_xpaths='//div[@class="nav"]'),
                           callback='parse_item', follow=True),
        #获取的二级分类
        Rule(LinkExtractor(allow=('http://www.263y.com/.*?/'),
                           restrict_xpaths='//div[@class="span8"]/div[@class="tit"]'),
                           follow=True),
        #获取二级分类下的所有页码
        Rule(LinkExtractor(allow=('.*?.html'),
                           restrict_xpaths='//div[@class="pagination pagination-centered"]'),
                           follow=True),
        #获取所有的详情作文
        Rule(LinkExtractor(allow=('http.*?.html'),
                           restrict_xpaths='//div[@class="zw_item"]'),
                           callback='parse_detail',follow=True),

    )

    def parse_item(self, response):
        print(response.url)
        #i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        #return i
    def parse_detail(self,response):
        print(response.url)
        item = ZuowenwangItem()
        #作文标题
        item['title'] = response.xpath('//h1[@class="text-center font24"]/text()').extract_first('')
        #发布时间及作者
        item['shijian_zuozhe'] = response.xpath('//div[@class="view_left"]/text()').extract_first('').replace('\n', '').replace('\r', '')
        #作文类型
        item['type'] = response.xpath('//div[@class="view_left"]/a[1]/text()').extract_first('')
        #作文字数
        item['zishu'] = response.xpath('//div[@class="view_left"]/a[2]/text()').extract_first('')
        #作文内容
        item['content'] = ''.join(response.xpath('//div[@class="view"]//p/text()').extract()).replace('\n', '').replace('\r', '').replace('\t', '').replace('上一篇', '').replace('标签', '')
        yield item
