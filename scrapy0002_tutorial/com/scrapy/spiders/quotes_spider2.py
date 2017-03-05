import scrapy
class QuotesSpider2(scrapy.Spider):
    name = "quotes2"
    start_urls = [
        'http://quotes.toscrape.com'
    ]
    def parse(self, response):
        print("demo2:css选择器")
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').extract_first(),
                'author': quote.css('small.author::text').extract_first(),
                'tags': quote.css('div.tags a.tag::text').extract(),
            }
