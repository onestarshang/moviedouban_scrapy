# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
#coding:utf-8
from scrapy.item import Item, Field

class MoviereaderItem(Item):
    # define the fields for your item here like:
    # name = Field()
    review = Field()
    movie = Field()
    
    pass

class MovieitemsItem(Item):
    content = Field()
    pass
