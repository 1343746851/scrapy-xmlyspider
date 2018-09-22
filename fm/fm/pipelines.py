# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from fm.items import FmItem, ChapterItem


class FmPipeline(object):
    def process_item(self, item, spider):

        # 判断是哪一个item
        if isinstance(item, FmItem):
            print(item.items())
        elif isinstance(item, ChapterItem):
            print(item.items(), "++++++++++")
        else:
            pass

        return item
