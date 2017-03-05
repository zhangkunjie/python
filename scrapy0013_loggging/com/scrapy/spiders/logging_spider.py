"""
CRITICAL - 严重错误(critical)
ERROR - 一般错误(regular errors)
WARNING - 警告信息(warning messages)
INFO - 一般信息(informational messages)
DEBUG - 调试信息(debugging messages)
"""

from scrapy import log
import scrapy
class LoggingSpider(scrapy.Spider):
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
