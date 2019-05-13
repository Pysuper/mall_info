# -*- coding: utf-8 -*-
import scrapy
from info.items import InfoItem


class JdSpider(scrapy.Spider):
    name = 'jd'
    allowed_domains = ['jd.com']
    start_urls = ['http://www.jd.com/']

    def parse(self, response):
        # 获取京东下面的电脑分类数据
        """
        extract(): 返回的是一个数组list, 里面包含了多个string, 如果只有一个string, 则返回['ABC']这样的形式
        extract_first(): 返回的是一个string字符串, 是list数组里面的第一个字符串
        """
        computer = response.xpath('//li[@clstag="h|keycount|head|category_03a"]/a[1]/@href').extract()
        for cate_href in computer:
            item = InfoItem()
            computer_href = "https:" + cate_href
            print(computer_href)
            yield scrapy.Request(
                url=computer_href,
                callback=self.parse_detail,
                meta={
                    "item":item
                }
            )

    def parse_detail(self, response):
        print(response.url)
        cate_2_title = response.xpath('//div[@class="menu-cont"]/a/text()').extract()
        cate_2_href = response.xpath('//div[@class="menu-cont"]/@href').extract()
        print(cate_2_href, cate_2_title)

        # for title, href in zip(cate_2_title, cate_2_href):
        #     print(title, href)
