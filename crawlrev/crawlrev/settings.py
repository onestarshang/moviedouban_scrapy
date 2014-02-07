# Scrapy settings for crawlrev project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'crawlrev'

SPIDER_MODULES = ['crawlrev.spiders']
NEWSPIDER_MODULE = 'crawlrev.spiders'

#ITEM_PIPELINES = {
#    'crawlrev.piplines.JsonWriterPipeline' : 800
#}


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'crawlrev (+http://www.yourdomain.com)'
