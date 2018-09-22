# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class XmlyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 书名
    bookName = scrapy.Field()
    # 简介
    introduction = scrapy.Field()
    # 章节名
    chapterName = scrapy.Field()
    # 音频url
    yinPinUrl = scrapy.Field()