import time
import scrapy
class QuotesSpider4(scrapy.Spider):
    name = 'author'
    start_urls = ['http://quotes.toscrape.com/']
    print("demo4:列表页和详情页递归")
    def parse(self, response):
        for href in response.css('.author + a::attr(href)').extract():
            #详情页抓取
           yield scrapy.Request(response.urljoin(href),
                                 callback=self.parse_author)
        next_page = response.css('li.next a::attr(href)').extract_first()
        #线程暂停3s
        time.sleep(3) 
        #下一页抓取
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse) 
    def parse_author(self, response):
        def extract_with_css(query):
            return response.css(query).extract_first().strip()
        yield {
            'name': extract_with_css('h3.author-title::text'),
            'birthdate': extract_with_css('.author-born-date::text'),
            'bio': extract_with_css('.author-description::text'),
        }

               