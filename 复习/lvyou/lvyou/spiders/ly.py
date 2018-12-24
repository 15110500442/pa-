# -*- coding: utf-8 -*-
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from lvyou.items import LvyouItem


class LySpider(CrawlSpider):
    name = 'ly'
    allowed_domains = ['lvyou.baidu.com']
    start_urls = ['https://lvyou.baidu.com/scene/t-all_s-all_a-all_l-all']

    rules = (
        Rule(LinkExtractor(allow=('.*?rn=')), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=('/.*?/'), restrict_xpaths='//header[@class="filter-result-hd pr yahei"]/h3'),
             callback='parse_detail', follow=True),
        # Rule(LinkExtractor(allow=('.*?'), restrict_xpaths='//div[@class="main-title clearfix"]'),
        #      callback='parse_detail_luxian')
    )

    def parse_item(self, response):
        print(response.status)

    def parse_detail(self, response):
        # item = LvyouItem()
        # # 标题
        # item['title'] = response.xpath('//span[@class="main-name clearfix"]/a/text()').extract_first('')
        # # 评分
        # item['grade'] = ''.join(response.xpath('//div[@class="main-score"]/text()').extract()).replace('\n', '')
        # # 评论
        # item['comment'] = response.xpath('//a[@class="remark-count"]/text()').extract_first('')
        # # 内容
        # item['content'] = response.xpath('//p[@class="main-desc-p"]/text()').extract_first('')
        # # 图片连接
        # item['link'] = response.xpath('//a[@class="pic-more more-pic-tip clearfix"]/@href').extract_first('')
        # # 路线
        # item['luxian_num'] = response.xpath('//*[@id="J_line-count"]/text()').extract_first('')
        urlww = response.xpath('//a[@id="J_line-count"]/@href').extract()
        print(urlww)
        # for i in url:
        #
        #     print(i.url)

            # fullurl = 'https://lvyou.baidu.com%s'%i



    # def parse_detail_luxian(self, response):
    #     print(response.url)
    #     item = LvyouItem1()
    #     # 标题
    #     item['title1'] = response.xpath('//div[@class="counselor-plan-detail"]/div/a/text()').extract_first('')
    #     # 线路1
    #     item['luxian1'] = '->->'.join(
    #         response.xpath('//div[@class="counselor-plan-detail"]/div[2]//span/text()').extract())
    #     # 线路2
    #     item['luxian2'] = '->->'.join(
    #         response.xpath('//div[@class="counselor-plan-detail"]/div[3]//span/text()').extract())
    #     # 精
    #     item['key_work'] = response.xpath('//div[@class="key-word"]//span/text()').extract()

