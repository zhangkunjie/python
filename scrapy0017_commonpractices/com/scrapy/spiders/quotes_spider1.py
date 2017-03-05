

import scrapy
from time import sleep


class QuotesSpider1(scrapy.Spider):
    name = "quotes1"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = [
        "http://quotes.toscrape.com/tag/humor/"
    ]
    download_delay = 10
    def parse(self, response):
        for quote in response.css('div.quote'):
            sleep(10)
            yield {
                'text': quote.css('span.text::text').extract_first(),
                'author': quote.xpath('span/small/text()').extract_first(),
            }
        next_page = response.css('li.next a::attr("href")').extract_first()
        if next_page is not None:
            sleep(10)
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)