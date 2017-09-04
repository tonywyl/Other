# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request,HtmlResponse
from scrapy.selector import Selector
from ..items import ImagesItem
from ..items import Cto51Item
class A51ctoSpider(scrapy.Spider):
    name = '51cto'
    allowed_domains = ['51cto.com']
    start_urls = ['http://51cto.com/']
    def start_requests(self):
        for url in self.start_urls:
            yield Request(url=url,method='GET',dont_filter=True,callback=self.parse)

    def parse(self, response):

        a_list=response.selector.xpath("//div[@class='pic']/a/@href").extract()

        for a_hre in a_list:
            yield Request(url=a_hre,method='GET',callback=self.parse1)
    def parse1(self,response):
        # print('img')
        imgs=response.selector.xpath("//img/@src").extract()
        # print(imgs)

        yield Cto51Item(img=imgs)

    # def parse2(self,response):
    #
    #     print('hahah')
    #     yield Cto51Item(img=response,filename=response.url)
    # def parse3(self,response):
    #     pass





















