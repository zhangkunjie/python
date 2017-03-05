"""
数据收集：暂时没写例子
"""

from scrapy import log
import scrapy
class StatuscollectionSpider(scrapy.Spider):
    name = "logging"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = [
        "http://quotes.toscrape.com/tag/humor/"
    ]
    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').extract_first(),
                'author': quote.xpath('span/small/text()').extract_first(),
            }
            log.msg("This is a warning", level=log.WARNING)
