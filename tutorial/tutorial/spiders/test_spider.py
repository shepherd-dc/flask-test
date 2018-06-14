import scrapy
from tutorial.items import TestItem

class TestSpider(scrapy.Spider):
    name = "test"
    allowed_domains = ["sina.com.cn"]
    start_urls = [
        "http://roll.finance.sina.com.cn/finance/jj4/jjyj/index.shtml"
    ]

    def parse(self, response):
        for sel in response.xpath('//ul/li'):
            item = TestItem()
            item['title'] = sel.xpath('a/text()').extract()
            item['link'] = sel.xpath('a/@href').extract()
            yield item
