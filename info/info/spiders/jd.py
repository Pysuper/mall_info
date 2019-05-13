# -*- coding: utf-8 -*-
import scrapy


class JdSpider(scrapy.Spider):
    name = 'jd'
    allowed_domains = ['jd.com']
    start_urls = ['http://www.jd.com/']

    def parse(self, response):
        cate_1_href = response.xpath('//li[@class="cate_menu_item"]/a/@href').extract()
        cate_1_title = response.xpath('//li[@class="cate_menu_item"]/a/text()').extract()

        for href_1, title_1 in zip(cate_1_href, cate_1_title):
            print(href_1, title_1)
