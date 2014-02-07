from scrapy.spider import Spider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request
from crawlrev.items import MovieitemsItem
import time
import crawlrev.setGB as setGB
import os, sys
import json

def getMovieList():
    filep = os.path.join(setGB.jsondir, '%s.json'%setGB.usr)
    lines = open(filep)
    ids =[]
    for l in lines:
        link = json.loads(l)['movie'][0]
        if link.find('movie') != -1:
            id = link.split('/')[-2]
            ids.append(id)
    return ids

class MovieitemsSpider(Spider):
    global movieids, myf
    name = 'movieitems'
    allowed_domains = ['api.douban.com']
    movieids = getMovieList()
    path = os.path.join(setGB.jsondir, 'movieitems.json')
    myf = open(path, 'wb')
    
    start_urls = ['http://api.douban.com/v2/movie/subject/%s'%(movieids[0])]
    movieids.remove(movieids[0])
    
    def parse(self, response):
        myf.write(response.body + "\n")
        for mid in movieids :
            next_url = 'http://api.douban.com/v2/movie/subject/%s'%mid
            yield Request(next_url, callback=self.parse)
        pass
    
        