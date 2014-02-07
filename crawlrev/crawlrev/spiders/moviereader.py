from scrapy.spider import Spider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request
from crawlrev.items import MoviereaderItem
import time
import crawlrev.setGB as setGB

class MoviereaderSpider(Spider):
    global _URL
    name = "moviereader"
    allowed_domains = ["douban.com"]
    _URL = 'http://www.douban.com/people'
    start_urls = ['%s/%s/reviews'%(_URL, setGB.usr)]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        revlist = hxs.select('//div[@class="article"]/ul')
        for rev in revlist:
            item = MoviereaderItem()
            item['reveiw'] = rev.select('li[1]/h3/a/@href').extract()
            item['movie'] = rev.select('li[2]/a/@href').extract()
            yield item
        
        page = hxs.select('//div[@class="paginator"]')
        if page:
            start = 1
            all = []
            for p in page.select('a/text()'):
                all.append(p.extract())
            all.sort()
            end = int(all.pop())
            
            while start<end:
                """http://www.douban.com/people/onestar/reviews?start=10"""
                next_url = '%s/%s/reviews?start=%s'%(_URL, setGB.usr, start*10)
                time.sleep(0.1)
                start +=1
                yield Request(next_url, callback=self.parse)
