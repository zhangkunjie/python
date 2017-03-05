import scrapy
class QuotesSpider3(scrapy.Spider):
    name = "quotes3"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
    ]
    print("demo3：列表页递归")
    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').extract_first(),
                'author': quote.css('small.author::text').extract_first(),
                'tags': quote.css('div.tags a.tag::text').extract(),
            }
        #得到下一页的链接地址    
        next_page = response.css('li.next a::attr(href)').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)