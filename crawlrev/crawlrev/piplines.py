# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
#coding:utf-8
import json
import setGB
class JsonWriterPipeline(object):
    def __init__(self):
        self.file = open('items_%s.json'%setGB.usr, 'wb')
    
    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item
    
class MovieItemsPipline(object):
    def __init__(self):
        self.file = open('movieitems.json', 'wb')
        
    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item
