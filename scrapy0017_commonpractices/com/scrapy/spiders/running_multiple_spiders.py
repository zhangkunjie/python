"""
多线程运行spider
"""

from django.utils.log import configure_logging
from scrapy.crawler import CrawlerProcess, CrawlerRunner
from twisted.internet import reactor

from com.scrapy.spiders.quotes_spider1 import QuotesSpider1
from com.scrapy.spiders.quotes_spider2 import QuotesSpider2


process = CrawlerProcess()
process.crawl(QuotesSpider1)
process.crawl(QuotesSpider2)
process.start()
