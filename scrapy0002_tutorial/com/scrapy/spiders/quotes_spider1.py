import scrapy
class QuotesSpider1(scrapy.Spider):
    name = "quotes1"
    start_urls = [
        'http://quotes.toscrape.com/page/1/'
    ]
    def parse(self, response):
        print("demo1:保存抓取的数据到文件")
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)