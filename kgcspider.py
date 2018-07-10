# -*- coding: utf-8 -*-
import scrapy
from kgc.items import *


class KgcspiderSpider(scrapy.Spider):
    name = 'kgcspider'
    #allowed_domains = ['http://www.kgc.cn/list/230-1-6-9-9-0.shtml']
    start_urls = ['http://www.kgc.cn/list/230-1-6-9-9-0.shtml']

    def parse(self, response):
        #print(response.body.decode())
        title = response.css('a.yui3-u.course-title-a.ellipsis::text').extract()
        price=response.css('div.right.align-right>span::text').extract()
        persons=response.css('span.course-pepo::text').extract()
        image_urls=response.css('a.kgc-w>img::attr("src")').extract()
        #print(title)
        datas=zip(title,price,persons,image_urls)
        for d in datas:
            item=KgcItem()
            item['title']=d[0]
            item['price']=d[1]
            item['persons']=d[2]
            item['image_urls']=[d[3]]
            yield  item
        # next_url=response.css('li.next>a::attr("href")').extract_first()
        #
        # if next_url is not None:
        #     yield response.follow(next_url,self.parse)
