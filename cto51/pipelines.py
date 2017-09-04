# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy,re
from scrapy.http import Request
import os,sys
from scrapy.contrib.pipeline.images import ImagesPipeline
from scrapy.exceptions import DropItem
import requests
import urllib
class Cto51Pipeline(object):
    def __init__(self):
        self.f=None
    def process_item(self, item, spider):

        for img_url in item['img']:

            result=requests.get(url=img_url)
            print(result)
            filename=img_url.split('/')

            self.f=open('/Users/tony/self_file/py_fullstacks4/year2017mon9day2/cto51/cto51/img/'+filename[-1],'wb')

            self.f.write(result.content)
            print('done')

    @classmethod
    def from_crawler(cls,crawler):
        return cls()

    def open_spider(self,spider):
        # self.f=open('img/%s'%)
        print('spider start ',spider)






















