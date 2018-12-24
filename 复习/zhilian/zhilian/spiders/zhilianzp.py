# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from zhilian.items import ZhilianItem,ZhilianCompanyItem

class ZhilianzpSpider(CrawlSpider):
    a = []
    name = 'zhilianzp'
    allowed_domains = ['zhaopin.com','sou.zhaopin.com']
    start_urls = ['https://sou.zhaopin.com', 'http://sou.zhaopin.com/jobs/searchresult.ashx']

    rules = (
        #获取全部职位分类
        Rule(LinkExtractor(allow=(r'https://.*?'),
                           restrict_xpaths='//div[@class="search_topcontent_main"]'),
                           callback='parse_item',
                           follow=True),
        #获取详情页码
        Rule(LinkExtractor(allow=(r'.*?',),
                           restrict_xpaths='//div[@class="pagesDown"]'),
                           callback='parse_zhilian_page',
                           follow=True),
        #获取分类下面的详情
        Rule(LinkExtractor(allow=('http.*?.htm',),
                           restrict_xpaths='//div[@class="newlist_list_content"]'),
                           callback='parse_zhilian_detail_link',
                           follow=True),
        #获取公司的详情
        Rule(LinkExtractor(allow=('http.*?company.zhaopin.com/.*?htm',)),
                           callback='parse_company_detail'),

    )

    # 获取全部职位分类'
    def parse_item(self, response):
        print(response.status)
        print(response.url)
    # 获取详情页码
    def parse_zhilian_page(self, response):
        print(response.status)
        print(response.url)
    # 获取分类下面的详情
    def parse_zhilian_detail_link(self,response):
        print(response.url)
        item = ZhilianItem()
        # 职位名称
        item['jobName'] = response.xpath('//div[@class="inner-left fl"]//h1/text()').extract_first('')
        # 职位薪资
        item['salary'] = response.xpath('//div[@class="terminalpage clearfix"]//ul[@class="terminal-ul clearfix"]/li[1]/strong/text()').extract_first('').strip()
        # 发布时间
        item['publishTime'] = response.xpath('//span[@id="span4freshdate"]/text()').extract_first('')
        # 职位描述
        item['jobDesc'] = ''.join(response.xpath('//div[@class="terminalpage-main clearfix"]//div[@class="tab-inner-cont"]//text()').extract_first('')).replace('\n','')
        # 地址
        item['address'] = response.xpath('//div[@class="terminalpage-main clearfix"]//h2/text()').extract_first('').replace('\n','')
        # 公司名称
        item['company'] = response.xpath('//div[@class="inner-left fl"]//h2/a/text()').extract_first('')
        # 工作经验
        item['work_experience'] = response.xpath('//div[@class="terminalpage-left"]/ul/li[5]/strong/text()').extract_first('')
        # 学历
        item['education'] = response.xpath('//div[@class="terminalpage-left"]/ul/li[6]/strong/text()').extract_first('')
        # 工作性质
        item['work_nature'] = response.xpath('//div[@class="terminalpage-left"]/ul/li[4]/strong/text()').extract_first('')
        yield item

    def parse_company_detail(self, response):
        print(response.status)
        print(response.url)
        item = ZhilianCompanyItem()

        # 公司名称
        item['companyName'] = response.xpath('//div[@class="mainLeft"]//h1/text()').extract_first('').strip()
        # 公司类型
        item['companyType'] = response.xpath('//table[@class="comTinyDes"]/tr[1]/td[2]/span/text()').extract_first('')
        # 公司规模
        item['companyModel'] = response.xpath('//table[@class="comTinyDes"]/tr[2]/td[2]/span/text()').extract_first('')
        # 行业
        item['trade'] = response.xpath('//table[@class="comTinyDes"]/tr[3]/td[2]/span/text()').extract_first('')
        # 公司地址
        item['address'] = response.xpath('//table[@class="comTinyDes"]/tr[4]/td[2]/span/text()').extract_first('')

        yield item
