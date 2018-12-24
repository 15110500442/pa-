# -*- coding: utf-8 -*-
import scrapy
from scrapy_test.items import ScrapyTestItem
from urllib.parse import urljoin

class TengxunSpider(scrapy.Spider):
    #爬虫的名称:启动爬虫的时候找对的爬虫文件
    name = 'tengxun'
    #允许爬取的域  你要爬区的链接必须是在这个域下面，可以是多个域
    allowed_domains = ['hr.tencent.com']
    #起始的url，可以有多个
    start_urls = ['https://hr.tencent.com/position.php']
    base_url = 'https://hr.tencent.com/position.php'
    #解析数据，response请求放回响应的结果
    def parse(self, response):
        #状态码
        #print(response.status)
        #全部文本
        # print(response.body)
        #目标数据: 职位名称  工作地点 职位类别   工作职责  工作要求
        
        
        
        job_even = response.xpath('//tr[@class="even"]/td[@class="l square"]/a/@href').extract()
        job_odd = response.xpath('//tr[@class="odd"]/td[@class="l square"]/a/@href').extract()
        #print(job_even, job_odd)
        #总的职位链接
        jobs = job_even + job_odd
        for i in jobs:
            fullurl = urljoin('https://hr.tencent.com/position.php',i)
            #print(fullurl)
            #yield在这里是实现一个异步,每当遇到yield就会先返回yield后面的值,下次在执行的时候，会从上次的执行中断处开始
            yield scrapy.Request(fullurl,callback=self.parseJobDetail)
        likes = response.xpath('//div[@class="pagenav"]//a/@href').extract()
        for url in likes:
            if 'position.php' in url:
           
                fullurl = urljoin(self.base_url,url)
                yield scrapy.Request(fullurl,callback=self.parse)

    #解析每一个职位详情
    def parseJobDetail(self,response):
        print(response.status)
        item = ScrapyTestItem()
        item["name"] = response.xpath('.//td[@id="sharetitle"]/text()').extract()[0]
        item["didian"] = response.xpath('.//tr[@class="c bottomline"]/td[1]/text()').extract()[0]
        item["leibie"] = response.xpath('.//tr[@class="c bottomline"]/td[2]/text()').extract()[0]
        item["zhize"] = response.xpath('//table[@class="tablelist textl"]/tr[3]//li/text()').extract()
        item["yaoqiu"] = response.xpath('//table[@class="tablelist textl"]/tr[4]//li/text()').extract()
        #print(name,didian,leibie,zhize,yaoqiu)
        yield item
            
        

        

