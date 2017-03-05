import scrapy
class SpiderDemo1(scrapy.Spider):
    name = 'SpiderDemo1'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = [
        'http://quotes.toscrape.com/'
    ]
    def parse(self, response):
        sel = scrapy.Selector(response)
        for text in response.xpath("//div[@class='quote']/span[@class='text']/text()").extract():
            print (text)
        for nextpage in response.xpath("//li[@class='next']/a/@href").extract():
            yield scrapy.Request(response.urljoin(nextpage), callback=self.parse)