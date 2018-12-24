# -*- coding: utf-8 -*-
import scrapy
from jobbole.items import JobboleItem


class JobbolespiderSpider(scrapy.Spider):
    name = 'jobbolespider'
    allowed_domains = ['blog.jobbole.com']
    start_urls = ['http://blog.jobbole.com/all-posts/']


    def parse(self, response):
        job_even = response.xpath('//div[@class="post floated-thumb"]/div/a/@href').extract()
        for url in job_even:
            yield scrapy.Request(url,callback=self.parseJobDetail)
        likes = response.xpath('//div[@class="navigation margin-20"]//a/@href').extract()
        for i in likes:
            yield scrapy.Request(i,callback=self.parse)

    def parseJobDetail(self, response):
        print(response.status)
        item = JobboleItem()
        item['title'] = response.xpath('//div[@class="grid-8"]/div/div[@class="entry-header"]/h1/text()')[0].extract()
        item['creation_time'] = response.xpath('.//p[@class="entry-meta-hide-on-mobile"]/text()')[0].extract()
        item['article_addresses'] = response.url
        item['image_links'] = response.xpath('//*[@class="entry"]//img/@src').extract()
        item['praise_num'] = response.xpath('//div[@class="post-adds"]/span[1]/h10/text()').extract()
        item['collect_num'] = response.xpath('//div[@class="post-adds"]/span[2]/text()').extract()
        item['comment_num'] = response.xpath('//span[@class="btn-bluet-bigger href-style hide-on-480"]/text()').extract()
        item['centent'] = response.xpath("//div[@class='entry']//p/text()").extract()
        item['label'] = response.xpath('//div[@class="entry-meta"]/p/a[3]/text()').extract()
        yield item