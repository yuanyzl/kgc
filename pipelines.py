# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class KgcPipeline(object):
    def open_spider(self,spider):
    #当蜘蛛启动时自动执行
        self.file=open("/home/yzhl/IdeaProjects/kgc/kgc.csv","w",encoding='utf8')
    def process_item(self, item, spider):
    #蜘蛛每yild一个item，执行一次
        line=item["title"]+","+item["price"]+','+item["persons"]+','+item["images_urls"]+'\n'
        self.file.write(line)
        return item
    def close_spider(self,spider):
    #蜘蛛完成工作关闭执行
        self.file.close()
