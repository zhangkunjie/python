"""
通过脚本的方式启动爬虫
"""

from scrapy.crawler import CrawlerProcess
from com.scrapy.spiders.quotes_spider1 import QuotesSpider1
process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})
process.crawl(QuotesSpider1)
process.start() # the script will block here until the crawling is finished