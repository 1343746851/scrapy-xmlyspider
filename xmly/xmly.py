#-*- coding: utf-8 -*-
'''
python3.6
@File  : xmly.py
@Author: min
@Date  : 2018/8/24
@Desc  : 
'''
# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import request

from xmly.items import XmlyItem
from scrapy.linkextractors import LinkExtractor  # 提取链接
from scrapy.spiders import CrawlSpider, Rule  # 爬取规则
import json



name = 'myxmly'
allowed_domains = ['ximalaya.com']
# start_urls = [
#     # 'http://www.ximalaya.com/revision/category/queryCategoryPageAlbums?category=youshengshu&subcategory=wenxue&meta=&sort=0&page=1&perPage=30'
#     'http://www.ximalaya.com/youshengshu/wenxue/'
# ]



def get_page(self, start_urls):

    pass

def parse(self, response):
    # print(response.text)
    # dataList = json.loads(response.text)['data']['albums']
    dataList = response.xpath('//div[@class="content"]//div[@class="u0jN album-wrapper "]')
    for data in dataList:
        # 书名
        bookName = data.xpath('.//a[@class="u0jN album-title lg"]/@title').extract()[0]
        # 书链接
        link = 'http://www.ximalaya.com' + data.xpath('.//a[@class="u0jN album-title lg"]/@href').extract()[0]

        # print(bookName, link)
        request = scrapy.Request(link, callback=self.get_zhanghui)
        request.meta['bookName'] = bookName
        # 发送请求
        yield request

def get_zhanghui(self, response):
    # 实例
    items = XmlyItem()
    # 接收
    bookName = response.meta['bookName']
    '''
    https://www.ximalaya.com/revision/album/getTracksList?albumId=16318024&pageNum=1
    https://www.ximalaya.com/revision/album/getTracksList?albumId=14192790&pageNum=1
    '''
    # 简介
    IntroductionList = response.xpath('//article[@class="vd4u intro"]//text()').extract()[:]
    Introduction = ""
    for i in IntroductionList:
        Introduction += i
        # print(Introduction)
    # 章节名
    chapterList = response.xpath('//li[@class="dOi2"]')
    # print(chapterList,'***'*30)
    for chapter in chapterList:
        chapterName = chapter.xpath('.//a/@title').extract()[0]
        yinPinUrl = 'https://www.ximalaya.com' + chapter.xpath('.//a/@href').extract()[0]

        print(bookName, '==', Introduction, '==', chapterName, '==', yinPinUrl, "+++++++++++++++")



if __name__ == '__main__':
    url = 'http://www.ximalaya.com/youshengshu/wenxue/'
    # request.Request(url,headers=)